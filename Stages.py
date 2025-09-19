def main():
    n, k = map(int, input().split())
    s = input().strip()
    
    s = sorted(s)  # sort characters
    
    ans = 0
    current = 0
    for i in range(len(s)):
        if k == 0:
            break
        if i == 0:
            current = ord(s[i]) - ord('a') + 1
            ans += current
            k -= 1
        else:
            temp = ord(s[i]) - ord('a') + 1
            if temp > current + 1:
                current = temp
                ans += current
                k -= 1
    
    if k > 0:
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    main()
