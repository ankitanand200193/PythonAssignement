# Overview
This Python script checks the strength of a user-entered password. It ensures the password meets security requirements before granting access.

# Features
* Enforces strong password policies:
    * Minimum 8 characters
    * At least one digit
    * At least one uppercase letter
    * At least one lowercase letter
    * At least one special character
* Provides up to 3 attempts to enter a strong password.
* Displays appropriate messages based on password strength.

# Prerequisites
Ensure you have Python installed (Python 3.x recommended).

# Usage
Run the script with: **python password_check.py**

You will be prompted to enter a password. If it meets the strength criteria, you will see:
Strong password

Otherwise, you will be asked to try again, with a total of 3 attempts. If all attempts fail, access is denied.

# Password Requirements
A valid password must:

  * Be at least 8 characters long
  * Contain at least one digit
  * Include at least one uppercase letter
  * Include at least one lowercase letter
  * Have at least one special character from !@#$%^&*()-_=+[]{};:'",.<>?/\|~`

# Exception Handling
* After three failed attempts, access is denied.
* User-friendly messages guide the user on how to create a strong password.

# License
This project is open-source and available under the MIT License.

# Image
![Alt text](https://github.com/ankitanand200193/PythonAssignement/blob/b1935eb54d7a8d0ae3817888f730709c6103f929/password_screenshot.png)

