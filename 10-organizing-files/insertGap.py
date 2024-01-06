#! python3
# insertGap.py - Inserts a gap into a series of numbered files so that a new file can be added.
# TODO: sorted will not work if the counter has different digit number between files.

import sys, shutil, re
from pathlib import Path

def insertGap(folder: str, prefix: str, gap: int) -> None:
    p = Path(folder)
    if not p.exists():
        print("Folder doesn't exist!")
        return

    # Check if the file with the gap exists; if it doesn't no action needed.
    isGap = False
    for file in p.glob(f'{prefix}*{gap}.*'):
        isGap = True
    if not isGap:
        print('No gap exists! Exiting!')
        return

    regex = re.compile(f'^({prefix})(\\d+)(.*)$')

    for file in sorted(p.glob(prefix + '*.*'), reverse=True):
        mo = regex.search(file.stem)
        if mo == None:
            continue
        counter = int(mo.group(2))
        if counter >= gap:
            # We just need to increment by 1.
            newFile = file.parent / f'{prefix}{str(counter + 1).rjust(len(mo.group(2)), "0")}{file.suffix}'
            print(f'Renaming {file.name} to {newFile.name}')
            shutil.move(file, newFile)
        else:
            # We are beyond the gap, no need to continue.
            break

if len(sys.argv) < 4:
    print('''Usage: closeGap.py <folder> <prefix> <gap>
    Where <folder> is the folder to search for files in
          <prefix> is the prefix of the file.
          <gap> is the counter value where we want the gap to occur.
    Assumes filenames are <prefix><counter>.extension.
    ''')
    sys.exit()

insertGap(sys.argv[1], sys.argv[2], int(sys.argv[3]))
