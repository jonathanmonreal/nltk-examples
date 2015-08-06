# Jonathan Monreal

import re, nltk
from nltk.corpus import brown

raw = brown.raw(categories = 'humor')
tokens = re.findall(r'\s(wh[\w]+)', raw)

for word in tokens:
    print word
