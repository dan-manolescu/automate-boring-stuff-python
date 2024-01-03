#! python3
# idiot.py - How to keep an idiot busy for hours: simple project for pyinputplus module.
# Requires the pyinputplus module to be installed. Use "pip install --user pyinputplus".

import pyinputplus as pyip

while True:
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    response = pyip.inputYesNo(prompt)

    if response == 'no':
        break

print('Thank you. Have a nice day.')

