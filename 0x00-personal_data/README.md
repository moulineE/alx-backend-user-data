## 0x00. Personal Data

### Introduction
This project focuses on implementing features related to handling personal data securely in a backend environment. It covers topics such as filtering sensitive information in log messages, encrypting passwords, authenticating users, and connecting securely to databases.

### Learning Objectives
Upon completing this project, you should be able to:
- Identify examples of Personally Identifiable Information (PII)
- Implement a log filter to obfuscate PII fields in log messages
- Encrypt passwords securely and validate user input against hashed passwords
- Authenticate to a database using environment variables

### Requirements
- Ubuntu 18.04 LTS
- Python 3.7
- pycodestyle 2.5
- bcrypt package
- MySQL database

### Tasks
0. **Regex-ing**: Write a function to obfuscate sensitive fields in log messages using regular expressions.
1. **Log Formatter**: Implement a log formatter that redacts specified fields in log messages.
2. **Create Logger**: Implement a function to create a logger object that handles sensitive information.
3. **Connect to Secure Database**: Connect to a secure database using environment variables for credentials.
4. **Read and Filter Data**: Retrieve data from a database and display it with sensitive fields filtered in log messages.
5. **Encrypting Passwords**: Implement a function to hash passwords securely using bcrypt.
6. **Check Valid Password**: Validate user passwords against hashed passwords using bcrypt.


### Resources
- [What Is PII, non-PII, and Personal Data?](https://piwik.pro/blog/what-is-pii-personal-data/)
- [Logging Documentation](https://docs.python.org/3/library/logging.html)
- [bcrypt Package](https://github.com/pyca/bcrypt/)
- [Logging to Files, Setting Levels, and Formatting](https://www.youtube.com/watch?v=-ARI4Cz-awo)