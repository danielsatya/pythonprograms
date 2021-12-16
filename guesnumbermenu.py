def mainMenu():
    print(" Welcome to the guess mistery number game.")
    playerName = input("    Enter you name: ")
    print("Welcome to The Mistery Number Game", playerName)
    print("---Game Modes---")
    print("1. You vs AI")
    print("2. You vs other player")
    print("4. Teams vs AI")
    print("4. Teams vs teams")
    gameMode = input("Which game mode you prefer to play today?? ")
    import runpy
    if gameMode == "1":
        runpy.run_module('guessNumber', run_name='__main__')


mainMenu()
k = input("press close to exit")
