#!/usr/bin/env python3
"""
Auth module
"""
from flask import request
from typing import List, TypeVar
import fnmatch


class Auth:
    """Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Method to determin if a path need authentification
        Args:
            path:
            excluded_paths:

        Returns:

        """
        if path is None:
            return True
        if not excluded_paths:
            return True
        if not path.endswith('/'):
            path += '/'
        for excluded_path in excluded_paths:
            if not excluded_path.endswith('/'):
                excluded_path += ('/')
            if fnmatch.fnmatch(path, excluded_path):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """

        Args:
            request:

        Returns:

        """
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """

        Args:
            request:

        Returns:

        """
        return None
