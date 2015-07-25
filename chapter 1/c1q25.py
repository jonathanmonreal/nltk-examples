# Jonathan Monreal

from __future__ import division
import nltk
from nltk.book import *

sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']

print 'Part a:'
print str([word for word in sent if word.startswith('sh')]) + '\n'

print 'Part b:'
print [word for word in sent if len(word) > 4]
