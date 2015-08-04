# Jonathan Monreal

import nltk
import urllib
from bs4 import BeautifulSoup as bs

# I am using BeautifulSoup here rather than NLTK's built-in functionality
# for HTML stripping

def strip_html(url):
    # get the page and make it a BeautifulSoup object
    html = bs(urllib.urlopen(url).read())
    return html.get_text()
