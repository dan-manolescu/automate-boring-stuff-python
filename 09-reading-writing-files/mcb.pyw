#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe mcb.pyw delete <keyword> - Deletes keyword from the shelf.
#        py.exe mcb.pyw delete-all - Deletes all keywords from the shelf.

import shelve, pyperclip, sys

if len(sys.argv) < 2:
    print('''
    Usage:  py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
            py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
            py.exe mcb.pyw list - Loads all keywords to clipboard.
            py.exe mcb.pyw delete <keyword> - Deletes keyword from the shelf.
            py.exe mcb.pyw delete-all - Deletes all keywords from the shelf.''')
    sys.exit()

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        # Save clipboard content.
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete' and sys.argv[2] in mcbShelf:
        # Delete key from shelf if it exists
        del mcbShelf[sys.argv[2]]

elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'delete-all':
        mcbShelf.clear()
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
