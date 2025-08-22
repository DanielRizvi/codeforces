n = int(input())
lst = list(map(int,input().rstrip().split()))

m = int(input())
queries = list(map(int,input().rstrip().split()))

#dict 
d = {}
for i in range(n):
    #element : i index 
    d[lst[i]] = i

vasya = 0
petya = 0

for q in queries:
    index = d[q]
    #vasya index - no of comparisons 
    v = d[q] + 1
    #petya index - no of comparisons 
    p = n - d[q]

    vasya += v
    petya += p
print(vasya,petya)
