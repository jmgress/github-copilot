# Unit Test for downloadimages.py
# Call the function with the URL of the website you want to download pdfs from and the directory to store the pdf files
# Test should have a maximum of 10 files

import unittest
import os
import re
import requests
from bs4 import BeautifulSoup
from downloadimages import download_pdf

class TestDownloadImages(unittest.TestCase):
    def test_download_pdf(self):
        url = 'http://jamesgress.com'
        directory = 'pdfs'
        max_files = 10
        download_pdf(url, directory, max_files)
        self.assertTrue(os.path.exists(directory))
        self.assertTrue(len(os.listdir(directory)) <= max_files)
        for file in os.listdir(directory):
            # regex to match pdf files and image files
            self.assertTrue(re.match(r'([^\s]+(\.(?i)(pdf))$)', file))
        for file in os.listdir(directory):
            os.remove(os.path.join(directory, file))
        os.rmdir(directory)

if __name__ == '__main__':
    unittest.main()

# Path: slides/src/downloadimages.py