from PyPDF2 import PdfFileWriter, PdfFileReader
from DigitRank import *
import time
import serial

# Print how many pages input1 has:


def getPDFContent(path):
    content = ''
    # Load PDF into pyPDF
    pdf = PdfFileReader(file(path, 'rb'))
    # Iterate pages
    for i in range(0, pdf.getNumPages()):
        # Extract text from page and add to content
        content += pdf.getPage(i).extractText() + '\n'
    # Collapse whitespace
    content = ' '.join(content.replace(u'\xa0', ' ').strip().split())
    return content


def main(ser):
    pdf = PdfFileReader(file('/home/pi/Documents/documents/SF424_page2.pdf', 'rb'))
    content = pdf.getPage(0).extractText().encode('ascii', 'ignore')
    for word in content:
        # word = word+" "
        for ch in word:
            print ch
            x = Rank(ch)
            ser.write(str(x)+'\r')
            y = ser.readline().strip()
            while y != 'touchup':
                y = ser.readline().strip()
