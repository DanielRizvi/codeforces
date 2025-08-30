n  = int(input())

lst = list(map(int,input().rstrip().split()))

min_el = lst[0]

ans = 1

for i in range(1,n):
    if lst[i] < min_el:
        min_el = lst[i]
        ans = i+1
    elif lst[i] == min_el:
        ans = "Still Rozdil"
    else:
        continue

print(ans)
        