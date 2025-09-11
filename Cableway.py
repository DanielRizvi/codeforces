def main():
    r, g, b = map(int, input().split())

    r = (r + 1) // 2
    g = (g + 1) // 2
    b = (b + 1) // 2

    output = 0
    if b >= g and b >= r:
        output = 30 + 3 * b - 1
    elif g >= r:
        output = 30 + 3 * g - 2
    else:
        output = 30 + 3 * r - 3

    print(output)


if __name__ == "__main__":
    main()
