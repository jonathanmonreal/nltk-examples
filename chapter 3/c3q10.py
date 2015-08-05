# Jonathan Monreal

sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']

for i in range(0, len(sent)):
    sent[i] = (sent[i], len(sent[i]))

print str(sent)
