def main():
    n, k = map(int, input().split())
    ans = (n + k - 1) // n   # integer division
    print(ans)


if __name__ == "__main__":
    main()
