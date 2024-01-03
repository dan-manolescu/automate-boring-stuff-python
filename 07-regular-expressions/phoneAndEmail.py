#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

# Create regex for phone numbers
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''', re.VERBOSE)

# Create regex for email addresses
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   # username
    @                   # @ symbol
    [a-zA-Z0-9.-]+      # domain name
    (\.[a-zA-Z]{2,4})   # dot-something
    )''', re.VERBOSE)

# Create regex for website URLs that begin with http:// or https://.
urlRegex = re.compile(r'''(
    http(s)?://
    (.*)\n
    )''', re.VERBOSE)

# Create regex for dates in different formats.
dateRegex = re.compile(r'''(
    (\d{1,2}|\d{4})     # month or year
    (/|-|\.)            # separator
    (\d{1,2})           # day or month
    (/|-|\.)            # separator
    (\d{4}|\d{1,2})     # year or day
    )''', re.VERBOSE)

# Create regex for SSN.
ssnRegex = re.compile(r'\d{3}-\d{2}-\d{4}')

# Create regex for CC numbers.
ccRegex = re.compile(r'\d{4}\s{1}\d{4}\s{1}\d{4}\s{1}\d{4}')

# Find matches in clipboard text.
text = str(pyperclip.paste())

# Remove sensitive information such as SSN or CC numbers
text = ssnRegex.sub('***-**-****', text)
text = ccRegex.sub('**** **** **** ****', text)

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[6] != '':
        phoneNum += ' x' + groups[6]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

for groups in urlRegex.findall(text):
    matches.append(groups[0])

for groups in dateRegex.findall(text):
    if len(groups[1]) == 4:  # We start with the year.
        matches.append('-'.join([groups[1], groups[2].rjust(2, '0'), groups[3].rjust(2, '0')]))
    else:
        matches.append('-'.join([groups[3], groups[1].rjust(2, '0'), groups[2].rjust(2, '0')]))

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
