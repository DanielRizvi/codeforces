# Translated from C++ to Python by ChatGPT (GPT-5)
# Original Author: Saurav Paul

def solve(v):
    n = len(v)
    diff = [v[i][0] - v[i - 1][0] for i in range(1, n)]

    # Case 1: Check if all differences are the same
    is_same = all(diff[i] == diff[i - 1] for i in range(1, len(diff)))
    if is_same:
        print(v[0][1])
        return

    # Case 2: Check if removing the first element fixes the sequence
    is_same = True
    for i in range(2, n - 1):
        if i == 2 and diff[i] != diff[0] + diff[1]:
            is_same = False
            break
        elif i != 2 and diff[i] != diff[i - 1]:
            is_same = False
            break
    if is_same:
        print(v[1][1])
        return

    # Case 3: Find the most common difference
    from collections import Counter
    freq = Counter(diff)
    different = max(freq, key=freq.get)

    cnt = 0
    index = 0
    rem = -1

    for i in range(1, n - 1):
        t = i - 1
        if rem == t:
            t -= 1
        if v[i][0] - v[t][0] != different:
            if v[i + 1][0] - v[i - 1][0] == different:
                cnt += 1
                index = v[i][1]
                rem = i
            else:
                cnt = 5
                break

    temp = n - 2
    if temp == rem:
        temp -= 1
    if v[n - 1][0] - v[temp][0] != different:
        cnt += 1
        index = v[n - 1][1]

    if cnt == 1:
        print(index)
    else:
        print(-1)


def main():
    n = int(input().strip())
    v = [(int(x), i + 1) for i, x in enumerate(input().split())]
    v.sort(key=lambda x: x[0])
    solve(v)


if __name__ == "__main__":
    main()
