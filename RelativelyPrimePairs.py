def main():
    l, r = map(int, input().split())
    need_pair = (r - l + 1) // 2
    pairs = []

    curr_pair = 0
    for i in range(l, r, 2):
        if curr_pair == need_pair:
            break
        pairs.append((i, i + 1))
        curr_pair += 1

    if curr_pair == need_pair:
        print("YES")
        for a, b in pairs:
            print(a, b)
    else:
        print("NO")


if __name__ == "__main__":
    main()
