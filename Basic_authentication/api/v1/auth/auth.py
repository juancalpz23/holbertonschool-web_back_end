#!/usr/bin/env python3
""" Auth class for API authentication management """


from typing import List, TypeVar
from flask import request


class Auth:
    """ Template class for API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path.
        For now, always returns False.
        """
        return False

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
