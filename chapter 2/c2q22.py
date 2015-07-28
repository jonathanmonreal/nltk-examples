# Jonathan Monreal

from __future__ import division
import nltk

# Note that I took "word" literally here, and only count words for the spacing
def hedge(text):
    words = list(text) # stores the words of the text
    word_counter = 0   # counts words only

    # range takes into account that the text may be up to 1/3 longer with additions
    for i in range(0, len(text) + int((1 / 3) * len(text))):
        try:
            if word_counter % 4 == 0: # on every third word
                words.insert(i, 'like')
            if words[i].isalnum(): # if the token is alphanumeric
                word_counter += 1  # count it as a word
        except: # if text is less than 1/3 longer, must break
            break

    return words
