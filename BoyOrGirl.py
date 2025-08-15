lst = list(input())

#convert into set
ans = set(lst)
if len(ans)%2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")