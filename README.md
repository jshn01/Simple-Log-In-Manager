# Simple-Log-In-Manager
Simple Log In Manager written in python, uses JSON files to store log ins, encrypts passwords using the SHA256 Algorithm.
# Warnings!
- This is just a side project, please do not use an SHA256 algorithm to store very important information, as it is easily brute forced because modern day computing is too powerful.
- I plan on changing the algorithm to one more robust to prevent brute forcing and many other ways to hack the system.
- If planning on making a project like this one, I suggest using Argon2 or bcrypt to encrypt the passwords and/or usernames. 
# How it works
- This Log In Manager allows a user to input their username and password.

![](/signin.png)
- The password is then encrypted with an SHA256 algorithm and both the username and password hash is put in a JSON file.
- When logging in, the system checks against the user's inputted log in with the system's, if the hash of the passwords match, then the user will be granted access.

![](/login.png)
# Requirements
- python 3.x
# How to use
- Make sure to run the main.py file
