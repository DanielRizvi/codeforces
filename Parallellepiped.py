
"""
logic -
rectangluar parallellpiped so the areas of faces are ab, bc and ca
given ab, bc, ca we solve for a b c
4 * (a+b+c) will give the answer

"""

import math
ab,bc,ca = list(map(int,input().rstrip().split()))
a = int(math.sqrt((ab*ca) / bc ))
b = int(math.sqrt((ab*bc) / ca ))
c = int(math.sqrt((bc*ca) / ab ))

print(4 *(a+b+c))