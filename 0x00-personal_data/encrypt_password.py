#!/usr/bin/env python3
"""Task 5. Encrypting passwords module"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    function that expects one string argument name password and
    returns a salted, hashed password, which is a byte string
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """function that the provided password matches the hashed password"""
    if bcrypt.checkpw(password.encode(), hashed_password):
        return True
    else:
        return False
