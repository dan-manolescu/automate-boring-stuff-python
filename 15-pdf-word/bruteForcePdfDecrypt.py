#! python3
# bruteForcePdfDecrypt.py - Brute force a password protected PDF if using a English dictionary word for password.

import PyPDF2, sys, os

def bruteForcePdfDecrypt(pdfFileName: str) -> str:
    if not os.path.exists('dictionary.txt'):
        print('Dictionary file missing!')
        return None

    with open(pdfFileName, 'rb') as pdfFile:
        pdfReader = PyPDF2.PdfFileReader(pdfFile)

        if not pdfReader.isEncrypted:
            print('PDF is not encrypted!')
            return None

        with open('dictionary.txt', 'r') as dictionary:
            while word := dictionary.readline():
                for password in (word, word.upper()):
                    if pdfReader.decrypt(password) == 1:
                        print('Password is', password)
                        return password

    print('Password is not in the dictionary!')
    return None


if len(sys.argv) < 2:
    print(f'Usage: {sys.argv[0]} pdfFile')
    sys.exit()

bruteForcePdfDecrypt(sys.argv[1])
