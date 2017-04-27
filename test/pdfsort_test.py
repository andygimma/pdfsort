import unittest
from pdfsort.pdfsort import PDFSort

class TestPDFSort(unittest.TestCase):
    def test_init(self):
        filename = 'filename.pdf'
        pdfsort = PDFSort(filename)
        assert pdfsort.filename == filename

if __name__ == '__main__':
    unittest.main()
