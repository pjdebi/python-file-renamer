# Usage
Rename TV Shows to follow the Plex season and episode formatting. A file called 'Show 001 Awesome Episode' will be updated to 'Show S01E01 Awesome Episode' if the season entered was 1. This allows for bulk renaming of files within a specified directory.

Anime shows typically follow this format
```
/Show
    /Season 1
        Episode 1
        Episode 2
    /Season 2
        Episode 3
        Episode 4
```
This program will update to the following. When provided w/the relevant paths to each season.
```
/Show
    /Season 1
        S01E01
        S01E02
    /Season 2
        S02E01
        S02E02
```

## How to Run
Run the application using `python main.py`. When in the same directory as the file. Python 3.9.6 used.

## Example
A sample run is provided below
```
(main)$ python main.py 
What directory do you want to rename files in? (Please use the full path): /Users/pjd/Documents/Projects/coding/python/python-show-renamer/test
What season is this? 1
Found 2 files to rename
{'test - 011 - file.txt': 'test - S01E01 - file.txt',
 'test - 100 - file.txt': 'test - S01E02 - file.txt'}

These values are the old values with the new values. Would you like to continue? (y or n) y
renaming test - 100 - file.txt to test - S01E02 - file.txt
renaming test - 011 - file.txt to test - S01E01 - file.txt
```

## TODO
- [ ] allow renaming all episodes when separated into season folders