#!/usr/bin/env python3
"""
SessionExpAuth module
"""
import os
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """SessionExpAuth class"""
    def __init__(self):
        """init the class and assign the session duration"""
        try:
            loc_session_duration = int(os.getenv('SESSION_DURATION'))
        except (Exception):
            loc_session_duration = 0
        self.session_duration = loc_session_duration

    def create_session(self, user_id=None):
        """create a new Session"""
        SessionID = super().create_session(user_id)
        if SessionID:
            session_dictionary = {'user_id': user_id,
                                  'created_at': datetime.now()
                                  }
            self.user_id_by_session_id[SessionID] = session_dictionary
            return SessionID
        return None

    def user_id_for_session_id(self, session_id=None):
        """Overload session_auth and return a User ID based on a Session ID"""
        if session_id is None or type(session_id) != str:
            return None
        if session_id not in self.user_id_by_session_id.keys():
            return None
        user = self.user_id_by_session_id[session_id]
        if user is None:
            return None
        if 'created_at' not in user.keys():
            return None
        if self.session_duration <= 0:
            return user['user_id']
        if ((user['created_at'] + timedelta(seconds=self.session_duration)) <
                datetime.now()):
            return None
        return user['user_id']
