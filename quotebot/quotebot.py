# Arch Quote bot v1.0 Created By KalkiDev.
# Licensed under MIT license.

import random
rnd=random.randint(1,28)
def primary():

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[rnd])

if __name__== "__main__":
  primary()
