import PyPDF2
import os

class PDFSort:
    def __init__(self, filename):
        try:
            self.filename = filename
            self.pdf = open(self.filename, 'rb')
            self.pdf_reader = PyPDF2.PdfFileReader(self.pdf, False)
            self.flipped = False
            self.create_temp_pdf()
            self.pdf_pages = self.pdf_reader.numPages
            self.generated_pages = []
        except IOError:
            print "Could not read file"
    def create_temp_pdf(self):
        pdf_writer = PyPDF2.PdfFileWriter()
        for index in range(self.pdf_reader.numPages):
            page = self.pdf_reader.getPage(index)
            pdf_writer.addPage(page)
        self.pdf_temp = pdf_writer
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
    def flip(self):
        pdf = PyPDF2.PdfFileWriter()
        for index in range(self.pdf_pages):
            page = self.pdf_temp.getPage(index)
            page.rotateClockwise(180)
            pdf.addPage(page)
        self.pdf_temp = pdf
        self.flipped = True
    def write_temp_pdf(self, new_filename):
        pdf_out = open(new_filename, 'wb')
        self.pdf_temp.write(pdf_out)
        pdf_out.close()
    def rotate_page_numbers(self, pages_string, degrees):
        page_numbers = self.get_page_numbers(pages_string)
        pdf = PyPDF2.PdfFileWriter()
        for index in range(self.pdf_pages):
            new_page = self.pdf_temp.getPage(index)
            if index in page_numbers:
                new_page.rotateClockwise(degrees)
            pdf.addPage(new_page)
        self.pdf_temp = pdf
    def generate_pdf(self, name, pages_string):
        ''' Create a new pdf from a given list of pages '''
        page_numbers = self.get_page_numbers(pages_string)
        pdf = PyPDF2.PdfFileWriter()
        for index in range(self.pdf_pages):
            if index in page_numbers:
                new_page = self.pdf_temp.getPage(index)
                pdf.addPage(new_page)
        self.generated_pages.append({'name': name, 'pdf': pdf})
    def write_generated_pdfs(self):
        for pdf in self.generated_pages:
            pdf_out = open(pdf['name'], 'wb')
            pdf['pdf'].write(pdf_out)
            pdf_out.close()

# generate_pdf(name, pages_list)
# self.generated_pdfs = [{name: pdf1, pages_list: array}]
# write_generated_pdfs(own_directories=False)
# split(start, end, increment, name)
# cli
# kedsort flip --rotate_pages --tracker --signin --canvass --split_increment
# ui
# flip checkbox
# rotate_pages [list numbers] [degrees]
# tracker [page_numbers]
# signin [page_numbers]
# canvass [page_numbers]
# split canvass [increment]
