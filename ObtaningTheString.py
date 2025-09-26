def solve():
    n = int(input())
    s = list(input())
    t = list(input())
    
    v = []
    
    for i in range(n):
        if s[i] == t[i]:
            continue
        
        p = -1
        for j in range(i + 1, n):
            if s[j] == t[i]:
                p = j
                break
        
        if p == -1:
            print(-1)
            return
        
        for j in range(p - 1, i - 1, -1):
            s[j], s[j + 1] = s[j + 1], s[j]
            v.append(j)
    
    print(len(v))
    print(' '.join(str(x + 1) for x in v))


if __name__ == "__main__":
    # Uncomment below if multiple test cases are needed
    # TCS = int(input())
    # for _ in range(TCS):
    solve()
