# Jonathan Monreal

import random

# generator expression inside a ''.join() function
weird = ''.join([random.choice("aehh ") for i in range(0, 500)])
print weird
# normalize
weird = weird.split()
weird = ' '.join(weird)
print weird
