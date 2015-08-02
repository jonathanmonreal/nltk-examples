# Jonathan Monreal

from __future__ import division
import nltk
from nltk.corpus import wordnet as wn

nouns = wn.all_synsets('n') # stores all noun synsets
total_branches = 0          # used to store the branches
total = 0                   # used to store the number of nouns with branches

for noun in nouns:
    branches = len(noun.hyponyms())
    if branches > 0: # if the noun has branches
        total_branches += branches
        total += 1

branching_factor = total_branches / total
print branching_factor
