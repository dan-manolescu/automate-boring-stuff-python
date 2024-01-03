#! python3
# strongPassDetect.py - Strong Password Detection program.

import re

def isPasswordStrong(password: str) -> bool:
    '''
    Verifies if the string password is a strong password
    according to the following criteria:
    * is at least eight characters long
    * contains both uppercase and lowercase characters
    * has at least one digit

    Returns true if the password is strong, false otherwise.
    '''
    passRegex = re.compile(r'''(
        ^               # match must occur at the beginning of the string
        (?=.*[A-Z])     # must have at least one uppercase letter
        (?=.*[a-z])     # must have at least one lowercase letter
        (?=.*[0-9])     # must have at least one digit
        .{8,}           # minimum of 8 characters long
        $               # together with ^ indicates that entire string must match
        )''', re.VERBOSE)

    return (passRegex.search(password) != None)

    '''
    # One other option is to use multiple simpler regexes like below and just check them.
    # This has the advantage of making the code easier to maintain.
    passLenRegex = re.compile(r'^[a-zA-Z0-9]{8,}$')
    passLoRegex = re.compile(r'[a-z]+')
    passHiRegex = re.compile(r'[A-Z]+')
    passDiRegex = re.compile(r'[0-9]+')

    return passLenRegex.search(password) and \
            passLoRegex.search(password) and \
            passHiRegex.search(password) and \
            passDiRegex.search(password)
            '''

print('Please enter your password:')
password = input()
if isPasswordStrong(password):
    print('Strong password')
else:
    print('Weak password')
