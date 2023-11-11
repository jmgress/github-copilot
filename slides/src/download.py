# Create a python program that will download all images from a given URL.

import requests
import os
import sys
import re
import urllib.request
from bs4 import BeautifulSoup

def download_images(url):
    # Get the page content
    page = requests.get(url)

    # Create a soup object
    soup = BeautifulSoup(page.content, 'html.parser')

    # Find all images in the page
    images = soup.findAll('img')

    # Set the directory name
    directory = "images"

    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Download all images
    for image in images:
        filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', image['src'])
        if not filename:
            print("Regex didn't match with the url: {}".format(image['src']))
            continue
        with open(directory + '/' + filename.group(1), 'wb') as f:
            if 'http' not in image['src']:
                # Sometimes an image source can be relative
                # If it is provide the base url which also happens
                # to be the site variable atm.
                url = '{}{}'.format(site, image['src'])
            response = requests.get(url)
            f.write(response.content)