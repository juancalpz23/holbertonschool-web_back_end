#!/usr/bin/env python3
"""
DB module: Handles database interactions with SQLAlchemy.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from user import Base, User


class DB:
    """
    DB class for managing database operations.
    """

    def __init__(self) -> None:
        """
        Initialize a new DB instance, setting up the SQLite database.
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """
        Memoized session object. This ensures only one
        session is active at a time.
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Add a new user to the database.
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)  # Stage the new user for insertion
        self._session.commit()  # Commit the transaction to save the user
        return new_user  # Return the created User object
