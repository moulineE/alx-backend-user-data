Certainly! Below is the README.md file for the project "0x02. Session Authentication":

---

# 0x02. Session Authentication

**Project Description:** This project aims to implement Session Authentication without the use of external modules or frameworks. It involves understanding the concept of authentication, particularly session authentication, and working with cookies in a Flask application.

- **Project Start:** February 14, 2024, 4:00 AM
- **Project End:** February 16, 2024, 4:00 AM
- **Checker Release:** February 14, 2024, 4:00 PM
- **Auto Review Deadline:** February 16, 2024, 4:00 AM

**Background Context:** In this project, you will implement a Session Authentication mechanism. Unlike industry standards where pre-built modules or frameworks are preferred, we'll delve into understanding the intricacies by building it from scratch.

**Resources:**
- [REST API Authentication Mechanisms](https://www.youtube.com/watch?v=501dpx2IjGY) - Focus on session auth
- [HTTP Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cookie)
- [Flask](https://palletsprojects.com/p/flask/)
- [Flask Cookie](https://flask.palletsprojects.com/en/1.1.x/quickstart/#cookies)

**Learning Objectives:** By the end of this project, you should be able to explain the following concepts without external assistance:

- Understand authentication principles
- Grasp the essence of session authentication
- Know how cookies work
- Implement sending and parsing cookies in Flask applications

**Requirements:**

- **Python Scripts:** All scripts will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- **Documentation:** All code files should have proper documentation following specified guidelines.
- **Code Style:** Pycodestyle should be adhered to (version 2.5).
- **Execution:** All files must be executable.
- **Length and Documentation:** The length and documentation of code will be checked.
- **Modules and Classes:** All modules and classes should have proper documentation.

## Tasks

### 0. Et moi et moi et moi!

**Objective:** Copy all work from the previous Basic Authentication project into this new folder and update it to include a new endpoint.

- Copy folders and files from the previous project.
- Implement a new endpoint `GET /users/me` to retrieve the authenticated User object.

### 1. Empty session

**Objective:** Create a SessionAuth class inheriting from Auth and validate the inheritance without overloading.

- Update `api/v1/app.py` to use `SessionAuth` instance based on the value of the environment variable `AUTH_TYPE`.

### 2. Create a session

**Objective:** Implement methods to create and manage session IDs in the `SessionAuth` class.

- Create a class attribute `user_id_by_session_id` for storing session IDs.
- Implement a method `create_session` to generate a session ID for a given user ID.

### 3. User ID for Session ID

**Objective:** Implement a method to retrieve a user ID based on a session ID in the `SessionAuth` class.

- Implement a method `user_id_for_session_id` to retrieve a user ID based on a session ID.

### 4. Session cookie

**Objective:** Add functionality to extract session ID from cookies in the `Auth` class.

- Implement a method `session_cookie` to extract session ID from cookies in a request.

### 5. Before request

**Objective:** Update the `@app.before_request` method in `api/v1/app.py` to handle session authentication.

- Exclude `/api/v1/auth_session/login/` from authentication.
- Return a 401 error if authentication headers or session cookies are missing.

### 6. Use Session ID for identifying a User

**Objective:** Implement a method to get the current user based on the session ID in the `SessionAuth` class.

- Implement a method `current_user` to return the User instance based on the session ID.

### 7. New view for Session Authentication

**Objective:** Create a new Flask view to handle session authentication.

- Create a route `POST /auth_session/login` to handle session login.
- Validate email and password parameters.
- Return appropriate error responses or create a session ID for the user.

### 8. Logout

**Objective:** Implement a method to destroy a session and log out the user.

- Implement a method `destroy_session` to delete the user session.

---
