#! python3
# splitPdf.py - Splits the given PDF into multiple PDF files for every page.
# Pattern for page splitting - original file name + "_" + xxxx counter
# Limitations: currently only tested with PyPDF2 3.0.1 (does not work with 1.x versions)

import PyPDF2, sys
from pathlib import Path

if len(sys.argv) < 2:
    print('Usage: %s pdfFileToSplit' % (sys.argv[0]))
    sys.exit()

p = Path(sys.argv[1])
if not p.exists():
    print('No such pdf file found %s' % (sys.argv[1]))
    sys.exit()

pdfFileObj = open(sys.argv[1], 'rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)

# Loop through all the pages and generate a new pdf for each page
for pageNum in range(len(pdfReader.pages)):
    pageObj = pdfReader.pages[pageNum]
    pdfWriter = PyPDF2.PdfWriter()
    pdfWriter.add_page(pageObj)
    pdfSplitFileName = f'{p.stem}_{(pageNum+1):04d}.pdf'
    pdfOutputFileObj = open(pdfSplitFileName, 'wb')
    pdfWriter.write(pdfOutputFileObj)
    pdfOutputFileObj.close()
    print(f'Split page {pageNum+1} out of {len(pdfReader.pages)} into file {pdfSplitFileName}')

print('All done!')
