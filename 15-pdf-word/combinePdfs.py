#! python3
# combinePdfs.py - Combine all the PDFs in the current working directory into a single PDF.
# Limitations: currently works with PyPDF2 1.26.0

import PyPDF2, os, sys

if len(sys.argv) < 2:
    print('Usage: combinePdfs.py mergedFile')
    sys.exit()

# Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF files.
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # Loop through all the pages (except the first) and add them.
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# Save the resulting PDF to a file.
pdfOutput = open(sys.argv[1], 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
