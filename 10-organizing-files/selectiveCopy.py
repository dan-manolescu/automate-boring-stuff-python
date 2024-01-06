#! python3
# selectiveCopy.py - Walks through a folder tree and searches for
# files with a certain file extension and then copies them to a
# new folder.

import sys, os, shutil
from pathlib import Path

def selectiveCopy(inputFolder: str, outputFolder: str, fileExtension: str) ->None:
    # Make sure we have a proper extension for Path.suffix.
    if len(fileExtension) > 0 and fileExtension[0] != '.':
        fileExtension = '.' + fileExtension

    # Check if input folder exists.
    inputFolder = os.path.abspath(inputFolder)
    if not os.path.exists(inputFolder):
        print("Input folder doesn't exist!")
        return

    # Check if output folder exists and if not create it.
    outputFolder = os.path.abspath(outputFolder)
    if not os.path.exists(outputFolder):
        print("Output folder doesn't exist! Creating ...")
        os.mkdir(outputFolder)

    # Walk through the whole tree and copy each file that matches the suffix.
    counter = 0
    for foldername, subfolders, filenames in os.walk(inputFolder):
        for filename in filenames:
            fileToCopy = os.path.join(foldername, filename)
            if Path(fileToCopy).suffix == fileExtension:
                print(f'Copying file {filename}...')
                shutil.copy(fileToCopy, outputFolder)
                counter += 1

    print(f'Done! {counter} files copied!')


if len(sys.argv) < 4:
    print('''Usage: selectiveCopy.py <inputFolder> <outputFolder> <fileExtension>
    Where:  <inputFolder> - folder whose tree is to be searched for specific files
            <outputFolder> - folder where to copy the files found
            <fileExtension> - the file extension to identify the files to be copied.
    ''')
    sys.exit()

selectiveCopy(sys.argv[1], sys.argv[2], sys.argv[3])


