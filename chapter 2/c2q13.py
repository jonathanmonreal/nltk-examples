# Jonathan Monreal

from __future__ import division
from nltk.corpus import wordnet as wn

counter = 0
total = 0
for synset in wn.all_synsets('n'):
    total += 1
    if len(synset.hyponyms()) == 0:
        counter += 1
print counter / total
