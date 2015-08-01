# Jonathan Monreal

from __future__ import division
import nltk
from nltk.corpus import brown

cfd = nltk.ConditionalFreqDist(
    (genre,word)
    for genre in brown.categories()
    for word in brown.words(categories = genre))

my_words = ['good', 'evil', 'terrible', 'awful', 'wonderful']

cfd.tabulate(conditions = brown.categories(), samples = my_words)

# The use of words that might be tied to value judgements shows
# interesting results here. The presence of the word "evil" among the religious
# category isn't especially surprising, though it is interesting how common
# it is compared to in other genres. The use of such words in belles lettres
# is also unsurprising given its hightened emotional nature.
