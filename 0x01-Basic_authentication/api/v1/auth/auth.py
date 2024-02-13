#!/usr/bin/env python3
"""
Auth module
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """

        Args:
            path:
            excluded_paths:

        Returns:

        """
        return False

    def authorization_header(self, request=None) -> str:
        """

        Args:
            request:

        Returns:

        """
        return False

    def current_user(self, request=None) -> TypeVar('User'):
        """

        Args:
            request:

        Returns:

        """
        return None
