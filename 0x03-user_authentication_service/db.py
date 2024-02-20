#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email, hashed_password) -> User:
        """
        Add a user in the db
        :param email:
        :param hashed_password:
        :return:
        """
        new_user = User(email=email, hashed_password=hashed_password)
        try:
            self.new(new_user)
            self.save()
        except Exception:
            self._session.rollback()
            raise
        return new_user

    def new(self, obj):
        """Add the object to the current database session"""
        self._session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self._session.commit()

    def find_user_by(self, **kwargs):
        """
        method that find user row by an arbitrary keyword arguments
        :return:
            first row found in the users table as filtered by the method’s
            input arguments
        """
        try:
            user = self._session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise NoResultFound()
        except InvalidRequestError:
            raise InvalidRequestError()
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        method that update a user
        :param user_id:
        :param kwargs:
        :return:
        """
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if not hasattr(user, key):
                raise ValueError
            setattr(user, key, value)
        self.save()
