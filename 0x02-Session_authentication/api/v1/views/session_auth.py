#!/usr/bin/env python3
""" Module of session auth views
"""
import os

from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session_login():
    """
    POST /auth_session/login
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None or email == '':
        return jsonify({"error": "email missing"}), 400
    if password is None or password == '':
        return jsonify({"error": "password missing"}), 400
    try:
        users = User.search({'email': email})
        if len(users) == 0:
            return jsonify({"error": "no user found for this email"}), 404
    except (Exception):
        return jsonify({"error": "no user found for this email"}), 404
    for user in users:
        if user.is_valid_password(password):
            from api.v1.app import auth
            SessionID = auth.create_session(user.id)
            resp = jsonify(user.to_json())
            session_name = os.getenv('SESSION_NAME')
            resp.set_cookie(session_name, SessionID)
            return resp
    return jsonify({"error": "wrong password"}), 401
