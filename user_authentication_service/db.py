#!/usr/bin/env python3
"""
DB module: Handles database interactions with SQLAlchemy.
"""

import bcrypt
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import NoResultFound, InvalidRequestError
from user import Base, User


class DB:
    """
    DB class for managing database operations.
    """

    def __init__(self) -> None:
        """
        Initialize a new DB instance, setting up the SQLite database.
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
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

    def _hash_password(self, password: str) -> bytes:
        """
        Hash a password using bcrypt.
        """
        salt = bcrypt.gensalt()  # Generate a salt
        return bcrypt.hashpw(password.encode(), salt)  # Return hashed password


    def add_user(self, email: str, password: str) -> User:
        """
        Add a new user to the database.
        """
        hashed_password = self._hash_password(password)
        new_user = User(email=email, hashed_password=hashed_password.decode())
        self._session.add(new_user)  # Stage the new user for insertion
        self._session.commit()  # Commit the transaction to save the user
        return new_user  # Return the created User object

    def find_user_by(self, **kwargs) -> User:
        """
        Find a user by arbitrary keyword arguments.
        """
        try:
            return self._session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise NoResultFound("No user found matching the criteria.")
        except InvalidRequestError:
            raise InvalidRequestError("Invalid query arguments provided.")

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Update a user's attributes.
        """
        user = self.find_user_by(id=user_id)  # Find the user to update

        for key, value in kwargs.items():
            if not hasattr(user, key):
                raise ValueError(f"Invalid attribute: {key}")
            setattr(user, key, value)  # Update the attribute

        self._session.commit()  # Commit the changes
