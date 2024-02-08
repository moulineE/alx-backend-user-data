#!/usr/bin/env python3
"""Task 5. Encrypting passwords module"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    function that expects one string argument name password and
    returns a salted, hashed password, which is a byte string
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
