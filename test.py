from itertools import product
import random

width = 10
mines = 20
locations = list(product(range(width), repeat=2))
mine_locs = random.sample(locations,k=mines)

print(mine_locs)
print(set(mine_locs))