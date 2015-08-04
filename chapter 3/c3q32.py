# Jonathan Monreal

silly = 'newly formed bland ideas are inexpressible in an infuriating way'
# a
bland = silly.split()
# b
print ''.join([word[1] for word in bland])
# c
print ' '.join(bland)
# d
for word in sorted(bland):
    print word
