# Jonathan Monreal

from __future__ import division
from nltk.corpus import wordnet as wn

counter = 0 # used to store the number of synsets with no hyponyms

for synset in wn.all_synsets('n'):
    if len(synset.hyponyms()) == 0: # if the synset has no hyponyms
        counter += 1

print counter / len(wn.all_synsets('n'))
