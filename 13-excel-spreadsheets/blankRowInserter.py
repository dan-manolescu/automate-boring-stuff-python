#! python3
# blankRowInserter.py - Starting at row N it inserts M blank rows into the spreadsheet.
# Usage: py blankRowInserter.py N M spreadsheet
# Example: Py blankRowInserter.py 3 2 mySpreadsheet.xlsx

import openpyxl, sys, os

def insertBlankRow(n: int, m: int, spreadsheet: str) -> None:
    '''
    Starting with row n it inserts m blank rows into the spreadsheet.
    '''
    wb = openpyxl.load_workbook(spreadsheet)
    sheet = wb.active
    sheet.insert_rows(n, m)
    wb.save(spreadsheet)


if len(sys.argv) < 4:
    print(f'Usage: {sys.argv[0]} N M spreadsheet')
    sys.exit()

if not os.path.exists(sys.argv[3]):
    print('Invalid spreadsheet file!')
    sys.exit()

insertBlankRow(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3])


