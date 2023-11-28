# Create a python program that will download all images from a given URL.

import os
import re
import requests
from bs4 import BeautifulSoup

def download_images(site):
    # Make the request to the website
    r = requests.get(site)

    # Create a BeautifulSoup object and specify the parser
    soup = BeautifulSoup(r.text, 'html.parser')

    # Find all images on the page
    images = soup.findAll('img')

    # Set the directory to store images
    directory = "images"

    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)
        print("Directory created: {}".format(directory))

    # Download all images
    for image in images:
        filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', image['src'])
        if not filename:
            print("Regex didn't match with the url: {}".format(image['src']))
            continue
        with open(os.path.join(directory, filename.group(1)), 'wb') as f:
            if 'http' not in image['src']:
                # Sometimes an image source can be relative
                # If it is, provide the base url which also happens
                # to be the site variable at the moment.
                url = '{}{}'.format(site, image['src'])
            else:
                url = image['src']
            response = requests.get(url)
            f.write(response.content)

# Call the function with the URL of the website you want to download images from
download_images('http://jamesgress.com')

