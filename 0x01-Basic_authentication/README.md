# 0x01. Basic Authentication

## Back-end

**Authentication**

By: Guillaume, CTO at Holberton School

**Weight:** 1

**Project Duration:** Feb 12, 2024, 4:00 AM - Feb 14, 2024, 4:00 AM

**Checker Release:** Feb 12, 2024, 4:00 PM

**Auto Review:** At the deadline

## Background Context

In this project, you will learn about the authentication process and implement Basic Authentication on a simple API.

In the industry, it's recommended not to implement your own Basic authentication system and instead use a module or framework that does it for you (like Flask-HTTPAuth in Python-Flask). However, for learning purposes, we will walk through each step of this mechanism to understand it thoroughly.

## Resources

Read or watch:

- [REST API Authentication Mechanisms](#)
- [Base64 in Python](#)
- [HTTP header Authorization](#)
- [Flask](#)
- [Base64 - concept](#)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

- What authentication means
- What Base64 is
- How to encode a string in Base64
- What Basic authentication means
- How to send the Authorization header

## Requirements

### Python Scripts

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class, or method (the length of it will be verified)

## Tasks

### 0. Simple-basic-API
### 1. Error handler: Unauthorized
### 2. Error handler: Forbidden
### 3. Auth class
### 4. Define which routes don't need authentication
### 5. Request validation!
### 6. Basic auth
### 7. Basic - Base64 part
### 8. Basic - Base64 decode
### 9. Basic - User credentials
### 10. Basic - User object
### 11. Basic - Overload current_user - and BOOM!

**Repo:**

- GitHub repository: [alx-backend-user-data](https://github.com/moulineE/alx-backend-user-data)
- Directory: `0x01-Basic_authentication`