#!/usr/bin/env python3
"""
SessionAuth module
"""
from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """SessionAuth class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        creates a Session ID for a user_id
        """
        if user_id is None or type(user_id) != str:
            return None
        SessionID = str(uuid4())
        self.user_id_by_session_id[SessionID] = user_id
        return SessionID

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        return a User ID based on a Session ID
        """
        if session_id is None or type(session_id) != str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """

        """
        SessionID = self.session_cookie(request)
        user_id = self.user_id_for_session_id(SessionID)
        return User.get(user_id)

    def destroy_session(self, request=None):
        """
        method that deletes the user session / logout
        """
        if request:
            SessionID = self.session_cookie(request)
            if SessionID is not None:
                if self.user_id_for_session_id(SessionID):
                    del self.user_id_by_session_id[SessionID]
                    return True
        return False
