#!/usr/bin/env python3
"""
Password hasher function
"""


import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt with a randomly-generated salt
    """
    # Generate a salt
    salt = bcrypt.gensalt()

    # Hash the password using bcrypt with the salt
    hashed_password = bcrypt.hashpw(password.encode(), salt)

    return hashed_password
