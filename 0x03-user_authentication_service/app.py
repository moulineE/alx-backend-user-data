#!/usr/bin/env python3
"""Flask app"""
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/')
def Bienvenue():
    """basic Bienvenue message root route"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """Register user"""
    email = request.form['email']
    password = request.form['password']
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    """Log in route"""
    email = request.form['email']
    password = request.form['password']
    if AUTH.valid_login(email, password):
        sessionID = AUTH.create_session(email)
        resp = jsonify({"email": email, "message": "logged in"})
        resp.set_cookie("session_id", sessionID)
        return resp
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'])
def logout():
    """log out route"""
    sessionID = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(sessionID)
    if user:
        AUTH.destroy_session(user.id)
        return redirect('/')
    else:
        abort(403)


@app.route('/profile')
def profile():
    """get user profile"""
    sessionID = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(sessionID)
    if user:
        return jsonify({"email": user.email}), 200
    else:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
