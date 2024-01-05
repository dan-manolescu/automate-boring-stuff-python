#! python3
# madLibs.py - Reads a text file and lets the user add their own text anywhere
# the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
# Usage: py.exe madLibs.py <inputfile> <outputfile>
# where <inputfile> is the file opened for reading
# and <outputfile> is the file where the updated text will be saved.

import sys, re

if len(sys.argv) < 3:
    print('Usage: py.exe madLibs.py <inputfile> <outputfile>')
    sys.exit()

inputFile = open(sys.argv[1], 'r')
outputFile = open(sys.argv[2], 'w')

# Read input text
text = inputFile.read()

# Create a reg expr and find all matches
tokenRegex = re.compile(r'(ADJECTIVE|NOUN|ADVERB|VERB)')
matches = tokenRegex.findall(text)
for match in matches:
    # For each match ask for a replacement word and substitute it.
    print(f'Enter a{'n' if match == 'ADJECTIVE' else ''} {match.lower()}:')
    replacement = input()
    text = tokenRegex.sub(replacement, text, count=1)

print(text)
outputFile.write(text)

inputFile.close()
outputFile.close()
