k = int(input())
a = list(map(int,input().rstrip().split()))

a.sort(reverse=True)

counter = 0

for i in a:
    if k <= 0:
        break
    else:
        counter += 1
        k -= i

if k>0:
    print(-1)
else:
    print(counter)