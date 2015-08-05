# Jonathan Monreal

f = open('word_freq.txt', 'rU').readlines()
word_freqs = []

for i in range(0, len(f)):
    # append to word_freqs the line stripped of the newline character and split
    word_freqs.append(f[i].strip('\n').split())
    # convert the number to an int
    word_freqs[i][1] = int(word_freqs[i][1])

print word_freqs
