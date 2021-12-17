def mainMenu():
    print(" Welcome to the guess mistery number game.")
    playerName = input("    Enter you name: ")
    userNameFile = open("playername.txt", "w")
    userNameFile.write(playerName)
    userNameFile.close()
    print("\n   Choose a game mode,", playerName)
    print("\n   ---Game Modes---    \n")
    print("    1. You vs AI")
    print("    2. You vs other player")
    print("    4. Players battle vs AI")
    print("    4. Players vs each other")
    gameMode = input("\n    Which game mode you prefer to play today?? ")
    import runpy
    if gameMode == "1":
        runpy.run_module('guessNumber', run_name='__main__')
    elif gameMode == "2":
        runpy.run_module('guess1vs1', run_name='__main__')
    elif gameMode == "3":
        runpy.run_module('guessBattleVsAI', run_name='__main__')
    elif gameMode == "4":
        runpy.run_module('guessBattle1on1', run_name='__main__')
    else:
        print("Enter a correct level please...\n")
        gameMode = input("Which game mode you prefer to play today?? ")




mainMenu()
