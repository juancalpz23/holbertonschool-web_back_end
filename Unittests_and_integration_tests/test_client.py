#!/usr/bin/env python3
"""
Unit tests for the GithubOrgClient class from the client module.
"""

import unittest
from unittest.mock import patch, PropertyMock, call, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for GithubOrgClient."""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"})
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected_payload, mock_get_json):
        """
        Test that the org property returns the correct value.
        Ensures that get_json is called once with the expected argument.
        """
        mock_get_json.return_value = expected_payload
        client = GithubOrgClient(org_name)

        self.assertEqual(client.org, expected_payload)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Test that the _public_repos_url property returns the correct value.
        """
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/google/repos"}
        client = GithubOrgClient("google")

        self.assertEqual(
            client._public_repos_url,
            "https://api.github.com/orgs/google/repos")
        mock_org.assert_called_once()

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Test that public_repos returns the expected list of repository names.
        """
        mock_get_json.return_value = [{"name": "repo1"}, {"name": "repo2"}]
        repos_url = "https://api.github.com/orgs/google/repos"

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_repos_url:
            mock_repos_url.return_value = repos_url
            client = GithubOrgClient("google")

            repos = client.public_repos()
            self.assertEqual(repos, ["repo1", "repo2"])

            mock_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(repos_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test that has_license correctly identifies whether a repo
        has the given license key.
        """
        client = GithubOrgClient("test_org")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for the GithubOrgClient."""

    @classmethod
    def setUpClass(cls):
        """Set up mocks and patch requests for integration testing."""
        org = cls.org_payload
        repos = cls.repos_payload

        cls.org_mock = Mock()
        cls.org_mock.json.return_value = org

        cls.repos_mock = Mock()
        cls.repos_mock.json.return_value = repos

        cls.get_patcher = patch('requests.get')
        cls.get = cls.get_patcher.start()

        # Define mock behavior for requests
        options = {org["repos_url"]: cls.repos_mock}
        cls.get.side_effect = lambda url: options.get(url, cls.org_mock)

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test that public_repos returns the expected repositories."""
        client = GithubOrgClient("x")

        self.assertEqual(client.org, self.org_payload)
        self.assertEqual(client.repos_payload, self.repos_payload)
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.assertEqual(client.public_repos("NONEXISTENT"), [])

        self.get.assert_has_calls([
            call("https://api.github.com/orgs/x"),
            call(self.org_payload["repos_url"])
        ])

    def test_public_repos_with_license(self):
        """Test that public_repos filters repositories by license."""
        client = GithubOrgClient("x")

        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)
        self.assertEqual(client.public_repos("NONEXISTENT"), [])

        self.get.assert_has_calls([
            call("https://api.github.com/orgs/x"),
            call(self.org_payload["repos_url"])
        ])
