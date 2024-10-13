#!/usr/bin/env python3
"""
Module for Session Authentication
"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User
from os import getenv


class SessionAuth(Auth):
    """
    Session Authentication class that inherits from Auth
    """

    user_id_by_session_id = {}  # Class attribute

    def create_session(self, user_id: str = None) -> str:
        """
        Create a Session ID for a user_id
        """
        if user_id is None or not isinstance(user_id, str):
            return None  # Return None if user_id is invalid

        # Generate a new Session ID
        session_id = str(uuid.uuid4())

        # Store the user_id in the dictionary using session_id as the key
        self.user_id_by_session_id[session_id] = user_id

        return session_id  # Return the created Session ID

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Return a User ID based on a Session ID
        """
        if session_id is None or not isinstance(session_id, str):
            return None  # Return None if session_id is invalid

        # Use .get() to retrieve the user ID from the dictionary
        return self.user_id_by_session_id.get(session_id)

    def session_cookie(self, request=None):
        """
        Returns the session cookie value from the request
        """
        if request is None:
            return None

        return request.cookies.get(getenv("SESSION_NAME", "_my_session_id"))

    def current_user(self, request=None):
        """
        Returns the User instance based on a session ID from the cookie
        """
        session_id = self.session_cookie(request)  # Get session ID from cookie
        user_id = self.user_id_for_session_id(session_id)  # Get user ID

        if user_id is None:
            return None  # No user associated with the session ID

        return User.get(user_id)

    def destroy_session(self, request=None) -> bool:
        """ Deletes the user session (logout) """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False

        del self.user_id_by_session_id[session_id]
        return True
