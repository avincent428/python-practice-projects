# Ask user if they want to generate a password or not
# if yes, ask for password length
# generate password
# print the password
# if initial response is no, exit program

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$$%^&*()")

def generate_password():
    password_length = int(input("How long would you like your password to be? "))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)

option = input("Do you want to generate a password? (Y/N)")

if option == "y":
    generate_password()
elif option == "n":
    print("Program ended")
    quit()
else:
    print("Invalid input, please try again")
    quit()