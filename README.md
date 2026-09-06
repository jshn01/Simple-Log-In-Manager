# Simple-Log-In-Manager
Simple Log In Manager written in python, uses JSON files to store log ins, encrypts passwords using the SHA256 Algorithm.
# How it works
- This Log In Manager allows a user to input their username and password.
- The password is then encrypted with an SHA256 algorithm and both the username and password hash is put in a JSON file.
- When logging in, the system checks against the user's inputted log in with the system's, if the hash of the passwords match, then the user will be granted access.
# Requirements
- python 3.x
# How to use
- Make sure to run the main.py file
