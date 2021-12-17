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
# 1. If user enters a number smaller than the random number, display
# Too Low" message and add integer to counter variable. Prompt for next round.
# 2. If user enters a number greater than the random number,display "Too High"
# message and add integer to counter variable. Prompt for next round.
# 3. If user enters a number equal to the random number, display
# "Congratulation!  You guess the number" message and
#  prompt user to enter "y" to play again or "n" to quit the game.
# Output: Tell user if input is wrong, if the guess is wrong or congratulate
#   if the user guessed the number. Restart or quit program as user wished to.


    # Welcome the user


print(" Welcome to Battle Vs AI mode")
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
            print("1.Easy Level: 14 rounds\n")
            print("2.Normal Level: 7 rounds\n")
            print("3.Hard Level: 5 rounds\n")
            print("4.God Level: 3 rounds\n")    # Present difficulty levels
            gameLevel()

getMainUser()
getName1()

            # Get guess


def main():
    global counter
    counter = 1


def getGuess(first, last):
    import random
    global number
    number = random.randint(first, last)


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
                print(" The number was", number, "\n")
                playAgain()


def newRoundNormal():
            if counter <= 24:
                print(" Round", counter, "of 24")
                print(" ------------------------")
            else:
                print(" The number was", number, "\n")
                playAgain()


def newRoundHard():
            if counter <= 18:
                print(" Round", counter, "of 18")
                print(" ------------------------")
            else:
                print(" The number was", number, "\n")
                playAgain()


def newRoundGod():
            if counter <= 12:
                print(" Round", counter, "of 12")
                print(" ------------------------")
            else:
                print(" The number was", number, "\n")
                playAgain()


    # Validate and evaluate input for every the next round


def guessWinEasy(number, guess):
        global userMaincount
        global user2count
        global user3count
        global user4count
        if (guess < 1 or guess > 100):
            print("Incorrect number. Try again")
            guessWinEasy()
        elif guess > number:
            print("--->", guess, "is too high...\n")
            global counter
            counter += 1
            newRoundEasy()
            guessWin2Easy()
        elif guess < number:
            print("--->", guess, "is too low...\n")
            counter += 1
            newRoundEasy()
            guessWin2Easy()
        if playerCount == 2:
            if (guess == number and userMaincount > user2count):
                print("Congratulations, you guessed the mistery number,", userMain)
                playAgain()
            elif (guess == number and user2count == userMaincount):
                print("Congratulations, you guessed the mistery number,", user2)
                playAgain()
        elif playerCount == 3:
            if (guess == number and userMaincount > user3count):
                print("Congratulations, you guessed the mistery number,", userMain)
                playAgain()
            elif (guess == number and user2count == userMaincount and user2count > user3count):
                print("Congratulations, you guessed the mistery number,", user2)
                playAgain()
            elif (guess == number and user3count == user2count):
                print("Congratulations, you guessed the mistery number,", user3)
                playAgain()
        elif playerCount == 4:
            if (guess == number and userMaincount > user4count):
                print("Congratulations, you guessed the mistery number,", userMain)
                playAgain()
            elif (guess == number and user2count == userMaincount and user2count > user3count):
                print("Congratulations, you guessed the mistery number,", user2)
                playAgain()
            elif (guess == number and user3count == user2count and user2count > user3count):
                print("Congratulations, you guessed the mistery number,", user3)
                playAgain()
            elif (guess == number and user4count == user3count):
                print("Congratulations, you guessed the mistery number,", user4)
                playAgain()



def guessWinNormal(number, guess):
        global userMaincount
        global user2count
        global user3count
        global user4count
        if (guess < 1 or guess > 100):
            print("Incorrect number. Try again")
            guessWinNormal()
        elif guess > number:
            print("--->", guess, "is too high...\n")
            global counter
            counter += 1
            newRoundNormal()
            guessWin2Normal()
        elif guess < number:
            print("--->", guess, "is too low...\n")
            counter += 1
            newRoundNormal()
            guessWin2Normal()
        if playerCount == 2:
            if (guess == number and userMaincount > user2count):
                print("Congratulations, you guessed the mistery number,", userMain)
                playAgain()
            elif (guess == number and user2count == userMaincount):
                print("Congratulations, you guessed the mistery number,", user2)
                playAgain()
        elif playerCount == 3:
            if (guess == number and userMaincount > user3count):
                print("Congratulations, you guessed the mistery number,", userMain)
                playAgain()
            elif (guess == number and user2count == userMaincount and user2count > user3count):
                print("Congratulations, you guessed the mistery number,", user2)
                playAgain()
            elif (guess == number and user3count == user2count):
                print("Congratulations, you guessed the mistery number,", user3)
                playAgain()
        elif playerCount == 4:
            if (guess == number and userMaincount > user4count):
                print("Congratulations, you guessed the mistery number,", userMain)
                playAgain()
            elif (guess == number and user2count == userMaincount and user2count > user3count):
                print("Congratulations, you guessed the mistery number,", user2)
                playAgain()
            elif (guess == number and user3count == user2count and user2count > user3count):
                print("Congratulations, you guessed the mistery number,", user3)
                playAgain()
            elif (guess == number and user4count == user3count):
                print("Congratulations, you guessed the mistery number,", user4)
                playAgain()


def guessWinHard(number, guess):
        global userMaincount
        global user2count
        global user3count
        global user4count
        if (guess < 1 or guess > 100):
            print("Incorrect number. Try again")
            guessWinHard()
        elif guess > number:
            print("--->", guess, "is too high...\n")
            global counter
            counter += 1
            newRoundHard()
            guessWin2Hard()
        elif guess < number:
            print("--->", guess, "is too low...\n")
            counter += 1
            newRoundHard()
            guessWin2Hard()
        if playerCount == 2:
            if (guess == number and userMaincount > user2count):
                print("Congratulations, you guessed the mistery number,", userMain)
                playAgain()
            elif (guess == number and user2count == userMaincount):
                print("Congratulations, you guessed the mistery number,", user2)
                playAgain()
        elif playerCount == 3:
            if (guess == number and userMaincount > user3count):
                print("Congratulations, you guessed the mistery number,", userMain)
                playAgain()
            elif (guess == number and user2count == userMaincount and user2count > user3count):
                print("Congratulations, you guessed the mistery number,", user2)
                playAgain()
            elif (guess == number and user3count == user2count):
                print("Congratulations, you guessed the mistery number,", user3)
                playAgain()
        elif playerCount == 4:
            if (guess == number and userMaincount > user4count):
                print("Congratulations, you guessed the mistery number,", userMain)
                playAgain()
            elif (guess == number and user2count == userMaincount and user2count > user3count):
                print("Congratulations, you guessed the mistery number,", user2)
                playAgain()
            elif (guess == number and user3count == user2count and user2count > user3count):
                print("Congratulations, you guessed the mistery number,", user3)
                playAgain()
            elif (guess == number and user4count == user3count):
                print("Congratulations, you guessed the mistery number,", user4)
                playAgain()

def guessWinGod(number, guess):
        global userMaincount
        global user2count
        global user3count
        global user4count
        if (guess < 1 or guess > 100):
            print("Incorrect number. Try again")
            guessWinGod()
        elif guess > number:
            print("--->", guess, "is too high...\n")
            global counter
            counter += 1
            newRoundGod()
            guessWin2God()
        elif guess < number:
            print("--->", guess, "is too low...\n")
            counter += 1
            newRoundGod()
            guessWin2God()
        if playerCount == 2:
            if (guess == number and userMaincount > user2count):
                print("Congratulations, you guessed the mistery number,", userMain)
                playAgain()
            elif (guess == number and user2count == userMaincount):
                print("Congratulations, you guessed the mistery number,", user2)
                playAgain()
        elif playerCount == 3:
            if (guess == number and userMaincount > user3count):
                print("Congratulations, you guessed the mistery number,", userMain)
                playAgain()
            elif (guess == number and user2count == userMaincount and user2count > user3count):
                print("Congratulations, you guessed the mistery number,", user2)
                playAgain()
            elif (guess == number and user3count == user2count):
                print("Congratulations, you guessed the mistery number,", user3)
                playAgain()
        elif playerCount == 4:
            if (guess == number and userMaincount > user4count):
                print("Congratulations, you guessed the mistery number,", userMain)
                playAgain()
            elif (guess == number and user2count == userMaincount and user2count > user3count):
                print("Congratulations, you guessed the mistery number,", user2)
                playAgain()
            elif (guess == number and user3count == user2count and user2count > user3count):
                print("Congratulations, you guessed the mistery number,", user3)
                playAgain()
            elif (guess == number and user4count == user3count):
                print("Congratulations, you guessed the mistery number,", user4)
                playAgain()


    # Get turns for every player and input after the first one then verify by selection control


def guessWin2Easy():
    global userMaincount
    global user2count
    global user3count
    global user4count
    if playerCount == 2:
        if userMaincount == user2count + 1:
            print("It's you turn", user2)
            guess = int(input(" Enter your guess (1-100): "))
            user2count += 1
            guessWinEasy(number, guess)
        elif userMaincount == user2count:
            print("Enter you guess", userMain, userMaincount)
            guess = int(input(" Enter your guess (1-100): "))
            userMaincount += 1
            guessWinEasy(number, guess)
    elif playerCount == 3:
        if userMaincount == user2count + 1:
            print("It's you turn", user2)
            guess = int(input(" Enter your guess (1-100): "))
            user2count += 1
            print(userMain, user2, user3)
            guessWinEasy(number, guess)
        elif userMaincount == user3count + 1:
            print("It's you turn", user3)
            guess = int(input(" Enter your guess (1-100): "))
            user3count += 1
            print(userMain, user2, user3)
            guessWinEasy(number, guess)
        elif userMaincount == user3count:
            print("It's your turn", userMain)
            guess = int(input(" Enter your guess (1-100): "))
            userMaincount += 1
            print(userMain, user2, user3)
            guessWinEasy(number, guess)
    elif playerCount == 4:
        if userMaincount == user2count + 1:
            print("It's you turn", user2)
            guess = int(input(" Enter your guess (1-100): "))
            user2count += 1
            guessWinEasy(number, guess)
        elif userMaincount == user3count + 1:
            print("It's you turn", user3)
            guess = int(input(" Enter your guess (1-100): "))
            user3count += 1
            guessWinEasy(number, guess)
        elif userMaincount == user4count + 1:
            print("It's you turn", user4)
            guess = int(input(" Enter your guess (1-100): "))
            user4count += 1
            guessWinEasy(number, guess)
        elif userMaincount == user4count:
            print("It's your turn", userMain)
            guess = int(input(" Enter your guess (1-100): "))
            userMaincount += 1
            guessWinEasy(number, guess)


def guessWin2Normal():
        global userMaincount
        global user2count
        global user3count
        global user4count
        if playerCount == 2:
            if userMaincount == user2count + 1:
                print("It's you turn", user2)
                guess = int(input(" Enter your guess (1-100): "))
                user2count += 1
                guessWinNormal(number, guess)
            elif userMaincount == user2count:
                print("Enter you guess", userMain, userMaincount)
                guess = int(input(" Enter your guess (1-100): "))
                userMaincount += 1
                guessWinNormal(number, guess)
        elif playerCount == 3:
            if userMaincount == user2count + 1:
                print("It's you turn", user2)
                guess = int(input(" Enter your guess (1-100): "))
                user2count += 1
                guessWinNormal(number, guess)
            elif userMaincount == user3count + 1:
                print("It's you turn", user3)
                guess = int(input(" Enter your guess (1-100): "))
                user3count += 1
                guessWinNormal(number, guess)
            elif userMaincount == user3count:
                print("It's your turn", userMain)
                guess = int(input(" Enter your guess (1-100): "))
                userMaincount += 1
                guessWinNormal(number, guess)
        elif playerCount == 4:
            if userMaincount == user2count + 1:
                print("It's you turn", user2)
                guess = int(input(" Enter your guess (1-100): "))
                user2count += 1
                guessWinNormal(number, guess)
            elif userMaincount == user3count + 1:
                print("It's you turn", user3)
                guess = int(input(" Enter your guess (1-100): "))
                user3count += 1
                guessWinNormal(number, guess)
            elif userMaincount == user4count + 1:
                print("It's you turn", user4)
                guess = int(input(" Enter your guess (1-100): "))
                user4count += 1
                guessWinNormal(number, guess)
            elif userMaincount == user4count:
                print("It's your turn", userMain)
                guess = int(input(" Enter your guess (1-100): "))
                userMaincount += 1
                guessWinNormal(number, guess)


def guessWin2Hard():
        global userMaincount
        global user2count
        global user3count
        global user4count
        if playerCount == 2:
            if userMaincount == user2count + 1:
                print("It's you turn", user2)
                guess = int(input(" Enter your guess (1-100): "))
                user2count += 1
                guessWinHard(number, guess)
            elif userMaincount == user2count:
                print("Enter you guess", userMain, userMaincount)
                guess = int(input(" Enter your guess (1-100): "))
                userMaincount += 1
                guessWinHard(number, guess)
        elif playerCount == 3:
            if userMaincount == user2count + 1:
                print("It's you turn", user2)
                guess = int(input(" Enter your guess (1-100): "))
                user2count += 1
                guessWinHard(number, guess)
            elif userMaincount == user3count + 1:
                print("It's you turn", user3)
                guess = int(input(" Enter your guess (1-100): "))
                user3count += 1
                guessWinHard(number, guess)
            elif userMaincount == user3count:
                print("It's your turn", userMain)
                guess = int(input(" Enter your guess (1-100): "))
                userMaincount += 1
                guessWinHard(number, guess)
        elif playerCount == 4:
            if userMaincount == user2count + 1:
                print("It's you turn", user2)
                guess = int(input(" Enter your guess (1-100): "))
                user2count += 1
                guessWinHard(number, guess)
            elif userMaincount == user3count + 1:
                print("It's you turn", user3)
                guess = int(input(" Enter your guess (1-100): "))
                user3count += 1
                guessWinHard(number, guess)
            elif userMaincount == user4count + 1:
                print("It's you turn", user4)
                guess = int(input(" Enter your guess (1-100): "))
                user4count += 1
                guessWinHard(number, guess)
            elif userMaincount == user4count:
                print("It's your turn", userMain)
                guess = int(input(" Enter your guess (1-100): "))
                userMaincount += 1
                guessWinHard(number, guess)


def guessWin2God():
        global userMaincount
        global user2count
        global user3count
        global user4count
        if playerCount == 2:
            if userMaincount == user2count + 1:
                print("It's you turn", user2)
                guess = int(input(" Enter your guess (1-100): "))
                user2count += 1
                guessWinGod(number, guess)
            elif userMaincount == user2count:
                print("Enter you guess", userMain, userMaincount)
                guess = int(input(" Enter your guess (1-100): "))
                userMaincount += 1
                guessWinGod(number, guess)
        elif playerCount == 3:
            if userMaincount == user2count + 1:
                print("It's you turn", user2)
                guess = int(input(" Enter your guess (1-100): "))
                user2count += 1
                guessWinGod(number, guess)
            elif userMaincount == user3count + 1:
                print("It's you turn", user3)
                guess = int(input(" Enter your guess (1-100): "))
                user3count += 1
                guessWinGod(number, guess)
            elif userMaincount == user3count:
                print("It's your turn", userMain)
                guess = int(input(" Enter your guess (1-100): "))
                userMaincount += 1
                guessWinGod(number, guess)
        elif playerCount == 4:
            if userMaincount == user2count + 1:
                print("It's you turn", user2)
                guess = int(input(" Enter your guess (1-100): "))
                user2count += 1
                guessWinGod(number, guess)
            elif userMaincount == user3count + 1:
                print("It's you turn", user3)
                guess = int(input(" Enter your guess (1-100): "))
                user3count += 1
                guessWinGod(number, guess)
            elif userMaincount == user4count + 1:
                print("It's you turn", user4)
                guess = int(input(" Enter your guess (1-100): "))
                user4count += 1
                guessWinGod(number, guess)
            elif userMaincount == user4count:
                print("It's your turn", userMain)
                guess = int(input(" Enter your guess (1-100): "))
                userMaincount += 1
                guessWinGod(number, guess)


    # Lets user play again


def playAgain():
    again = input(" Do you want to keep playing y/n: ")
    if again == "y":
        print("\n")
        import runpy
        runpy.run_module('guessBattleVsAI')


    elif again == "n":
        quit()


        # Call main functions for game


def mainCallEasy():
    main()
    getGuess(1, 100)
    newRoundEasy()
    print("Enter you guess", userMain)
    guess = int(input(" Enter your guess (1-100): "))
    global userMaincount
    userMaincount = userMaincount + 1
    guessWinEasy(number, guess)




def mainCallNormal():
    main()
    getGuess(1, 100)
    newRoundNormal()
    print("Enter you guess", userMain)
    guess = int(input(" Enter your guess (1-100): "))
    global userMaincount
    userMaincount = userMaincount + 1
    guessWinNormal(number, guess)


def mainCallHard():
    main()
    getGuess(1, 100)
    newRoundHard()
    print("Enter you guess", userMain)
    guess = int(input(" Enter your guess (1-100): "))
    global userMaincount
    userMaincount = userMaincount + 1
    guessWinHard(number, guess)


def mainCallGod():
    main()
    getGuess(1, 100)
    newRoundGod()
    print("Enter you guess", userMain)
    guess = int(input(" Enter your guess (1-100): "))
    global userMaincount
    userMaincount = userMaincount + 1
    guessWinGod(number, guess)


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
            print("1.Easy Level: 14 rounds\n")
            print("2.Normal Level: 7 rounds\n")
            print("3.Hard Level: 5 rounds\n")
            print("4.God Level: 3 rounds\n")
            gameLevel()  # Present difficulty levels

def getAnother2():
        anotherUser = input("Do you want to add another player? ")
        if anotherUser == "y":
            getName3()
        elif anotherUser == "n":
            print("Choose a difficulty level: \n")
            print("1.Easy Level: 14 rounds\n")
            print("2.Normal Level: 7 rounds\n")
            print("3.Hard Level: 5 rounds\n")
            print("4.God Level: 3 rounds\n")    # Present difficulty levels
            gameLevel()

getAnother()
getAnother2()
