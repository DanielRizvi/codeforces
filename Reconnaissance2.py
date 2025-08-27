n = int(input())

a = list(map(int,input().rstrip().split()))

#logic
"""
set minimum as difference between last and first element
then iterate over the list, comparing each two elements
incase it is lower, update the minimum distance and the answer repeat
"""

min_difference = abs(a[0] - a[-1])
p1 = 1
p2 = n

for i in range(1,n):
    difference = abs(a[i] - a[i-1])
    if difference < min_difference:
        min_difference = difference
        p1 = i + 1
        p2 = i

print(p1,p2)