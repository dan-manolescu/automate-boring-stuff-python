#! python3
# pdfDecrypt.py - Decrypts all PDFs found in the given folder (and its subfolders) using the provided password.
# Limitations: currently works with PyPDF2 1.26.0

import PyPDF2, sys, os

def pdfDecrypt(folder: str, password: str) -> None:
    '''
    Decrypts all encrypted PDF files found in the given folder
    and its subfolders using the given password.
    If a file cannot be decrypted it's skipped.
    Decrypted files are saved with the suffix "_decrypted".
    '''
    absFolderPath = os.path.abspath(folder)
    for folderName, subfolders, filenames in os.walk(absFolderPath):
        print('Looking into folder', folderName, '...')
        for filename in filenames:
            if filename.lower().endswith('.pdf'):
                # If the file is a pdf then read it and decrypt it with the password
                filePath = os.path.join(folderName, filename)
                print('Processing PDF file', filename)
                pdfFile = open(filePath, 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFile)

                # Check if the original PDF is not encrypted and if it isn't then skip it.
                if not pdfReader.isEncrypted:
                    print('PDF is not encrypted. Skipping it!')
                    continue
                elif pdfReader.decrypt(password) == 0:
                    print('Invalid password for this PDF. Skipping it!')
                    continue

                pdfWriter = PyPDF2.PdfFileWriter()
                for pageNum in range(pdfReader.numPages):
                    pdfWriter.addPage(pdfReader.getPage(pageNum))

                decFileName = filename[:-4] + '_decrypted.pdf'
                decPdfPath = os.path.join(folderName, decFileName)
                print('Saving decrypted version as', decFileName)
                decPdf = open(decPdfPath, 'wb')
                pdfWriter.write(decPdf)
                pdfFile.close()
                decPdf.close()


if len(sys.argv) < 3:
    print(f'Usage: {sys.argv[0]} folder password')
    sys.exit()

pdfDecrypt(sys.argv[1], sys.argv[2])
