def main():
    n = int(input())
    v = []
    
    # read pairs
    for _ in range(n):
        a, b = map(int, input().split())
        if a < b:
            a, b = b, a   # ensure a >= b
        v.append((a, b))
    
    flag = True
    for i in range(n - 1):
        # check ordering condition
        if v[i][0] < v[i+1][0]:
            # swap elements of next pair
            v[i+1] = (v[i+1][1], v[i+1][0])
        if v[i][0] < v[i+1][0]:
            flag = False
            break
    
    if flag:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
