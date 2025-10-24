def main():
    n, m = map(int, input().split())
    cost = list(map(int, input().split()))
    wallet = list(map(int, input().split()))

    i = 0
    j = 0
    cnt = 0

    while i < n and j < m:
        if cost[i] <= wallet[j]:
            j += 1
            cnt += 1
        i += 1

    print(cnt)


if __name__ == "__main__":
    main()
