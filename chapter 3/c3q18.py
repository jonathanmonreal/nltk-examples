# Jonathan Monreal

import re, nltk
from nltk.corpus import brown

raw = brown.raw(categories = 'humor')
tokens = nltk.word_tokenize(raw)

for word in tokens:
    if word[:2] == 'wh':
        print word[:word.find('/')]
