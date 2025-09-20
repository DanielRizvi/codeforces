def main():
    people, food = map(int, input().split())
    v = list(map(int, input().split()))
    
    # Sort the food array
    v.sort()

    low, high = 0, food // people + 10

    while low < high:
        expected = (low + high + 1) // 2
        cnt = 0
        temp = 0

        for i in range(food):
            if i == 0:
                temp += 1
            else:
                if v[i] == v[i - 1]:
                    temp += 1
                else:
                    temp = 1

            if temp >= expected:
                cnt += 1
                temp = 0

        if cnt >= people:
            low = expected
        else:
            high = expected - 1

    print(low)


if __name__ == "__main__":
    main()
