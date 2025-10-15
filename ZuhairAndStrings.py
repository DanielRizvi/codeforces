def main():
    n = int(input())
    k = int(input())
    s = input().strip() + '0'  # Add '0' to avoid out-of-bound access
    
    alphabet = [0] * 27
    rem = 1

    for i in range(n):
        if rem >= k:
            alphabet[ord(s[i]) - ord('a')] += 1
            rem = 1
        elif s[i] == s[i + 1]:
            rem += 1
        else:
            rem = 1

    ans = max(alphabet)
    print(ans)


if __name__ == "__main__":
    main()
