def main():
    n = int(input().strip())
    a = []
    b = []

    for i in range(n):
        x, y = map(int, input().split())
        a.append((x, i))
        b.append((y, i))

    # sort a in descending order by x
    a.sort(key=lambda p: p[0], reverse=True)
    # sort b in ascending order by y
    b.sort(key=lambda p: p[0])

    mx = 0
    if a[0][1] == b[0][1]:
        if n == 1:
            mx = 0
        else:
            mx = max(mx, b[1][0] - a[1][0])
    else:
        mx = max(mx, b[0][0] - a[1][0])
        mx = max(mx, b[1][0] - a[0][0])

    print(mx)


if __name__ == "__main__":
    main()
