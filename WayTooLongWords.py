n = int(input())

for _ in range(n):
    st = input()
    if len(st) < 11:
        #nothing
        print(st)
    else:
        print(st[0]+ str(len(st) - 2) + st[-1])