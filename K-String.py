k = int(input())
st = input()

d = {}

for i in st:
    if i in d:
        d[i] += 1

    else:
        d[i] = 1

ans = ""
invalid = False
for i in d:
    if not d[i] % k == 0:
        invalid = True
        break

if invalid:
    print(-1)
else:
    #find my basic string 
    s = ""
    for i in d:
        s += i * (d[i] // k)
    ans = s * k 
    print(ans)