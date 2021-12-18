# Filename: videorank.py
# Author: Daniel Hernandez
# Date: December 17th 2021
# Program description: User enter various and their amount of views, show the total amount of 
# views and a ranking from most to least watched videos.

# Welcome user


print("Welcome to the video ranking calculator")

# Ask the user for the number of videos


def GetVideos():
    global videotitle
    global videorank
    global videoNumber
    global totalViews
    global videocounter
    totalViews = 0
    videorank = []
    videotitle = []
    videoNumber = int(input("How many videos do you want to analyze? "))
    for video in range(1, videoNumber + 1):
        title = input("Enter the name of the video " + str(video) + " ")
        videotitle.append(title)
        views = int(input("Enter the number of views for video " + str(video) + " "))
        videorank.append(views)
        totalViews += views


def showResults():
    import itertools
    global totalViews
    global videorank
    avgViews = totalViews / videoNumber
    print("The total amount of views is ", sum(videorank))
    print("The average amount of views is", avgViews)
    videorank.reverse()
    print("Video raking:")
    for (number, title, video) in itertools.zip_longest(range(1, videoNumber + 1), videotitle, videorank):
        print(number, title, video, "views")

GetVideos()
showResults()
        
