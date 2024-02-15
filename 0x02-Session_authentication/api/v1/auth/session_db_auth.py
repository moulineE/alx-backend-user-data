#!/usr/bin/env python3
"""
Session_db_auth module
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import datetime, timedelta


class SessionDBAuth(SessionExpAuth):
    """Session_db_auth class"""
    tmp_sdate = datetime.now()

    def create_session(self, user_id=None):
        """overload session_exp_auth and create a new Session"""
        SessionID = super().create_session(user_id)
        kwargs = {
            'user_id': user_id,
            'session_id': SessionID,
        }
        user = UserSession(**kwargs)
        user.save()
        return SessionID

    def user_id_for_session_id(self, session_id=None):
        """
        Overload session_exp_auth and return a User ID based on a Session ID
        """
        try:
            users = UserSession.search({'session_id': session_id})
        except (Exception):
            return None
        if len(users) <= 0:
            return None
        self.session_duration
        if users is None:
            return None
        if self.session_duration <= 0:
            return users[0].user_id
        if ((self.tmp_sdate + timedelta(seconds=self.session_duration)) <
                datetime.now()):
            return None
        return users[0].user_id

    def destroy_session(self, request=None):
        """method that deletes the user session / logout"""
        if request:
            SessionID = self.session_cookie(request)
            if SessionID is not None:
                user_session = UserSession.search({"session_id": session_id})
                if len(user_session) <= 0:
                    user_session[0].remove()
                    return True
        return False
