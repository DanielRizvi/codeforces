def main():
    n = int(input())
    vec = list(map(int, input().split()))

    ans = 0
    for i in range(1, n - 1):
        if vec[i - 1] == 1 and vec[i] == 0 and vec[i + 1] == 1:
            ans += 1
            vec[i + 1] = 0  # prevent overlap

    print(ans)


if __name__ == "__main__":
    main()
