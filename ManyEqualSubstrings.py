def find_repeating(s: str, n: int) -> str:
    """
    Finds the repeating suffix part of string s.
    If found, return that suffix, else return the whole string.
    """
    for i in range(1, n):
        k = 0
        j = i
        while j < n:
            if s[k] != s[j]:
                break
            if j == n - 1:  # matched till end
                return s[k + 1:]
            j += 1
            k += 1
    return s


def main():
    n, k = map(int, input().split())
    s = input().strip()

    repeating = find_repeating(s, n)

    # Build the answer
    result = s + repeating * (k - 1)
    print(result)


if __name__ == "__main__":
    main()
