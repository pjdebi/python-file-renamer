Run the application using `python main.py`. When in the same directory as the file. Python 3.9.6 used.

Provide a full path the directory containing files you want to rename. Enter the season of the series ex: 1, 3, 10, 23. You will be shown what the values will update from and to.

A sample run is provided below
```
(main)$ python main.py 
What directory do you want to rename files in? (Please use the full path): /Users/pjd/Documents/Projects/coding/python/dbz-renamer/test
What season is this? 1
Found 5 files to rename
{'test - 011 - file.txt': 'test - S01E01 - file.txt',
 'test - 100 - file.txt': 'test - S01E02 - file.txt'}

These values are the old values with the new values. Would you like to continue? (y or n) y
renaming test - 100 - file.txt to test - S01E02 - file.txt
renaming test - 011 - file.txt to test - S01E01 - file.txt
```