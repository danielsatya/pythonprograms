# Filename: intro.py
# Author: Daniel Hernandez
# Date: December 12th 2021
# Program description: A game which lets you choose a business model and choose the best for your enterprises.


# Welcome the user


print("Welcome to the Youtube Game!")
print("If you already have an account go directly to the login.py file and start the game")

# Let the user enter his/her credentials for all future games


def getName():
    userName = input("What is your name? ")
    if len(userName) > 20:
        print("This name is too long, choose a different one") 
        getName()


def getuserName(): 
    userName = input("Enter your username... ")
    if len(userName) > 20:
        print("Name is too long, make it shorter")
        getuserName()
    userFile = open('username.txt', 'w')
    userFile.write(userName)
    userFile.close()


def getuserPassword(): 
    userPassword = input("Enter your password... ")
    if len(userPassword) > 20:
        print("The password is too long, shorten it")
    digit = False
    for character in userPassword:
        if character.isdigit():
            digit = True
            if digit != True:
                print("Enter at least one digit")
                getuserPassword()
    passwordFile = open('password.txt', 'w')
    passwordFile.write(userPassword)
    passwordFile.close()
    print("Don't forget the username or the password, you will need them later to log in")


def getAge():
    userAge = int(input("How old are you? "))
    if userAge < 18:
        print("You're too young to play this game, sorry")
        quit()
    else:
        startGame()


def startGame():
    import time
    print("Loading...")
    time.sleep(3)
    print("Starting game...")
    import runpy
    runpy.run_module('login', run_name='__main__')
    






getName()
getuserName()
getuserPassword()
getAge()
startGame()
