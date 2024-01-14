#! python3
# findMistake.py - Find mistakes in the spreadsheet at https://docs.google.com/spreadsheets/d/1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg/edit?usp=sharing/

import ezsheets

ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
sheet = ss[0]

for i in range(2, sheet.rowCount + 1):
    row = sheet.getRow(i)
    if not row[0] or not row[1] or not row[2]:
        continue
    actualTotal = int(row[0]) * int(row[1])
    total = int(row[2])
    if actualTotal != total:
        print('Row %s has the wrong total %s instead of %s' % (i, total, actualTotal))



