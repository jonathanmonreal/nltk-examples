# Jonathan Monreal

import nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
from nltk.corpus import abc

def ari(raw):

    # tokenize raw text and get words
    tokens = nltk.wordpunct_tokenize(raw)
    words = [word.lower() for word in tokens if word.isalpha()]

    # instantiate punctuation parameters
    punkt_params = PunktParameters()
    # specify abbreviations to be ignored in sentence separation
    punkt_params.abbrev_types = set(['dr', 'inc', 'mr', 'mrs', 'ms', 'prof',
                                     'etc'])
    # separate into sentences using a PuktSentenceTokenizer
    sentences = PunktSentenceTokenizer(punkt_params).tokenize(raw)

    chars = 0

    for word in words:
        chars += len(word)
    
    return (4.71 * (chars / len(words)) + 0.5 * (len(words) / len(sentences))
            - 21.43)

for fileid in abc.fileids():
    print '%*s %9f' % (max(len(f) for f in abc.fileids()), fileid,
                       ari(abc.raw(fileids=fileid)))
