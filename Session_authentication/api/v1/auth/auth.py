#!/usr/bin/env python3


"""
Auth class for API authentication management
"""

from typing import List, TypeVar
from flask import request
from os import getenv


class Auth:
    """
    Template class for API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path.
        """
        if path is None:
            return True
        if not excluded_paths:
            return True

        normalized_path = path if path.endswith('/') else f"{path}/"
        return normalized_path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the Authorization header from the Flask request object.
        """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user from the Flask request object.
        """
        return None

    def session_cookie(self, request=None) -> str:
        """
        Retrieve the session cookie value from the request
        """
        if request is None:
            return None  # Return None if request is None

        # Get the cookie name from the environment variable SESSION_NAME
        cookie_name = getenv("SESSION_NAME", "_my_session_id")

        # Return the value of the specified cookie using .get()
        return request.cookies.get(cookie_name)
