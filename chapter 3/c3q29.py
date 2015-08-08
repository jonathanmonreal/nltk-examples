# Jonathan Monreal

from __future__ import division
from nltk.corpus import brown

def ari(words, sentences):
    chars = 0

    for word in words:
        chars += len(word)
    
    return (4.71 * (chars / len(words)) + 0.5 * (len(words) / len(sentences))
            - 21.43)

for category in brown.categories():
    print '%*s %9f' % (max(len(c) for c in brown.categories()), category,
                       ari(brown.words(categories = category),
                       brown.sents(categories = category)))
