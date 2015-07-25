# Jonathan Monreal

from __future__ import division
import nltk
from nltk.book import *

print set([word for word in text6 if word.endswith("ize") or 'z' in word
     or 'pt' in word or word.istitle()])
