#! python3
# convertSpreadsheet.py - Upload a xlsx file to Google Sheets and convert it to other formats

import ezsheets, sys, os

if len(sys.argv) < 2:
    print(f'Usage: py {sys.argv[0]} spreadsheet')
    sys.exit()

if not os.path.exists(sys.argv[1]):
    print('Missing spreadsheet file!')
    sys.exit()

print('Uploading spreadsheet...')
ss = ezsheets.upload(sys.argv[1])
print('Converting to CSV...')
ss.downloadAsCSV()
print('Converting to ODS...')
ss.downloadAsODS()
print('Converting to TSV...')
ss.downloadAsTSV()
print('Converting to PDF...')
ss.downloadAsPDF()
print('Converting to HTML...')
ss.downloadAsHTML()
ss.delete(permanent=True)
print('Done!')
