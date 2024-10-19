#!/usr/bin/env python3
"""
Authentication module for user registration and password management.
"""

import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt.
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)


def _generate_uuid() -> str:
    """
    Generate a new UUID and return its string representation.

    This is a private function, meant to be used internally in the module.
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self) -> None:
        """Initialize a new Auth instance."""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user with the provided email and password.
        """
        try:
            # Check if a user with the given email already exists
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists.")
        except NoResultFound:
            # If user does not exist, proceed with registration
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password.decode())
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate user login credentials.
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode(),
                                  user.hashed_password.encode())
        except (NoResultFound, AttributeError):
            return False

    def create_session(self, email: str) -> str:
        """
        Create a new session ID for the user with the given email
        """
        try:
            user = self._db.find_user_by(email=email)  # Find user by email
            session_id = _generate_uuid()  # Generate a new UUID for session
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return ""

    def get_user_from_session_id(self, session_id: str) -> User | None:
        """
        Find and return the user associated with the given session ID.
        If no user is found, return None.
        """
        if session_id is None:
            return None
        try:
            _user = self._db.find_user_by(session_id=session_id)
            return _user
        except NoResultFound:
            return None
