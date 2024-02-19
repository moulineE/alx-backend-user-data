# 0x03. User Authentication Service

## Introduction
Welcome to the 0x03 User Authentication Service project! In this project, you'll be building a user authentication service from scratch using Python and Flask. Unlike in industry practice, where you'd typically use existing authentication frameworks, here you'll walk through each step of the authentication mechanism to understand it thoroughly.

## Project Overview
- **Back-end**: This project focuses on building the backend logic for user authentication.
- **Authentication**: You'll implement user authentication functionalities such as user registration, login, logout, password reset, etc.
- **By**: Emmanuel Turlay, Staff Software Engineer at Cruise
- **Weight**: 1

## Learning Objectives
By the end of this project, you will be able to:
- Declare API routes in a Flask app.
- Manage user sessions and cookies.
- Retrieve request form data and handle it appropriately.
- Return various HTTP status codes to indicate the success or failure of operations.
- Work with SQLAlchemy for database interactions.

## Setup
To get started with this project, ensure you have Python 3.7 installed on your system. You'll also need to install the required packages using pip:
```bash
pip3 install bcrypt
```

## Tasks Overview
Here's a brief overview of the tasks involved in this project:
0. **User Model**: Define a SQLAlchemy model for the User entity.
1. **Create User**: Implement the functionality to add a new user to the database.
2. **Find User**: Implement a method to find a user by email.
3. **Update User**: Implement the functionality to update user attributes.
4. **Hash Password**: Define a method to hash passwords securely.
5. **Register User**: Create an endpoint to register new users.
6. **Basic Flask App**: Set up a basic Flask app with a single GET route.
7. **Register user**: implement the end-point to register a user.
8. **Credentials Validation**: Implement user credentials validation.
9. **Generate UUIDs**: Define a method to generate UUIDs for sessions.
10. **Get Session ID**: Implement session creation functionality.
11. **Log in**: Implement the login functionality.
12. **Find User by Session ID**: Implement functionality to find a user by session ID.
13. **Destroy Session**: Implement session destruction functionality.
14. **Log out**: Implement the logout functionality.
15. **User Profile**: Implement the user profile endpoint.
16. **Generate Reset Password Token**: Implement functionality to generate reset password tokens.
17. **Get Reset Password Token**: Implement the endpoint to get reset password tokens.
18. **Update Password**: Implement functionality to update user passwords.
19. **Update Password Endpoint**: Implement the endpoint to update user passwords.
