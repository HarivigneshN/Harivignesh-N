a=input()
from itertools import permutations
perm = permutations(a) 
for i in list(perm): 
    print ("".join(i)) 
