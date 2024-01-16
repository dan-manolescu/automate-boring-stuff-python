#! python3
# pdfWatermark.py - Add a watermark on all or only specific page of a PDF.
# Usage: py pdfWatermark.py sourcePdf watermarkPdf {pageNo}

import PyPDF2, sys, os

def watermarkPdf(sourcePdf, watermarkPdf, *pages):
    sourceFile = open(sourcePdf, 'rb')
    sourcePdfReader = PyPDF2.PdfFileReader(sourceFile)
    pdfWriter = PyPDF2.PdfFileWriter()

    if sourcePdfReader.isEncrypted:
        print('Source PDF is password-protected. Please enter password:')
        passwd = input()
        if not pdfReader.decrypt(passwd):
            print('Invalid password. Aborting...')
            return
        pdfWriter.encrypt(passwd)

    pdfWatermarkReader = PyPDF2.PdfFileReader(open(watermarkPdf, 'rb'))
    pageWatermark = pdfWatermarkReader.getPage(0)

    if pages != None:
        pages = [int(page) for page in pages]

    for pageNum in range(sourcePdfReader.numPages):
        pageObj = sourcePdfReader.getPage(pageNum)
        if not pages or pageNum in pages:
            pageObj.mergePage(pageWatermark)
        pdfWriter.addPage(pageObj)


    resultPdfFile = open('watermarked' + os.path.basename(sourcePdf), 'wb')
    pdfWriter.write(resultPdfFile)
    sourceFile.close()
    resultPdfFile.close()

if len(sys.argv) < 3:
    print(f'Usage: {sys.argv[0]} sourcePdf watermarkPdf [pageNo1 pageNo2 pageNo3...]')
    sys.exit()

if len(sys.argv) > 3:
    watermarkPdf(sys.argv[1], sys.argv[2], *sys.argv[3:])
else:
    watermarkPdf(sys.argv[1], sys.argv[2])
