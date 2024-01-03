#! python3
# regexStrip.py - Regex version of the strip() method.

import re

def regexStrip(text: str, stripChar: str=' ') -> str:
    '''
    Strips the supplied text of the leading and trailing
    specified stripChar characters (by default whitespaces).
    Returns the stripped text.
    '''
    regexStr = re.compile(f'(^[{stripChar}]*)|([{stripChar}]*$)')
    return regexStr.sub('', text)

print('Please input text for stripping:')
text = input()
print('Please enter character to strip:')
strip = input()[0]

print(f'Stripped version is: {regexStrip(text, strip)}')

