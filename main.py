import os
import pprint

# /Users/pjd/Documents/Projects/coding/python/dbz-renamer/test

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
            userInput = str(input(question))
            if userInput == "y":
                continue
            elif userInput == "n":
                print("Select 'n'. Exiting")
                exit
        except ValueError:
            print("Please enter y or n")
            continue
        else:
            break

def main():
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

    with cd(directory):
        files = os.listdir()
        numbers = []
        for f in files:
            if os.path.isfile(f):
                filename = f.split()
                for name in filename:
                    if name.isdigit():
                        numbers.append(name)
        numbers.sort()

        seasonAndEpisodes = {}

        for idx, number in enumerate(numbers):
            idx = idx + 1
            if idx < 10:
                episode = "0{}".format(idx)
            else:
                episode = "{}".format(idx)
            seasonAndEpisodes[number] = "S{}E{}".format(season, episode)

        pp.pprint(seasonAndEpisodes)
        confirmUserInput("These values are the old values with the new values. Would you like to continue? (y or n)")

        for idx, filename in enumerate(files):
            for se in seasonAndEpisodes:
                if se in filename:
                    newFileName = filename.replace(se, seasonAndEpisodes[se])
                    os.rename(filename, newFileName)
main()