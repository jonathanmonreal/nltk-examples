# Jonathan Monreal

import nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters

def guess_syllables(text):
    
    prondict = nltk.corpus.cmudict.dict() # Stores the pronunciation dictionary

    num_syllables = 0                     # Stores the numer of syllables

    for word in text:
        average = 0
        try:
            # There are typically multiple sets of phones for each word
            word_phones = prondict[word]
            for phones in word_phones:    # For each set of phone
                for phone in phones:      # For each individual phone
                    # If there is a digit, it indicates inflection
                    if phone[-1].isdigit():
                        average += 1
            average /= float(len(word_phones)) # Average the number of phones
            num_syllables += average           # Add the average for the word
        except:
            pass

    return int(num_syllables)
