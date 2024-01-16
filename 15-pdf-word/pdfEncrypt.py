#! python3
# pdfEncrypt.py - Encrypt all PDF's in a given folder (and its subfolders).
# Usage: py pdfEncrypt.py folder password
# Limitations: currently works with PyPDF2 1.26.0

import PyPDF2, sys, os

def pdfEncrypt(folder: str, password: str) -> None:
    '''
    Finds all PDF files in the folder (and its subfolders)
    and encrypts them using the given password.
    All files are saved with the _encrypted suffix.
    '''
    absFolder = os.path.abspath(folder)
    for folderName, subfolders, filenames in os.walk(absFolder):
        print('Looking into folder', folderName, '...')
        for filename in filenames:
            if filename.lower().endswith('.pdf'):
                # If the file is a pdf then read it and encrypt it with the password
                filePath = os.path.join(folderName, filename)
                print('Processing PDF file', filename)
                pdfFile = open(filePath, 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFile)

                # Check if the original PDF is encrypted and if it is then skip it.
                if pdfReader.isEncrypted:
                    print('PDF is already encrypted. Skipping it!')
                    continue

                pdfWriter = PyPDF2.PdfFileWriter()
                for pageNum in range(pdfReader.numPages):
                    pdfWriter.addPage(pdfReader.getPage(pageNum))

                pdfWriter.encrypt(password)
                encFileName = filename[:-4] + '_encrypted.pdf'
                encPdfPath = os.path.join(folderName, encFileName)
                print('Saving encrypted version as', encFileName)
                encPdf = open(encPdfPath, 'wb')
                pdfWriter.write(encPdf)
                pdfFile.close()
                encPdf.close()
                # Removes original pdf file.
                print('Deleting original PDF file', filename)
                os.unlink(filePath)


if len(sys.argv) < 3:
    print(f'Usage: {sys.argv[0]} folder password')
    sys.exit()

pdfEncrypt(sys.argv[1], sys.argv[2])
