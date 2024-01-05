#! python3
# regexSearch.py - Opens all .txt files in the current folder and searches for
# any line that matches a user-supplied regular expression.

from pathlib import Path
import re

print('Please input regular expression:')
regEx = re.compile(input())

# Search for all .txt files in the current directory:
for filePath in Path.cwd().glob('*.txt'):
    file = open(filePath, 'r')
    print(filePath.name)
    print('-' * len(filePath.name))
    # For each file go line by line and try to match the regex.
    while textLine := file.readline():
        if regEx.search(textLine):
            print(textLine)

