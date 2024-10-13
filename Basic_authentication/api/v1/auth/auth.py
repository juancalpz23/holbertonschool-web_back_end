#!/usr/bin/env python3
"""
Auth class for API authentication management
"""

from typing import List, TypeVar
from flask import request


class Auth:
    """
    Template class for API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path.

        Returns:
            - True if path is None
            - True if excluded_paths is None or empty
            - False if path is in excluded_paths
        """
        if path is None:
            return True

        if not excluded_paths:
            return True

        # Ensure trailing slash tolerance
        normalized_path = path if path.endswith('/') else f"{path}/"

        # Check if the normalized path exists in excluded_paths
        return normalized_path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the Authorization header from the Flask request object.
        For now, always returns None.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user from the Flask request object.
        For now, always returns None.
        """
        return None
