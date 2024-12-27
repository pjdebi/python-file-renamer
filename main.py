import os
import sys
import pprint

# /Users/pjd/Documents/Projects/coding/python/python-show-renamer/test

pp = pprint.PrettyPrinter()

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        try:
            os.chdir(self.newPath)
        except FileNotFoundError:
            print("Directory not found!")

    def __exit__(self, etype, value, traceback):
        try:
            os.chdir(self.savedPath)
        except FileNotFoundError:
            print("Directory not found!")

def confirmUserInput(question):
    while True:
        try:
            userInput = str(input(question + " "))
            if userInput == "y":
                break
            elif userInput == "n":
                print("Select 'n'. Exiting application")
                sys.exit()
        except ValueError:
            print("Please enter y or n")
            continue
        else:
            break

def main():
    directory, season = getDirectoryAndSeason()

    with cd(directory):
        files = os.listdir()
        episodeNumbersList = getEpisodes(files)

        seasonAndEpisodes = getSeasonAndEpisodesDictionary(season, episodeNumbersList)

        newFilesNames = getNewFileNames(files, seasonAndEpisodes)
        
        pp.pprint(newFilesNames)
        confirmUserInput("These values are the old values with the new values. Would you like to continue? (y or n)")
        
        renameFiles(newFilesNames)

def renameFiles(newFilesNames):
    for key, value in newFilesNames.items():
        print("renaming {} to {}".format(key, value))
        os.rename(key, value)

def getNewFileNames(files, seasonAndEpisodes):
    newFilesNames = {}

    for idx, filename in enumerate(files):
        for se in seasonAndEpisodes:
            if se in filename:
                newFileName = filename.replace(se, seasonAndEpisodes[se])
                newFilesNames[filename] = newFileName
    return newFilesNames

def getSeasonAndEpisodesDictionary(season, episodeNumbersList):
    seasonAndEpisodes = {}

    for idx, number in enumerate(episodeNumbersList):
        idx = idx + 1
        if idx < 10:
            episode = "0{}".format(idx)
        else:
            episode = "{}".format(idx)
        seasonAndEpisodes[number] = "S{}E{}".format(season, episode)
    return seasonAndEpisodes

def getEpisodes(files):
    numbers = []
    for f in files:
        if os.path.isfile(f):
            filename = os.path.splitext(f)[0]
            filename = filename.split()
            for name in filename:
                if name.isdigit():
                    numbers.append(name)
    print("Found {} files to rename".format(len(numbers)))
    numbers.sort()
    return numbers

def getDirectoryAndSeason():
    directory = input("What directory do you want to rename files in? (Please use the full path): ")
    while True:
        try:
            season = int(input("What season is this? "))
        except ValueError:
            print("Enter a valid number")
            continue
        else:
            break

    if season < 10:
        season = "0{}".format(season)
    else:
        season = "{}".format(season)
    return directory, season   
            
main()