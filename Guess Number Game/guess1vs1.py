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

# Import desired variable from close proximity files
# Let the user choose a difficulty level

print("\nChoose a difficulty level: \n")
print("1.Easy Level: 14 rounds\n")
print("2.Normal Level: 7 rounds\n")
print("3.Hard Level: 5 rounds\n")
print("4.God Level: 3 rounds\n")

    # Verify user input for difficulty level
def gameLevel():
    gameDifficulty = input("Enter the difficulty level you prefer: ")
    if gameDifficulty == "1":
        mainCallEasy()
    elif gameDifficulty == "2":
        mainCallNormal()
    elif gameDifficulty == "3":
        mainCallHard()
    elif gameDifficulty == "4":
        mainCallGod()
    else:
        UserName = open("playername.txt", "r")
        readUserName = UserName.readline()
        print("Enter a correct difficulty level,", readUserName)
        UserName.close()
        gameDifficulty = input("Enter the difficulty level you prefer: ")


        # Counter for new rounds.
def main():
    global counter
    counter = 1

    # Get the guess for all difficulty levels
def getGuess():
    global number
    number = int(input("Enter the number to be guessed: "))
    if (number > 100 or number < 100):
        print("Invalid number, try again")
        getGuess()

    # Set new rounds
def newRoundEasy():
    if counter <= 14:
        print(" Round", counter, "of 14")
        print(" ------------------------")
    else:
        print(" The number was", number, "\n")
        playAgain()


def newRoundNormal():
    if counter <= 7:
        print(" Round", counter, "of 7")
        print(" ------------------------")
    else:
        print(" The number was", number, "\n")
        playAgain()

def newRoundHard():
    if counter <= 5:
        print(" Round", counter, "of 5")
        print(" ------------------------")
    else:
        print(" The number was", number, "\n")
        playAgain()

def newRoundGod():
    if counter <= 3:
        print(" Round", counter, "of 3")
        print(" ------------------------")
    else:
        print(" The number was", number, "\n")
        playAgain()

        # Validate and evaluate input for every round
def guessWinEasy(number, guess):
    if (guess < 1 or guess > 100):
        print("Incorrect number. Try again")
        guessWin2Easy()
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
    elif guess == number:
        print("Congratulations, you guessed the mistery number")
        playAgain()

def guessWinNormal(number, guess):
    if (guess < 1 or guess > 100):
        print("Incorrect number. Try again")
        guessWin2Normal()
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
    elif guess == number:
        print("Congratulations, you guessed the mistery number")
        playAgain()

def guessWinHard(number, guess):
    if (guess < 1 or guess > 100):
        print("Incorrect number. Try again")
        guessWin2Hard()
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
    elif guess == number:
        print("Congratulations, you guessed the mistery number")
        playAgain()

def guessWinGod(number, guess):
    if (guess < 1 or guess > 100):
        print("Incorrect number. Try again")
        guessWin2God()
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
    elif guess == number:
        print("Congratulations, you guessed the mistery number")
        playAgain()

        # Evaluate input for new rounds after the first
def guessWin2Easy():
    guess = int(input(" Enter your guess (1-100): "))
    guessWinEasy(number, guess)

def guessWin2Normal():
    guess = int(input(" Enter your guess (1-100): "))
    guessWinNormal(number, guess)

def guessWin2Hard():
    guess = int(input(" Enter your guess (1-100): "))
    guessWinHard(number, guess)

def guessWin2God():
    guess = int(input(" Enter your guess (1-100): "))
    guessWinGod(number, guess)


def playAgain():
    again = input(" Do you want to keep playing y/n: ")
    if again == "y":
        print("\n")
        gameLevel()
    elif again == "n":
        quit()

        # Main calls for every difficulty level.
def mainCallEasy():
    main()
    getGuess()
    newRoundEasy()
    guess = int(input(" Enter your guess (1-100): "))
    guessWinEasy(number, guess)


def mainCallNormal():
    main()
    getGuess()
    newRoundNormal()
    guess = int(input(" Enter your guess (1-100): "))
    guessWinNormal(number, guess)


def mainCallHard():
    main()
    getGuess()
    newRoundHard()
    guess = int(input(" Enter your guess (1-100): "))
    guessWinHard(number, guess)


def mainCallGod():
    main()
    getGuess()
    newRoundGod()
    guess = int(input(" Enter your guess (1-100): "))
    guessWinNormal(number, guess)

    # Let the user choose difficulty level.
gameLevel()
