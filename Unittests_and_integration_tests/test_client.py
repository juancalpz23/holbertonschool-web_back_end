#!/usr/bin/env python3
"""
Unit tests for the GithubOrgClient class from the client module.
"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


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
