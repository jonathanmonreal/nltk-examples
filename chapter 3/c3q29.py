# Jonathan Monreal

from nltk.corpus import brown

def ari(w, s):
    return 4.71 * w + 0.5 * s - 21.43

for category in brown.categories():
    print '%*s %9d' % (max(len(c) for c in brown.categories()), category,
                             ari(len(brown.words(categories = category)),
                                     len(brown.sents(categories = category))))
