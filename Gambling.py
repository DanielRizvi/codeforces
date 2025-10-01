def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort(reverse=True)
    b.sort(reverse=True)

    i = j = 0
    up = low = 0

    for k in range(1, 2 * n + 1):
        if k % 2 == 1:  # odd turn -> "up"
            if i < n and (a[i] >= b[j] if j < n else True):
                up += a[i]
                i += 1
            elif j < n:
                j += 1
            else:
                up += a[i]
                i += 1
        else:  # even turn -> "low"
            if j < n and (b[j] >= a[i] if i < n else True):
                low += b[j]
                j += 1
            elif i < n:
                i += 1
            else:
                low += b[j]
                j += 1

    print(up - low)


if __name__ == "__main__":
    main()
