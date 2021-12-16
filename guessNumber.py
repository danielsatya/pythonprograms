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

print(" Welcome to mystery number guess...  \n")


def main():
    global counter
    counter = 1


def getGuess(first, last):
    import random
    global number
    number = random.randint(first, last)


def newRound():
    if counter <= 7:
        print(" Round", counter, "of 7")
        print(" ------------------------")
    else:
        print(" The number was", number, "\n")
        playAgain()


def guessWin(number, guess):
    if (guess < 1 or guess > 100):
        print("Incorrect number. Try again")
        guessWin2()
    elif guess > number:
        print("--->", guess, "is too high...\n")
        global counter
        counter += 1
        newRound()
        guessWin2()
    elif guess < number:
        print("--->", guess, "is too low...\n")
        counter += 1
        newRound()
        guessWin2()
    elif guess == number:
        print("Congratulations, you guessed the mistery number")
        playAgain()


def guessWin2():
    guess = int(input(" Enter your guess (1-100): "))
    guessWin(number, guess)


def playAgain():
    again = input(" Do you want to keep playing y/n: ")
    if again == "y":
        print("\n")
        mainCall()
    elif again == "n":
        quit()


def mainCall():
    main()
    getGuess(1, 100)
    newRound()
    guess = int(input(" Enter your guess (1-100): "))
    guessWin(number, guess)


mainCall()
