# Jonathan Monreal

import re, urllib
from nltk.corpus import words
from bs4 import BeautifulSoup as bs

def unknown(url):
    # get the HTML, as a string
    html = str(bs(urllib.urlopen(url).read()))
    # find all substrings
    substrings = set(re.findall(r'[a-z]+', html))
    # specify the wordlist
    wordlist = words.words()
    # return the words not in the wordlist
    return [word for word in substrings if word not in wordlist]

# A lot of the results are HTML tags, javascript, CSS, etc. Also present are
# words that start with capital letters such that the regular expression cuts
# off the first letter.
