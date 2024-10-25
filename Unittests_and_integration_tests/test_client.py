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
    """Test class for GithubOrgClient."""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"})
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected_payload, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.
        Ensure get_json is called once with the expected argument
        and returns the expected payload.
        """
        # Configure the mock to return the expected payload
        mock_get_json.return_value = expected_payload

        # Instantiate the GithubOrgClient with the provided org_name
        client = GithubOrgClient(org_name)

        # Assert the .org method returns the correct payload
        self.assertEqual(client.org, expected_payload)

        # Assert that get_json was called exactly once with the correct URL
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Test that _public_repos_url returns the correct value based on
        the mocked org property.
        """
        # Define the payload for the mock
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/google/repos"}

        # Instantiate the client
        client = GithubOrgClient("google")

        # Assert the _public_repos_url property matches the expected repos_url
        self.assertEqual(client._public_repos_url,
                         "https://api.github.com/orgs/google/repos")

        # Verify that the org property was accessed exactly once
        mock_org.assert_called_once()

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Test that public_repos returns the expected list of repositories.
        """
        # Define mock payload and _public_repos_url value
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
        ]
        repos_url = "https://api.github.com/orgs/google/repos"

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_repos_url:
            mock_repos_url.return_value = repos_url

            # Instantiate the client
            client = GithubOrgClient("google")

            # Call public_repos method
            repos = client.public_repos()

            # Assert the returned list matches the expected repo names
            self.assertEqual(repos, ["repo1", "repo2"])

            # Assert the mocked property and get_json were called once
            mock_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(repos_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test that has_license returns the correct boolean value.
        """
        client = GithubOrgClient("test_org")

        # Call has_license and compare result to expected value
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)

    @classmethod
    def setUpClass(cls):
        """Set up the class-level mocks for external requests."""
        cls.get_patcher = patch("requests.get")

        # Start patcher and configure side_effect for URL-based responses
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.side_effect = cls.mocked_requests_get


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
@classmethod
def setUpClass(cls):
    """Set up resources and mock requests for testing."""
    # Initialize mocks for the org and repos payloads
    org = cls.org_payload
    repos = cls.repos_payload

    cls.org_mock = Mock()
    cls.org_mock.json = Mock(return_value=org)

    cls.repos_mock = Mock()
    cls.repos_mock.json = Mock(return_value=repos)

    # Start patching 'requests.get' method globally
    cls.get_patcher = patch('requests.get')
    cls.get = cls.get_patcher.start()

    # Configure side effects to return correct mock objects
    url_map = {org["repos_url"]: cls.repos_mock}
    cls.get.side_effect = lambda url: url_map.get(url, cls.org_mock)


@classmethod
def tearDownClass(cls):
    """Clean up and stop the patcher after tests."""
    cls.get_patcher.stop()


def test_public_repos(self):
    """Test that public_repos returns the expected repository list."""
    client = GithubOrgClient("test_org")

    # Check that public_repos returns the correct list from the fixture
    self.assertEqual(client.public_repos(), self.expected_repos)

    # Ensure that the correct API calls were made
    self.get.assert_has_calls([
        call("https://api.github.com/orgs/test_org"),
        call(self.org_payload["repos_url"])
    ])


def test_public_repos_with_license(self):
    """Test public_repos with filtering by the 'apache-2.0' license."""
    client = GithubOrgClient("test_org")

    # Verify that public_repos filters correctly by license
    self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)

    # Verify that requests were made as expected
    self.get.assert_has_calls([
        call("https://api.github.com/orgs/test_org"),
        call(self.org_payload["repos_url"])
    ])
