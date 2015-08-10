# Jonathan Monreal

import nltk

def load(f):
    return open(f).read()

def tokenizer_a(raw):
    pattern = r'''(?x)
        \w+('\w+)*     # matches words with optional apostrophes
      | [\.,:!\?]      # matches punctuation
    '''
    return nltk.regexp_tokenize(raw, pattern)

def tokenizer_b(raw):
    pattern = r'''(?x)
        \$[0-9]+(\.[0-9]+)*
      | [0-9]+[\./][0-9]+[\./][0-9]+
      | ([A-Z]\w+(\s[a-z]+)?(\s[A-Z]\w+)*)+
    '''
    return nltk.regexp_tokenize(raw, pattern)

def tokenizer_examples():
    print tokenizer_a(load('corpus.txt'))
    print tokenizer_b('$50 is the amount owed to Bank of America on the date '\
                      '5/4/2018')
