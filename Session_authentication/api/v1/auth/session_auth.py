#!/usr/bin/env python3
"""
Module for Session Authentication
"""
from api.v1.auth.auth import Auth
import uuid


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
