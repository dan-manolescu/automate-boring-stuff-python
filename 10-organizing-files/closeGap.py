#! python3
# closeGap.py - Identifies gaps in the file numbering
# and closes the gap by renaming later files.
# TODO: sorted will not work if the counter has different digit number between files.

import sys, shutil, re
from pathlib import Path

def closeGap(folder: str, prefix: str) -> None:
    p = Path(folder)
    if not p.exists():
        print("Folder doesn't exist!")
        return

    regex = re.compile(f'^({prefix})(\\d+)(.*)$')

    counter = 1
    for file in sorted(p.glob(prefix + '*.*')):
        mo = regex.search(file.stem)
        if mo == None:
            continue
        if int(mo.group(2)) > counter:
            # We found a gap, start renaming
            newFile = file.parent / (prefix + str(counter).rjust(len(mo.group(2)), '0') + file.suffix)
            print(f'Found gap, renaming {file.name} to {newFile.name}')
            shutil.move(file, newFile)
        counter += 1

if len(sys.argv) < 3:
    print('''Usage: closeGap.py <folder> <prefix>
    Where <folder> is the folder to search for files in
          <prefix> is the prefix of the file.
    Assumes filenames are <prefix><counter>.extension
    ''')
    sys.exit()

closeGap(sys.argv[1], sys.argv[2])
