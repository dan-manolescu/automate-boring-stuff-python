#! python3
# dateDetection.py - Detect dates in the DD/MM/YYYY format.

import re

def isValidDate(day, month, year):
    '''
    day is an integer representing the number of a day in the month.
    month is an integer representing the number of a month in a year.
    year is an integer representing the year number.
    The output is a boolean indicating if the date represented bye
    day, month and year is a valid date.
    '''
    if day < 1 or day > 31:
        return False
    if month < 1 or month > 12:
        return False
    if year < 1000 or year > 2999:
        return False
    # April, June, September and November have 30 days.
    if month in (4, 6, 9, 11) and day == 31:
        return False

    isLeapYear = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

    # February has 28 days unless it's a leap year where it has 29 days.
    if month == 2:
        if not isLeapYear and day > 28:
            return False
        elif day > 29:
            return False

    return True


dateRegex = re.compile(r'^(\d{1,2})/(\d{1,2})/(\d{4})$')

print('Please enter a date in format DD/MM/YYYY or q to quit')
while (date := input()) != 'q':
    match = dateRegex.search(date)
    if match:
        day, month, year = match.groups()
        if isValidDate(int(day), int(month), int(year)):
            print('Valid date')
            continue
    print('Not a valid date')


