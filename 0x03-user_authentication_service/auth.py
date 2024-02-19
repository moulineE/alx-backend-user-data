#!/usr/bin/env python3
"""auth module"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    function that expects one string argument name password and
    returns a salted, hashed password, which is a byte string

    :param password:
    :return:
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
