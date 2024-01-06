#! python3
# findLargeFiles.py - Walks through a given folder tree adn searches
# for files larger than the indicated size and then prints their absolute path

import sys, os

def findLargeFiles(folder: str, size: int) -> None:
    '''
    Prints to stdout all the files in the <folder> tree
    that are equal or greater than <size> bytes.
    '''
    folder = os.path.abspath(folder)
    if not os.path.exists(folder):
        print(f"Folder {folder} doesn't exist!")
        return

    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            file = os.path.join(foldername, filename)
            if os.path.getsize(file) >= size:
                print(file)


if len(sys.argv) < 3:
    print('''Usage: findLargeFiles.py <folder> <size>
    Where:  <folder> folder whose tree to be searched
            <size> the minimum file size in bytes for files to be reported.
    ''')
    sys.exit()

findLargeFiles(sys.argv[1], int(sys.argv[2]))
