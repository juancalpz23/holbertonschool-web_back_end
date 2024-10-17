#!/usr/bin/env python3
"""
Authentication module for password hashing.
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt.
    """
    salt = bcrypt.gensalt()  # Generate a salt
    return bcrypt.hashpw(password.encode(), salt)
