# Filename: guessNumber.py
# Author: Daniel Hernandez
# Date: November 8th 2021
# Program description: Let the user guess a randomly
#                       created number from 1 to 100 up to 7 rounds.
# Input:
# 1.Player guesses 7 times, a number from 1 to a 100,
#        every round adds 1 to counter variable.
#  2. Exit menu. "n" if player wishes to quit
# or "y" if player wished to play again.
# Processing:
# 1. Welcome the player to the game. For each new round print "round
# (counter variable) out of 7"... If counter is greater than 7,
# print what number random number was and prompt user to enter "y"
# to play again or "n" to quit the game.
# 2.Input validation: If the player enter a number smaller than 2 or
# greater than a hundred, prompt user to enter again.
#  Don't add round to counter as guess was invalid.
# 3. Verify the guess:
# 1. If user enters a number smaller than the random display
# Too Low" message and add integer to counter variable. Prompt for next round.
# 2. If user enters a number greater than the random number,display "Too High"
# message and add integer to counter variable. Prompt for next round.
# 3. If user enters a number equal to the random display
# "Congratulation!  You guess the number" message and
#  prompt user to enter "y" to play again or "n" to quit the game.
# Output: Tell user if input is wrong, if the guess is wrong or congratulate
#   if the user guessed the number. Restart or quit program as user wished to.


    # Welcome the user


print(" Welcome to Battle 1on1 mode")
print(" You can add up to 4 players to play with")


    # Get usernames


def getMainUser():
    getPrimaryUser = open("playername.txt", "r")
    recordUser = getPrimaryUser.readline()
    global userMain
    userMain = recordUser
    getPrimaryUser.close()
    global playerCount
    playerCount = 1


def getName1():
        getUser2 = input("Enter your username (up to 4) ---> ")
        print("Welcome,", getUser2)
        global user2
        user2 = getUser2
        global playerCount
        playerCount += 1


def getName2():
            getUser3 = input("Enter your username (up to 4) ---> ")
            print("Welcome,", getUser3)
            global user3
            user3 = getUser3
            global playerCount
            playerCount += 1

def getName3():
            getUser4 = input("Enter your username (up to 4) ---> ")
            print("Welcome,", getUser4)
            global user4
            user4 = getUser4
            global playerCount
            playerCount += 1
            print("Choose a difficulty level: \n")
            print("1.Normal Level: 14 rounds\n")
            print("2.Normal Level: 7 rounds\n")
            print("3.God Level: 5 rounds\n")
            print("4.God Level: 3 rounds\n")    # Present difficulty levels
            gameLevel()

getMainUser()
getName1()

            # Get guess


def main():
    global counter
    counter = 1


def getGuess():
    global number1
    global number2
    global number3
    global number4
    if playerCount == 2:
        print(userMain, "has to guess", user2, "'s number")
        print(user2, "has to guess", userMain, "'s number")
        number1 = int(input("Enter the number to be guessed " + userMain + ": "))
        if (number1 > 100 or number1 < 0):
            print("Invalid try again")
            getGuess()
        number2 = int(input("Enter the number to be guessed " + user2 + ": "))
        if (number2 > 100 or number2 < 0):
            print("Invalid try again")
            getGuess()
    if playerCount == 3:
        print(userMain, "has to guess", user2, "'s number")
        print(user2, "has to guess", user3, "'s number")
        print(user3, "has to guess", userMain, "'s number")
        number1 = int(input("Enter the number to be guessed " + userMain + ": "))
        if (number1 > 100 or number1 < 0):
            print("Invalid try again")
            getGuess()
        number2 = int(input("Enter the number to be guessed " + user2 + ": "))
        if (number2 > 100 or number2 < 0):
            print("Invalid try again")
            getGuess()
        number3 = int(input("Enter the number to be guessed " + user3 + ": "))
        if (number3 > 100 or number3 < 0):
            print("Invalid try again")
            getGuess()
    if playerCount == 4:
        print(userMain, "has to guess", user2, "'s number")
        print(user2, "has to guess", user3, "'s number")
        print(user3, "has to guess", user4, "'s number")
        print(user4, "has to guess", userMain, "'s number")
        number1 = int(input("Enter the number to be guessed " + userMain + ": "))
        if (number1 > 100 or number1 < 0):
            print("Invalid try again")
            getGuess()
        number2 = int(input("Enter the number to be guessed " + user2 + ": "))
        if (number2 > 100 or number2 < 0):
            print("Invalid try again")
            getGuess()
        number3 = int(input("Enter the number to be guessed " + user3 + ": "))
        if (number3 > 100 or number3 < 0):
            print("Invalid try again")
            getGuess()
        number4 = int(input("Enter the number to be guessed " + user4 + ": "))
        if (number4 > 100 or number4 < 0):
            print("Invalid try again")
            getGuess()


    # Add usernames to list

def getTurns():
        global userMaincount
        global user2count
        global user3count
        global user4count
        userMaincount = 0
        user2count = 0
        user3count = 0
        user4count = 0

getTurns()

        # Define rounds with list to create for loop


def newRoundEasy():
        if counter <= 30:
            print(" Round", counter, "of 30")
            print(" ------------------------")
        else:
            if playerCount == 2:
                print(userMain, "number was", number1)
                print(user2, "number was", number2)
            elif playerCount == 3:
                print(userMain, "number was", number1)
                print(user2, "number was", number2)
                print(user3, "number was", number3)
            elif playerCount == 4:
                print(userMain, "number was", number1)
                print(user2, "number was", number2)
                print(user3, "number was", number3)
                print(user4, "number was", number4)


def newRoundNormal():
            if counter <= 24:
                print(" Round", counter, "of 24")
                print(" ------------------------")
            else:
                if playerCount == 2:
                    print(userMain, "number was", number1)
                    print(user2, "number was", number2)
                elif playerCount == 3:
                    print(userMain, "number was", number1)
                    print(user2, "number was", number2)
                    print(user3, "number was", number3)
                elif playerCount == 4:
                    print(userMain, "number was", number1)
                    print(user2, "number was", number2)
                    print(user3, "number was", number3)
                    print(user4, "number was", number4)


def newRoundHard():
            if counter <= 18:
                print(" Round", counter, "of 18")
                print(" ------------------------")
            else:
                if playerCount == 2:
                    print(userMain, "number was", number1)
                    print(user2, "number was", number2)
                elif playerCount == 3:
                    print(userMain, "number was", number1)
                    print(user2, "number was", number2)
                    print(user3, "number was", number3)
                elif playerCount == 4:
                    print(userMain, "number was", number1)
                    print(user2, "number was", number2)
                    print(user3, "number was", number3)
                    print(user4, "number was", number4)


def newRoundGod():
            if counter <= 12:
                print(" Round", counter, "of 12")
                print(" ------------------------")
            else:
                if playerCount == 2:
                    print(userMain, "number was", number1)
                    print(user2, "number was", number2)
                elif playerCount == 3:
                    print(userMain, "number was", number1)
                    print(user2, "number was", number2)
                    print(user3, "number was", number3)
                elif playerCount == 4:
                    print(userMain, "number was", number1)
                    print(user2, "number was", number2)
                    print(user3, "number was", number3)
                    print(user4, "number was", number4)


    # Validate and evaluate input for every the next round


def guessWinEasy(guess):
        global userMaincount
        global user2count
        global user3count
        global user4count
        if playerCount == 2:
            if (guess == number2 and userMaincount > user2count):
                print("Congratulations, you guessed the mistery number,", userMain)
                playAgain()
            elif (guess == number1 and user2count == userMaincount):
                print("Congratulations, you guessed the mistery number,", user2)
                playAgain()
        elif playerCount == 3:
            if (guess == number2 and userMaincount > user3count):
                print("Congratulations, you guessed the mistery number,", userMain)
                playAgain()
            elif (guess == number3 and user2count == userMaincount and user2count > user3count):
                print("Congratulations, you guessed the mistery number,", user2)
                playAgain()
            elif (guess == number1 and user3count == user2count):
                print("Congratulations, you guessed the mistery number,", user3)
                playAgain()
        elif playerCount == 4:
            if (guess == number2 and userMaincount > user4count):
                print("Congratulations, you guessed the mistery number,", userMain)
                playAgain()
            elif (guess == number3 and user2count == userMaincount and user2count > user3count):
                print("Congratulations, you guessed the mistery number,", user2)
                playAgain()
            elif (guess == number4 and user3count == user2count and user2count > user3count):
                print("Congratulations, you guessed the mistery number,", user3)
                playAgain()
            elif (guess == number1 and user4count == user3count):
                print("Congratulations, you guessed the mistery number,", user4)
                playAgain()



def guessWinNormal(guess):
        global userMaincount
        global user2count
        global user3count
        global user4count
        if playerCount == 2:
            if (guess == number2 and userMaincount > user2count):
                print("Congratulations, you guessed the mistery number,", userMain)
                playAgain()
            elif (guess == number1 and user2count == userMaincount):
                print("Congratulations, you guessed the mistery number,", user2)
                playAgain()
        elif playerCount == 3:
            if (guess == number2 and userMaincount > user3count):
                print("Congratulations, you guessed the mistery number,", userMain)
                playAgain()
            elif (guess == number3 and user2count == userMaincount and user2count > user3count):
                print("Congratulations, you guessed the mistery number,", user2)
                playAgain()
            elif (guess == number1 and user3count == user2count):
                print("Congratulations, you guessed the mistery number,", user3)
                playAgain()
        elif playerCount == 4:
            if (guess == number2 and userMaincount > user4count):
                print("Congratulations, you guessed the mistery number,", userMain)
                playAgain()
            elif (guess == number3 and user2count == userMaincount and user2count > user3count):
                print("Congratulations, you guessed the mistery number,", user2)
                playAgain()
            elif (guess == number4 and user3count == user2count and user2count > user3count):
                print("Congratulations, you guessed the mistery number,", user3)
                playAgain()
            elif (guess == number1 and user4count == user3count):
                print("Congratulations, you guessed the mistery number,", user4)
                playAgain()


def guessWinHard(guess):
        global userMaincount
        global user2count
        global user3count
        global user4count
        if playerCount == 2:
            if (guess == number2 and userMaincount > user2count):
                print("Congratulations, you guessed the mistery number,", userMain)
                playAgain()
            elif (guess == number1 and user2count == userMaincount):
                print("Congratulations, you guessed the mistery number,", user2)
                playAgain()
        elif playerCount == 3:
            if (guess == number2 and userMaincount > user3count):
                print("Congratulations, you guessed the mistery number,", userMain)
                playAgain()
            elif (guess == number3 and user2count == userMaincount and user2count > user3count):
                print("Congratulations, you guessed the mistery number,", user2)
                playAgain()
            elif (guess == number1 and user3count == user2count):
                print("Congratulations, you guessed the mistery number,", user3)
                playAgain()
        elif playerCount == 4:
            print(userMain, "has to guess", user2, "'s number")
            if (guess == number2 and userMaincount > user4count):
                print("Congratulations, you guessed the mistery number,", userMain)
                playAgain()
            elif (guess == number3 and user2count == userMaincount and user2count > user3count):
                print("Congratulations, you guessed the mistery number,", user2)
                playAgain()
            elif (guess == number4 and user3count == user2count and user2count > user3count):
                print("Congratulations, you guessed the mistery number,", user3)
                playAgain()
            elif (guess == number1 and user4count == user3count):
                print("Congratulations, you guessed the mistery number,", user4)
                playAgain()

def guessWinGod(guess):
        global userMaincount
        global user2count
        global user3count
        global user4count
        if playerCount == 2:
            if (guess == number2 and userMaincount > user2count):
                print("Congratulations, you guessed the mistery number,", userMain)
                playAgain()
            elif (guess == number1 and user2count == userMaincount):
                print("Congratulations, you guessed the mistery number,", user2)
                playAgain()
        elif playerCount == 3:
            if (guess == number2 and userMaincount > user3count):
                print("Congratulations, you guessed the mistery number,", userMain)
                playAgain()
            elif (guess == number3 and user2count == userMaincount and user2count > user3count):
                print("Congratulations, you guessed the mistery number,", user2)
                playAgain()
            elif (guess == number1 and user3count == user2count):
                print("Congratulations, you guessed the mistery number,", user3)
                playAgain()
        elif playerCount == 4:
            if (guess == number2 and userMaincount > user4count):
                print("Congratulations, you guessed the mistery number,", userMain)
                playAgain()
            elif (guess == number3 and user2count == userMaincount and user2count > user3count):
                print("Congratulations, you guessed the mistery number,", user2)
                playAgain()
            elif (guess == number4 and user3count == user2count and user2count > user3count):
                print("Congratulations, you guessed the mistery number,", user3)
                playAgain()
            elif (guess == number1 and user4count == user3count):
                print("Congratulations, you guessed the mistery number,", user4)
                playAgain()


    # Get turns for every player and input after the first one then verify by selection control


def guessWin2Easy():
    global userMaincount
    global user2count
    global user3count
    global user4count
    global counter
    global number1
    global number2
    global number3
    global number4
    if playerCount == 2:
        if userMaincount == user2count + 1:
            print("It's you turn", user2)
            guess = int(input(" Enter your guess (J1-100): "))
            if (guess < 1 or guess > 100):
                print("Incorrect number. Try again")
                guessWin2Easy()
            elif guess > number1:
                print("--->", guess, "is too high...\n")
                counter += 1
                user2count += 1
                newRoundEasy()
                guessWin2Easy()
            elif guess < number1:
                print("--->", guess, "is too low...\n")
                counter += 1
                user2count += 1
                newRoundEasy()
                guessWin2Easy()
            else:
                guessWinEasy(guess)
        elif userMaincount == user2count:
            print("It's your turn", userMain)
            guess = int(input(" Enter your guess (1-100): "))
            if (guess < 1 or guess > 100):
                print("Incorrect number. Try again")
                guessWinEasy()
            elif guess > number1:
                print("--->", guess, "is too high...\n")
                counter += 1
                userMaincount += 1
                newRoundEasy()
                guessWin2Easy()
            elif guess < number1:
                print("--->", guess, "is too low...\n")
                counter += 1
                userMaincount += 1
                newRoundEasy()
                guessWin2Easy()
            else:
                guessWinEasy(guess)
    elif playerCount == 3:
        if userMaincount == user2count + 1:
            print("It's you turn", user2)
            guess = int(input(" Enter your guess (1-100): "))
            if (guess < 1 or guess > 100):
                print("Incorrect number. Try again")
                guessWinEasy()
            elif guess > number3:
                print("--->", guess, "is too high...\n")
                counter += 1
                user2count += 1
                newRoundEasy()
                guessWin2Easy()
            elif guess < number3:
                print("--->", guess, "is too low...\n")
                counter += 1
                user2count += 1
                newRoundEasy()
                guessWin2Easy()
            else:
                guessWinEasy(guess)
        elif userMaincount == user3count + 1:
            print("It's you turn", user3)
            guess = int(input(" Enter your guess (1-100): "))
            if (guess < 1 or guess > 100):
                print("Incorrect number. Try again")
                guessWinEasy()
            elif guess > number1:
                print("--->", guess, "is too high...\n")
                counter += 1
                user3count += 1
                newRoundEasy()
                guessWin2Easy()
            elif guess < number1:
                print("--->", guess, "is too low...\n")
                counter += 1
                user3count += 1
                newRoundEasy()
                guessWin2Easy()
            else:
                guessWinEasy(guess)
        elif userMaincount == user3count:
            print("It's your turn", userMain)
            guess = int(input(" Enter your guess (1-100): "))
            if (guess < 1 or guess > 100):
                print("Incorrect number. Try again")
                guessWinEasy()
            elif guess > number2:
                print("--->", guess, "is too high...\n")
                counter += 1
                userMaincount += 1
                newRoundEasy()
                guessWin2Easy()
            elif guess < number2:
                print("--->", guess, "is too low...\n")
                counter += 1
                userMaincount += 1
                newRoundEasy()
                guessWin2Easy()
            else:
                guessWinEasy(guess)
    elif playerCount == 4:
        if userMaincount == user2count + 1:
            print("It's you turn", user2)
            guess = int(input(" Enter your guess (1-100): "))
            if (guess < 1 or guess > 100):
                print("Incorrect number. Try again")
                guessWinEasy()
            elif guess > number3:
                print("--->", guess, "is too high...\n")
                counter += 1
                user2count += 1
                newRoundEasy()
                guessWin2Easy()
            elif guess < number3:
                print("--->", guess, "is too low...\n")
                counter += 1
                user2count += 1
                newRoundEasy()
                guessWin2Easy()
            else:
                guessWinEasy(guess)
        elif userMaincount == user3count + 1:
            print("It's you turn", user3)
            guess = int(input(" Enter your guess (1-100): "))
            if (guess < 1 or guess > 100):
                print("Incorrect number. Try again")
                guessWinEasy()
            elif guess > number4:
                print("--->", guess, "is too high...\n")
                counter += 1
                user3count += 1
                newRoundEasy()
                guessWin2Easy()
            elif guess < number4:
                print("--->", guess, "is too low...\n")
                counter += 1
                user3count += 1
                newRoundEasy()
                guessWin2Easy()
            else:
                guessWinEasy(guess)
        elif userMaincount == user4count + 1:
            print("It's you turn", user4)
            guess = int(input(" Enter your guess (1-100): "))
            if (guess < 1 or guess > 100):
                print("Incorrect number. Try again")
                guessWinEasy()
            elif guess > number1:
                print("--->", guess, "is too high...\n")
                counter += 1
                user4count += 1
                newRoundEasy()
                guessWin2Easy()
            elif guess < number1:
                print("--->", guess, "is too low...\n")
                counter += 1
                user4count += 1
                newRoundEasy()
                guessWin2Easy()
            else:
                guessWinEasy(guess)
        elif userMaincount == user4count:
            print("It's your turn", userMain)
            guess = int(input(" Enter your guess (1-100): "))
            if (guess < 1 or guess > 100):
                print("Incorrect number. Try again")
                guessWinEasy()
            elif guess > number2:
                print("--->", guess, "is too high...\n")
                counter += 1
                userMaincount += 1
                newRoundEasy()
                guessWin2Easy()
            elif guess < number2:
                print("--->", guess, "is too low...\n")
                counter += 1
                userMaincount += 1
                newRoundEasy()
                guessWin2Easy()
            else:
                guessWinEasy(guess)


def guessWin2Normal():
        global userMaincount
        global user2count
        global user3count
        global user4count
        global counter
        if playerCount == 2:
            if userMaincount == user2count + 1:
                print("It's you turn", user2)
                guess = int(input(" Enter your guess (1-100): "))
                if (guess < 1 or guess > 100):
                    print("Incorrect number. Try again")
                    guessWin2Normal()
                elif guess > number1:
                    print("--->", guess, "is too high...\n")
                    counter += 1
                    user2count += 1
                    newRoundNormal()
                    guessWin2Normal()
                elif guess < number1:
                    print("--->", guess, "is too low...\n")
                    counter += 1
                    user2count += 1
                    newRoundNormal()
                    guessWin2Normal()
                else:
                    guessWinNormal(guess)
            elif userMaincount == user2count:
                print("It's your turn", userMain)
                guess = int(input(" Enter your guess (1-100): "))
                if (guess < 1 or guess > 100):
                    print("Incorrect number. Try again")
                    guessWinNormal()
                elif guess > number1:
                    print("--->", guess, "is too high...\n")
                    counter += 1
                    userMaincount += 1
                    newRoundNormal()
                    guessWin2Normal()
                elif guess < number1:
                    print("--->", guess, "is too low...\n")
                    counter += 1
                    userMaincount += 1
                    newRoundNormal()
                    guessWin2Normal()
                else:
                    guessWinNormal(guess)
        elif playerCount == 3:
            if userMaincount == user2count + 1:
                print("It's you turn", user2)
                guess = int(input(" Enter your guess (1-100): "))
                if (guess < 1 or guess > 100):
                    print("Incorrect number. Try again")
                    guessWinNormal()
                elif guess > number3:
                    print("--->", guess, "is too high...\n")
                    counter += 1
                    user2count += 1
                    newRoundNormal()
                    guessWin2Normal()
                elif guess < number3:
                    print("--->", guess, "is too low...\n")
                    counter += 1
                    user2count += 1
                    newRoundNormal()
                    guessWin2Normal()
                else:
                    guessWinNormal(guess)
            elif userMaincount == user3count + 1:
                print("It's you turn", user3)
                guess = int(input(" Enter your guess (1-100): "))
                if (guess < 1 or guess > 100):
                    print("Incorrect number. Try again")
                    guessWinNormal()
                elif guess > number1:
                    print("--->", guess, "is too high...\n")
                    counter += 1
                    user3count += 1
                    newRoundNormal()
                    guessWin2Normal()
                elif guess < number1:
                    print("--->", guess, "is too low...\n")
                    counter += 1
                    user3count += 1
                    newRoundNormal()
                    guessWin2Normal()
                else:
                    guessWinNormal(guess)
            elif userMaincount == user3count:
                print("It's your turn", userMain)
                guess = int(input(" Enter your guess (1-100): "))
                if (guess < 1 or guess > 100):
                    print("Incorrect number. Try again")
                    guessWinNormal()
                elif guess > number2:
                    print("--->", guess, "is too high...\n")
                    counter += 1
                    userMaincount += 1
                    newRoundNormal()
                    guessWin2Normal()
                elif guess < number2:
                    print("--->", guess, "is too low...\n")
                    counter += 1
                    userMaincount += 1
                    newRoundNormal()
                    guessWin2Normal()
                else:
                    guessWinNormal(guess)
        elif playerCount == 4:
            if userMaincount == user2count + 1:
                print("It's you turn", user2)
                guess = int(input(" Enter your guess (1-100): "))
                if (guess < 1 or guess > 100):
                    print("Incorrect number. Try again")
                    guessWinNormal()
                elif guess > number3:
                    print("--->", guess, "is too high...\n")
                    counter += 1
                    user2count += 1
                    newRoundNormal()
                    guessWin2Normal()
                elif guess < number3:
                    print("--->", guess, "is too low...\n")
                    counter += 1
                    user2count += 1
                    newRoundNormal()
                    guessWin2Normal()
                else:
                    guessWinNormal(guess)
            elif userMaincount == user3count + 1:
                print("It's you turn", user3)
                guess = int(input(" Enter your guess (1-100): "))
                if (guess < 1 or guess > 100):
                    print("Incorrect number. Try again")
                    guessWinNormal()
                elif guess > number4:
                    print("--->", guess, "is too high...\n")
                    counter += 1
                    user3count += 1
                    newRoundNormal()
                    guessWin2Normal()
                elif guess < number4:
                    print("--->", guess, "is too low...\n")
                    counter += 1
                    user3count += 1
                    newRoundNormal()
                    guessWin2Normal()
                else:
                    guessWinNormal(guess)
            elif userMaincount == user4count + 1:
                print("It's you turn", user4)
                guess = int(input(" Enter your guess (1-100): "))
                if (guess < 1 or guess > 100):
                    print("Incorrect number. Try again")
                    guessWinNormal()
                elif guess > number1:
                    print("--->", guess, "is too high...\n")
                    counter += 1
                    user4count += 1
                    newRoundNormal()
                    guessWin2Normal()
                elif guess < number1:
                    print("--->", guess, "is too low...\n")
                    counter += 1
                    user4count += 1
                    newRoundNormal()
                    guessWin2Normal()
                else:
                    guessWinNormal(guess)
            elif userMaincount == user4count:
                print("It's your turn", userMain)
                guess = int(input(" Enter your guess (1-100): "))
                if (guess < 1 or guess > 100):
                    print("Incorrect number. Try again")
                    guessWinNormal()
                elif guess > number2:
                    print("--->", guess, "is too high...\n")
                    counter += 1
                    userMaincount += 1
                    newRoundNormal()
                    guessWin2Normal()
                elif guess < number2:
                    print("--->", guess, "is too low...\n")
                    counter += 1
                    userMaincount += 1
                    newRoundNormal()
                    guessWin2Normal()
                else:
                    guessWinNormal(guess)


def guessWin2Hard():
        global userMaincount
        global user2count
        global user3count
        global user4count
        global counter
        if playerCount == 2:
            if userMaincount == user2count + 1:
                print("It's you turn", user2)
                guess = int(input(" Enter your guess (1-100): "))
                if (guess < 1 or guess > 100):
                    print("Incorrect number. Try again")
                    guessWin2Hard()
                elif guess > number1:
                    print("--->", guess, "is too high...\n")
                    counter += 1
                    user2count += 1
                    newRoundHard()
                    guessWin2Hard()
                elif guess < number1:
                    print("--->", guess, "is too low...\n")
                    counter += 1
                    user2count += 1
                    newRoundHard()
                    guessWin2Hard()
                else:
                    guessWinHard(guess)
            elif userMaincount == user2count:
                print("It's your turn", userMain)
                guess = int(input(" Enter your guess (1-100): "))
                if (guess < 1 or guess > 100):
                    print("Incorrect number. Try again")
                    guessWinHard()
                elif guess > number1:
                    print("--->", guess, "is too high...\n")
                    counter += 1
                    userMaincount += 1
                    newRoundHard()
                    guessWin2Hard()
                elif guess < number1:
                    print("--->", guess, "is too low...\n")
                    counter += 1
                    userMaincount += 1
                    newRoundHard()
                    guessWin2Hard()
                else:
                    guessWinHard(guess)
        elif playerCount == 3:
            if userMaincount == user2count + 1:
                print("It's you turn", user2)
                guess = int(input(" Enter your guess (1-100): "))
                if (guess < 1 or guess > 100):
                    print("Incorrect number. Try again")
                    guessWinHard()
                elif guess > number3:
                    print("--->", guess, "is too high...\n")
                    counter += 1
                    user2count += 1
                    newRoundHard()
                    guessWin2Hard()
                elif guess < number3:
                    print("--->", guess, "is too low...\n")
                    counter += 1
                    user2count += 1
                    newRoundHard()
                    guessWin2Hard()
                else:
                    guessWinHard(guess)
            elif userMaincount == user3count + 1:
                print("It's you turn", user3)
                guess = int(input(" Enter your guess (1-100): "))
                if (guess < 1 or guess > 100):
                    print("Incorrect number. Try again")
                    guessWinHard()
                elif guess > number1:
                    print("--->", guess, "is too high...\n")
                    counter += 1
                    user3count += 1
                    newRoundHard()
                    guessWin2Hard()
                elif guess < number1:
                    print("--->", guess, "is too low...\n")
                    counter += 1
                    user3count += 1
                    newRoundHard()
                    guessWin2Hard()
                else:
                    guessWinHard(guess)
            elif userMaincount == user3count:
                print("It's your turn", userMain)
                guess = int(input(" Enter your guess (1-100): "))
                if (guess < 1 or guess > 100):
                    print("Incorrect number. Try again")
                    guessWinHard()
                elif guess > number2:
                    print("--->", guess, "is too high...\n")
                    counter += 1
                    userMaincount += 1
                    newRoundHard()
                    guessWin2Hard()
                elif guess < number2:
                    print("--->", guess, "is too low...\n")
                    counter += 1
                    userMaincount += 1
                    newRoundHard()
                    guessWin2Hard()
                else:
                    guessWinHard(guess)
        elif playerCount == 4:
            if userMaincount == user2count + 1:
                print("It's you turn", user2)
                guess = int(input(" Enter your guess (1-100): "))
                if (guess < 1 or guess > 100):
                    print("Incorrect number. Try again")
                    guessWinHard()
                elif guess > number3:
                    print("--->", guess, "is too high...\n")
                    counter += 1
                    user2count += 1
                    newRoundHard()
                    guessWin2Hard()
                elif guess < number3:
                    print("--->", guess, "is too low...\n")
                    counter += 1
                    user2count += 1
                    newRoundHard()
                    guessWin2Hard()
                else:
                    guessWinHard(guess)
            elif userMaincount == user3count + 1:
                print("It's you turn", user3)
                guess = int(input(" Enter your guess (1-100): "))
                if (guess < 1 or guess > 100):
                    print("Incorrect number. Try again")
                    guessWinHard()
                elif guess > number4:
                    print("--->", guess, "is too high...\n")
                    counter += 1
                    user3count += 1
                    newRoundHard()
                    guessWin2Hard()
                elif guess < number4:
                    print("--->", guess, "is too low...\n")
                    counter += 1
                    user3count += 1
                    newRoundHard()
                    guessWin2Hard()
                else:
                    guessWinHard(guess)
            elif userMaincount == user4count + 1:
                print("It's you turn", user4)
                guess = int(input(" Enter your guess (1-100): "))
                if (guess < 1 or guess > 100):
                    print("Incorrect number. Try again")
                    guessWinHard()
                elif guess > number1:
                    print("--->", guess, "is too high...\n")
                    counter += 1
                    user4count += 1
                    newRoundHard()
                    guessWin2Hard()
                elif guess < number1:
                    print("--->", guess, "is too low...\n")
                    counter += 1
                    user4count += 1
                    newRoundHard()
                    guessWin2Hard()
                else:
                    guessWinHard(guess)
            elif userMaincount == user4count:
                print("It's your turn", userMain)
                guess = int(input(" Enter your guess (1-100): "))
                if (guess < 1 or guess > 100):
                    print("Incorrect number. Try again")
                    guessWinHard()
                elif guess > number2:
                    print("--->", guess, "is too high...\n")
                    counter += 1
                    userMaincount += 1
                    newRoundHard()
                    guessWin2Hard()
                elif guess < number2:
                    print("--->", guess, "is too low...\n")
                    counter += 1
                    userMaincount += 1
                    newRoundHard()
                    guessWin2Hard()
                else:
                    guessWinHard(guess)


def guessWin2God():
            global userMaincount
            global user2count
            global user3count
            global user4count
            global counter
            if playerCount == 2:
                if userMaincount == user2count + 1:
                    print("It's you turn", user2)
                    guess = int(input(" Enter your guess (1-100): "))
                    if (guess < 1 or guess > 100):
                        print("Incorrenumber. Try again")
                        guessWin2God()
                    elif guess > number1:
                        print("--->", guess, "is too high...\n")
                        counter += 1
                        user2count += 1
                        newRoundGod()
                        guessWin2God()
                    elif guess < number1:
                        print("--->", guess, "is too low...\n")
                        counter += 1
                        user2count += 1
                        newRoundGod()
                        guessWin2God()
                    else:
                        guessWinGod(guess)
                elif userMaincount == user2count:
                    print("It's your turn", userMain)
                    guess = int(input(" Enter your guess (1-100): "))
                    if (guess < 1 or guess > 100):
                        print("Incorrect number. Try again")
                        guessWinGod()
                    elif guess > number1:
                        print("--->", guess, "is too high...\n")
                        counter += 1
                        userMaincount += 1
                        newRoundGod()
                        guessWin2God()
                    elif guess < number1:
                        print("--->", guess, "is too low...\n")
                        counter += 1
                        userMaincount += 1
                        newRoundGod()
                        guessWin2God()
                    else:
                        guessWinGod(guess)
            elif playerCount == 3:
                if userMaincount == user2count + 1:
                    print("It's you turn", user2)
                    guess = int(input(" Enter your guess (1-100): "))
                    if (guess < 1 or guess > 100):
                        print("Incorrect number. Try again")
                        guessWinGod()
                    elif guess > number3:
                        print("--->", guess, "is too high...\n")
                        counter += 1
                        user2count += 1
                        newRoundGod()
                        guessWin2God()
                    elif guess < number3:
                        print("--->", guess, "is too low...\n")
                        counter += 1
                        user2count += 1
                        newRoundGod()
                        guessWin2God()
                    else:
                        guessWinGod(guess)
                elif userMaincount == user3count + 1:
                    print("It's you turn", user3)
                    guess = int(input(" Enter your guess (1-100): "))
                    if (guess < 1 or guess > 100):
                        print("Incorrect number. Try again")
                        guessWinGod()
                    elif guess > number1:
                        print("--->", guess, "is too high...\n")
                        counter += 1
                        user3count += 1
                        newRoundGod()
                        guessWin2God()
                    elif guess < number1:
                        print("--->", guess, "is too low...\n")
                        counter += 1
                        user3count += 1
                        newRoundGod()
                        guessWin2God()
                    else:
                        guessWinGod(guess)
                elif userMaincount == user3count:
                    print("It's your turn", userMain)
                    guess = int(input(" Enter your guess (1-100): "))
                    if (guess < 1 or guess > 100):
                        print("Incorrect number. Try again")
                        guessWinGod()
                    elif guess > number2:
                        print("--->", guess, "is too high...\n")
                        counter += 1
                        userMaincount += 1
                        newRoundGod()
                        guessWin2God()
                    elif guess < number2:
                        print("--->", guess, "is too low...\n")
                        counter += 1
                        userMaincount += 1
                        newRoundGod()
                        guessWin2God()
                    else:
                        guessWinGod(guess)
            elif playerCount == 4:
                if userMaincount == user2count + 1:
                    print("It's you turn", user2)
                    guess = int(input(" Enter your guess (1-100): "))
                    if (guess < 1 or guess > 100):
                        print("Incorrect number. Try again")
                        guessWinGod()
                    elif guess > number3:
                        print("--->", guess, "is too high...\n")
                        counter += 1
                        user2count += 1
                        newRoundGod()
                        guessWin2God()
                    elif guess < number3:
                        print("--->", guess, "is too low...\n")
                        counter += 1
                        user2count += 1
                        newRoundGod()
                        guessWin2God()
                    else:
                        guessWinGod(guess)
                elif userMaincount == user3count + 1:
                    print("It's you turn", user3)
                    guess = int(input(" Enter your guess (1-100): "))
                    if (guess < 1 or guess > 100):
                        print("Incorrect number. Try again")
                        guessWinGod()
                    elif guess > number4:
                        print("--->", guess, "is too high...\n")
                        counter += 1
                        user3count += 1
                        newRoundGod()
                        guessWin2God()
                    elif guess < number4:
                        print("--->", guess, "is too low...\n")
                        counter += 1
                        user3count += 1
                        newRoundGod()
                        guessWin2God()
                    else:
                        guessWinGod(guess)
                elif userMaincount == user4count + 1:
                    print("It's you turn", user4)
                    guess = int(input(" Enter your guess (1-100): "))
                    if (guess < 1 or guess > 100):
                        print("Incorrect number. Try again")
                        guessWinGod()
                    elif guess > number1:
                        print("--->", guess, "is too high...\n")
                        counter += 1
                        user4count += 1
                        newRoundGod()
                        guessWin2God()
                    elif guess < number1:
                        print("--->", guess, "is too low...\n")
                        counter += 1
                        user4count += 1
                        newRoundGod()
                        guessWin2God()
                    else:
                        guessWinGod(guess)
                elif userMaincount == user4count:
                    print("It's your turn", userMain)
                    guess = int(input(" Enter your guess (1-100): "))
                    if (guess < 1 or guess > 100):
                        print("Incorrect number. Try again")
                        guessWinGod()
                    elif guess > number2:
                        print("--->", guess, "is too high...\n")
                        counter += 1
                        userMaincount += 1
                        newRoundGod()
                        guessWin2God()
                    elif guess < number2:
                        print("--->", guess, "is too low...\n")
                        counter += 1
                        userMaincount += 1
                        newRoundGod()
                        guessWin2God()
                    else:
                        guessWinGod(guess)


    # Lets user play again


def playAgain():
    again = input(" Do you want to keep playing y/n: ")
    if again == "y":
        print("\n")
        import runpy
        runpy.run_module('guessBattle1on1')


    elif again == "n":
        quit()


        # Call main functions for game


def mainCallEasy():
    main()
    getGuess()
    newRoundEasy()
    guessWin2Easy()


def mainCallNormal():
    main()
    getGuess()
    newRoundNormal()
    guessWin2Normal()


def mainCallHard():
    main()
    getGuess()
    newRoundHard()
    guessWin2Hard()


def mainCallGod():
    main()
    getGuess()
    newRoundGod()
    guessWin2God()


    # Let the user choose a difficulty level


def gameLevel():
    gameDifficulty = int(input("Enter the difficulty level you prefer: "))
    if gameDifficulty == 1:
        mainCallEasy()
    elif gameDifficulty == 2:
        mainCallNormal()
    elif gameDifficulty == 3:
        mainCallHard()
    elif gameDifficulty == 4:
        mainCallGod()
    else:
        UserName = open("playername.txt", "r")
        readUserName = UserName.readline()
        print("Enter a correct difficulty level,", readUserName)
        UserName.close()
        gameLevel()


        # Functions to let user add more than one player


def getAnother():
        anotherUser = input("Do you want to add another player? ")
        if anotherUser == "y":
            getName2()
        elif anotherUser == "n":
            print("Choose a difficulty level: \n")
            print("1.Normal Level: 14 rounds\n")
            print("2.Normal Level: 7 rounds\n")
            print("3.God Level: 5 rounds\n")
            print("4.God Level: 3 rounds\n")
            gameLevel()  # Present difficulty levels

def getAnother2():
        anotherUser = input("Do you want to add another player? ")
        if anotherUser == "y":
            getName3()
        elif anotherUser == "n":
            print("Choose a difficulty level: \n")
            print("1.Normal Level: 14 rounds\n")
            print("2.Normal Level: 7 rounds\n")
            print("3.God Level: 5 rounds\n")
            print("4.God Level: 3 rounds\n")    # Present difficulty levels
            gameLevel()

getAnother()
getAnother2()
