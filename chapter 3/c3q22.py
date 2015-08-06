# Jonathan Monreal

import re, urllib
from nltk.corpus import words
from bs4 import BeautifulSoup as bs

# More could be done to strip the unwanted tags and code, but for the purpose
# of this example, I am only requiring whitespace before and after and
# including upper- as well as lowecase characters.
def unknown(url):
    # get the HTML, as a string
    html = str(bs(urllib.urlopen(url).read()))
    # find all substrings
    substrings = set(re.findall(r'\s+([a-zA-Z]+)\s+', html))
    substrings = [word.lower() for word in substrings]
    # specify the wordlist
    wordlist = words.words()
    # return the words not in the wordlist
    return [word for word in substrings if word not in wordlist]
