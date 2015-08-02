# Jonathan Monreal

from __future__ import division
import nltk
from nltk.corpus import wordnet as wn

word_pairs = [('car', 'automobile'), ('gem', 'jewel'), ('journey', 'voyage'),
              ('boy', 'lad'), ('coast', 'shore'), ('asylum', 'madhouse'),
              ('magician', 'wizard'), ('midday', 'noon'), ('furnace', 'stove'),
              ('food', 'fruit'), ('bird', 'cock'), ('bird', 'crane'),
              ('tool', 'implement'), ('brother', 'monk'), ('lad', 'brother'),
              ('crane', 'implement'), ('journey', 'car'), ('monk', 'oracle'),
              ('cemetary', 'woodland'), ('food', 'rooster'), ('coast', 'hill'),
              ('forest', 'graveyard'), ('shore', 'woodland'), ('monk', 'slave'),
              ('coast', 'forest'), ('lad', 'wizard'), ('chord', 'smile'),
              ('glass', 'magician'), ('rooster', 'voyage'), ('noon', 'string')]
scores = []
for word_pair in word_pairs:
    similarity = 0
    comparisons = 0
    for word0_synset in wn.synsets(word_pair[0]):
        for word1_synset in wn.synsets(word_pair[1]):
            try:
                similarity += word0_synset.path_similarity(word1_synset)
                comparisons += 1
            except:
                pass
    try:
        scores.append((word_pair, similarity / comparisons))
    except:
        scores.append((word_pair, 0))

sorted_scores = sorted(scores, key=lambda score: 1 - score[1])
