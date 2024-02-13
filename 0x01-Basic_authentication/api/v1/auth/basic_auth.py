#!/usr/bin/env python3
"""
Basic Auth module
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth class"""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        returns the Base64 part of the Authorization header for a Basic Authentication
        Args:
            authorization_header:

        Returns:

        """
        if authorization_header:
            if type(authorization_header) == str:
                if authorization_header.startswith('Basic '):
                    return authorization_header.split(' ')[1]
        return None
                    