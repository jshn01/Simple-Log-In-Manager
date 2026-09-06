import json
import hashlib
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, 'data.json')
def loginPage():
    running = True
    matchFound = False
    with open(file_path) as f:
        users = json.load(f) or []
    
    while running == True:
        username = input("Please enter your username: ")
        print("")
        password = input("Please enter your password: ")

        hashPassword = encryptedPass(password=password)
        data = {"user": username, "password": hashPassword}
        for i in users:
            if i == data:
                print("-----------")
                print("You have successfully logged in.")
                print("------------")
                matchFound = True
                running = False
                break
        if matchFound == False:
            running = True
            print("------------")
            print("The username or password was wrong, please try again.")
            print("------------")

def encryptedPass(password):
    sha256 = hashlib.sha256()
    sha256.update(password.encode())
    hashPassword = sha256.hexdigest()
    return hashPassword

