# Jonathan Monreal

import nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters

def guess_syllables(text):
    
    prondict = nltk.corpus.cmudict.dict()

    num_syllables = 0

    for word in text:
        average = 0
        try:
            word_phones = prondict[word]
            for phones in word_phones:
                for phone in phones:
                    # If there is a digit, it indicates inflection
                    if phone[-1].isdigit():
                        average += 1
            average /= float(len(word_phones))
            num_syllables += average
        except:
            pass

    return int(num_syllables)
