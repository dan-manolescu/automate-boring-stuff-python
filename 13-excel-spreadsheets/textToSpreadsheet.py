#! python3
# textToSpreadsheet.py - Read the contents of several text files and insert the contents
# into a spreadsheet, one line of text per row, each file into one column.
# Usage: py textToSpreadsheet.py [spreadsheet] [file1] [file2] ... [fileN]

import openpyxl, sys, os

def textToSpreadsheet(spreadsheet, *argv):
    wb = openpyxl.Workbook()
    sheet = wb.active

    for i in range(len(argv)):
        if not os.path.exists(argv[i]):
            print(f'File {argv[i]} doesn\' exist. Skipping it...')
            continue  # Skip the file if it doesn't exist

        print(f'Copying text from file {argv[i]} to workbook column {i+1}')
        file = open(argv[i], 'r')
        row = 1
        while line := file.readline():
            sheet.cell(row=row, column=i+1).value = line
            row += 1
        file.close()

    print(f'Saving workbook to {spreadsheet}')
    wb.save(spreadsheet)


if len(sys.argv) < 3:
    print(f'Usage: py {sys.argv[0]} [spreadsheet] [file1] [file2] ... [fileN]')
    sys.exit()

textToSpreadsheet(sys.argv[1], *sys.argv[2:])
