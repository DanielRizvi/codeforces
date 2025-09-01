n = int(input())

lst = list(map(int,input().rstrip().split()))
d = {}
for i in lst:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

if 5 not in d:
    print(0)
elif 0 not in d:
    print(-1)
else:
    if d[5] >= 9:
        print(("5"*9) * (d[5] // 9) + "0" * d[0])
    else:
        print(0)