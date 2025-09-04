n = int(input())
for _ in range(n):
    a,b = list(map(int,input().rstrip().split()))

    if a%2 != 0:
        print("NO")
    else:
        if b%2 ==0:
            print("YES")
        else:
            if a >=2:
                print("YES")
            else:
                print("NO")