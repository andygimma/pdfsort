import unittest
from pdfsort.pdfsort import PDFSort

class TestPDFSort(unittest.TestCase):
    def test_init(self):
        filename = 'filename.pdf'
        pdf_sort = PDFSort(filename)
        assert pdf_sort.filename == filename
        assert pdf_sort != None

if __name__ == '__main__':
    unittest.main()
