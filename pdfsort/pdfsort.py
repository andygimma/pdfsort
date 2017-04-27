import PyPDF2
import os

class PDFSort:
    def __init__(self, filename):
        try:
            self.filename = filename
            self.pdf = open(self.filename, 'rb')
            self.pdf_reader = PyPDF2.PdfFileReader(self.pdf, False)
        except IOError:
            print "Could not read file"
        except Exception:
            print "Unknown error"
    def get_page_numbers(self, string):
        page_numbers = []
        raw_list = string.split(',')
        for group in raw_list:
            if "-" not in group:
                page_numbers.append(int(group) - 1)
            else:
                t = group.split("-")
                for i in range(int(t[0]), int(t[1]) + 1):
                    page_numbers.append(int(i) - 1)
        return page_numbers
