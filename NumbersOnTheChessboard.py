def main():
    n, m = map(int, input().split())

    for _ in range(m):
        x, y = map(int, input().split())
        ans = 0

        if n % 2 == 1:  # n is odd
            if x % 2 == 1:  # x odd
                if y % 2 == 1:  # y odd
                    ans = (x - 1) * ((n // 2) + (n % 2)) + 1 + (y // 2) - ((x - 1) // 2)
                else:  # y even
                    temp = ((n // 2) + (n % 2)) * n + 1
                    ans = temp + (x - 1) * ((n // 2) + (n % 2)) + (y // 2) - 1 + x // 2
                    ans -= (n // 2) + (x - 1)
            else:  # x even
                if y % 2 == 1:  # y odd
                    temp = ((n // 2) + (n % 2)) * n + 1
                    ans = (x - 1) * ((n // 2) + (n % 2)) + (y // 2) + temp + (x - 1) // 2
                    ans -= (n // 2) + (x - 1)
                else:  # y even
                    ans = (x - 1) * ((n // 2) + (n % 2)) + (y // 2) - ((x - 1) // 2)

        else:  # n is even
            if x % 2 == 1:  # x odd
                if y % 2 == 1:  # y odd
                    ans = (x - 1) * ((n // 2) + (n % 2)) + 1 + (y // 2)
                else:  # y even
                    temp = ((n // 2) + (n % 2)) * n + 1
                    ans = temp + (x - 1) * ((n // 2) + (n % 2)) + (y // 2) - 1
            else:  # x even
                if y % 2 == 1:  # y odd
                    temp = ((n // 2) + (n % 2)) * n + 1
                    ans = (x - 1) * ((n // 2) + (n % 2)) + (y // 2) + temp
                else:  # y even
                    ans = (x - 1) * ((n // 2) + (n % 2)) + (y // 2)

        print(ans)


if __name__ == "__main__":
    main()
