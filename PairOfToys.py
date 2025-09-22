def main():
    # Read inputs
    n, k = map(int, input().split())

    # Equivalent logic
    L = max(k - n, 1)
    R = (k - 1) // 2

    # Print result
    print(max(R - L + 1, 0))


if __name__ == "__main__":
    main()
