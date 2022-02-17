# Filename: videorank.py
# Author: Daniel Hernandez
# Date: December 17th 2021
# Program description: User enter various and their amount of views, show the total amount of
# views and a ranking from most to least watched videos.


# Welcome user


print("Welcome to the video ranking calculator")


# Ask the user for the number of videos


def GetVideos():
    title_views = {}
    rankNumber = []
    rankholder = 0
    totalViews = 0
    videoNumber = int(input("How many videos do you want to analyze? "))
    for video in range(1, videoNumber + 1):
        title = input("Enter the name of the video " + str(video) + " ")
        views = int(input("Enter the number of views for video " + str(video) + " "))
        totalViews += views
        rankholder += 1
        rankNumber.append(rankholder)
        title_views[title] = views

    ranking = dict(sorted(title_views.items(), key=lambda x: x[1], reverse=True))
    avgViews = totalViews / videoNumber
    print("\n The total amount of views is ", totalViews)
    print(" The average amount of views is", int(avgViews))
    print(" Video ranking:")
    for rank, (key,value) in zip(rankNumber, ranking.items()):
        print(" " + str(rank) + ". " + key + " ---> " + str(value), "views")




GetVideos()
