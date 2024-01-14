#! python3
# multiplicationTable.py - Take a number N from the command line and creates
# a NxN multiplication table in an Excel spreadsheet.
# Usage: py multiplicationTable.py <excel_file> <N>
# Example: py multiplicationTable.py example.xlsx 6

import openpyxl, sys
from openpyxl.styles import Font

def multiplicationTable(spreadsheetFile: str, n: int) -> None:
    '''
    Saves a spreadsheet file with a nxn multiplication table.
    '''
    wb = openpyxl.Workbook()
    sheet = wb.active
    for row in range(n + 1):
        for col in range(n + 1):
            cell = sheet.cell(row=row+1, column=col+1)
            if row == 0 or col == 0:
                boldFont = Font(bold=True)
                cell.font = boldFont
                if col > 0:
                    cell.value = col
                if row > 0:
                    cell.value = row
            else:
                cell.value = row * col

    wb.save(spreadsheetFile)


if len(sys.argv) < 3:
    print('Usage: multiplicationTable.py <excel_file> <N>')
    sys.exit()

multiplicationTable(sys.argv[1], int(sys.argv[2]))

