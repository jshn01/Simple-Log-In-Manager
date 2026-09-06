import hashlib
import json
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, 'data.json')
# constants
sha256 = hashlib.sha256()

def createPage():
    running = True
    isUsernameTaken = False
    with open(file_path) as f:
        users = json.load(f) or []
    
    while running == True:
        username = input("Please enter a username: ")
        for i in users:
            if i["user"] == username:
                isUsernameTaken = True
                running = False
        if isUsernameTaken == True:
            print("The username is already taken")
            isUsernameTaken = False
            running = True
        else:
            break
    
    password = input("Please enter a strong password: ")
    sha256.update(password.encode())
    hashPassword = sha256.hexdigest()

    data = {"user" : username, "password" : hashPassword}
        
    users.append(data)
    with open(file_path, "w") as f:
        json.dump(users, f, indent=2)
        print("Account created")
