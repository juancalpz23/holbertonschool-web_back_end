#!/usr/bin/env python3
"""
This module defines the SQLAlchemy User model for the 'users' table.
It contains attributes for user management, including email, password,
session ID, and reset token.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base class for all models
Base = declarative_base()


class User(Base):
    """
    User model for the 'users' table.
    """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
