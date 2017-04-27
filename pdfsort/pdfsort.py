import PyPDF2
import os

from unittest.mock import mock_ope

class PDFSort:
    def __init__(self, filename):
        try:
            self.filename = filename
            self.pdf_file = open(input_pdf, 'rb')
            self.pdf_reader = PyPDF2.PdfFileReader(pdf_in, False)
        except IOError:
            print "Could not read file"
        except Exception:
            print "Unknown error"
