#!/usr/bin/env python3
"""auth module"""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4
from user import User


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        method that register new users
        :param email:
        :param password:
        :return:
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            hashed_pass = _hash_password(password)
            user = self._db.add_user(email, hashed_pass)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """
        method that the provided password matches the hashed password for
        a given user
        :param email:
        :param password:
        :return:
        """
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode(), user.hashed_password):
                return True
            else:
                return False
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """
        method that create a new session id and assign it to a user
        :param email:
        :return:
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        try:
            self._db.update_user(user_id, session_id=None)
        except NoResultFound:
            raise ValueError('user id not found')

    def get_user_from_session_id(self, session_id):
        """
        method that find a user by session_id
        :param session_id:
        :return:
        """
        if session_id:
            try:
                user = self._db.find_user_by(session_id=session_id)
                return user
            except NoResultFound:
                pass
        return None

    def get_reset_password_token(self, email: str) -> str:
        """
        method that reset the user password token
        :param email:
        :return:
        """
        try:
            user = self._db.find_user_by(email=email)
            reset_token = _generate_uuid()
            self._db.update_user(user.id, reset_token=reset_token)
            return reset_token
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """
        method that update the password
        :param reset_token:
        :param password:
        :return:
        """
        if reset_token is None or password is None:
            return None
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError
        hashed_password = _hash_password(password)
        self._db.update_user(user.id, hashed_password=hashed_password,
                             reset_token=None)


def _hash_password(password: str) -> bytes:
    """
    function that expects one string argument name password and
    returns a salted, hashed password, which is a byte string

    :param password:
    :return:
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def _generate_uuid() -> str:
    """function that generate & return a string representation of a UUID"""
    return str(uuid4())
