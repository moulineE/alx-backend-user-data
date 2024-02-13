#!/usr/bin/env python3
"""
Basic Auth module
"""
import base64

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        returns the Base64 part of the Authorization header for
        a Basic Authentication
        Args:
            authorization_header:

        Returns:

        """
        if authorization_header:
            if type(authorization_header) == str:
                if authorization_header.startswith('Basic '):
                    return authorization_header.split(' ')[1]
        return None

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        a method that decode a Base64 string
        Args:
            base64_authorization_header:

        Returns:
            decoded value of a Base64 string

        """
        if base64_authorization_header:
            if type(base64_authorization_header) == str:
                try:
                    return (base64.b64decode(
                        base64_authorization_header, validate=True)
                            .decode('utf-8'))
                except (Exception):
                    return None
        return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        return user credentials
        Args:
            decoded_base64_authorization_header:

        Returns:
            returns the user email and password from the Base64 decoded value

        """
        if decoded_base64_authorization_header:
            if type(decoded_base64_authorization_header) == str:
                user_credentials = (decoded_base64_authorization_header.
                                    split(':'))
                if len(user_credentials) == 2:
                    return tuple(user_credentials)
        return None, None
