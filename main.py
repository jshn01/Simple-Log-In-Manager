from exit import exitPage
from create import createPage
from login import loginPage
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, 'data.json')
# Variables
running = True


def homePage():
    print("1 - Login")
    print("")
    print("---------------")
    print("")
    print("2 - Create an account")
    print("")
    print("---------------")
    print("3 - Exit")
    print("")

homePage()
try:
    while running:
        try:
            number = int(input("Please enter a number 1-3: "))
            if 1 <= number <= 3:
                running = False
            else:
                print("Enter a number between the ranges given")
        except:
            print("Please enter a number.")
            pass

    if number == 1:
        loginPage()
        input = input("Press ENTER TO EXIT")
    elif number == 2:
        createPage()
        running = True
    elif number == 3:
        exitPage() 

except Exception as e:
    print(f"Error {e}")

    