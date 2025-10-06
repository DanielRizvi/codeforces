def main():
    n = int(input())
    print("1", end=' ')
    n -= 1
    r = n - 1
    if r % 3 == 0:
        r -= 1
    print(r, n - r)

if __name__ == "__main__":
    main()
