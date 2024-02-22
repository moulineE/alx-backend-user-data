#!/usr/bin/env python3
"""
Main file End-to-end integration test
"""
import requests
import time


def register_user(email: str, password: str) -> None:
    """
    test /users endpoint
    :param email:
    :param password:
    :return:
    """
    url = 'http://0.0.0.0:5000/users'
    data = {
        'email': email,
        'password': password
    }
    response = requests.post(url, data=data)
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "user created"}
    response = requests.post(url, data=data)
    assert response.status_code == 400
    assert response.json() == {"message": "email already registered"}


def log_in_wrong_password(email: str, password: str) -> None:
    """
    test /sessions endpoint with wrong password
    :param email:
    :param password:
    :return:
    """
    url = 'http://0.0.0.0:5000/sessions'
    data = {
        'email': email,
        'password': password
    }
    response = requests.post(url, data=data)
    time.sleep(0.1)
    assert response.status_code == 401


def log_in(email: str, password: str) -> str:
    """
    test /sessions endpoint with correct password
    :param email:
    :param password:
    :return:
    """
    url = 'http://0.0.0.0:5000/sessions'
    data = {
        'email': email,
        'password': password
    }
    response = requests.post(url, data=data)
    time.sleep(1)
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "logged in"}
    return response.cookies.get('session_id')


def profile_unlogged() -> None:
    """
   test /profile endpoint while unlogged
    :return:
    """
    url = 'http://0.0.0.0:5000/profile'
    response = requests.get(url)
    time.sleep(1)
    assert response.status_code == 403


def profile_logged(session_id: str) -> None:
    """
    test /profile endpoint with GET method while logged
    :param session_id:
    :return:
    """
    url = 'http://0.0.0.0:5000/profile'
    cookies = {
        'session_id': session_id
    }
    response = requests.get(url, cookies=cookies, )
    time.sleep(1)
    assert response.status_code == 200
    assert response.json() == {"email": EMAIL}


def log_out(session_id: str) -> None:
    """test /sessions endpoint wit DELETE method while logged"""
    url = 'http://0.0.0.0:5000/sessions'
    cookies = {
        'session_id': session_id
    }
    response = requests.delete(url, cookies=cookies)
    time.sleep(1)
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenue"}


def reset_password_token(email: str) -> str:
    """
    test /reset_password endpoint with POST method to get a reset token
    :param email:
    :return:
    """
    url = 'http://0.0.0.0:5000/reset_password'
    data = {
        'email': email
    }
    response = requests.post(url, data=data)
    time.sleep(1)
    assert response.status_code == 200
    reset_token = response.json().get('reset_token')
    assert response.json() == {"email": email, "reset_token": reset_token}
    return reset_token


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """
    test /reset_password endpoint with PUT method to update user password
    :param email:
    :param reset_token:
    :param new_password:
    :return:
    """
    url = 'http://0.0.0.0:5000/reset_password'
    data = {
        'email': email,
        'reset_token': reset_token,
        'new_password': new_password
    }
    response = requests.put(url, data=data)
    time.sleep(1)
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "Password updated"}


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
