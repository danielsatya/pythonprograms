# This is the game itself

# Welcome the user to the game 




print("Welcome to the Youtube Game")
print("You will gain more followers as you upload more videos for you audience")


# Let youtuber decide the name for his channel
def channelName():
    global channelName
    channelName = input("Choose a name for you channel...")
   
   # Let user decide username to login later on
def getuserName():
    global userName
    userName = input("Enter the username you will use to log in to your account")
    if len(userName) > 60:
        print("this name is too long, try again")

   

  
    global channelType 
    
    channelType = input("Choose a category for your channel...")
    print("1. Vlogs")
    print("2. Entertainment")
    print("Gameplay")