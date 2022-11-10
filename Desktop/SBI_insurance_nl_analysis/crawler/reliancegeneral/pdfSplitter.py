import sys
from pyPDF2 import PdfFileReader,PdfFileWriter
from PyPDF2 import PdfFileWriter, PdfFileReader

def PDFsplit(pdf, splits):
    # creating input pdf file object
    pdfFileObj = open(pdf, 'rb')
      
    # creating pdf reader object
    pdfReader = PdfFileReader(pdfFileObj)
      
    # starting index of first slice
    start = 0
      
    # starting index of last slice
    end = splits[0]
      
      
    for i in range(len(splits)+1):
        print('HI')
        # creating pdf writer object for (i+1)th split
        pdfWriter = PdfFileWriter()
          
        # output pdf file name
        outputpdf = pdf.split('.pdf')[0] + str(i) + '.pdf'
          
        # adding pages to pdf writer object
        for page in range(start,end):
            pdfWriter.addPage(pdfReader.getPage(page))
          
        # writing split pdf pages to pdf file
        with open(outputpdf, "wb") as f:
            pdfWriter.write(f)
  
        # interchanging page split start position for next split
        start = end
        try:
            # setting split end position for next split
            end = splits[i+1]
        except IndexError:
            # setting split end position for last split
            end = pdfReader.numPages
          
    # closing the input pdf file object
    pdfFileObj.close()

    pdf = 'reliance_PD Q1 2022-23.pdf'
      
    # split page positions
    splits = [1,48]
      
    # calling PDFsplit function to split pdf
    PDFsplit(pdf, splits)