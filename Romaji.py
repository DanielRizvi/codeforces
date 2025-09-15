def main():
    s = input().strip()
    s += 'k'  # Append 'k' at the end

    v = "aeioun"
    vowel = "aeiou"

    n = len(s) - 1
    for i in range(n):
        c = s[i]
        check = False

        # check if c is in v (aeioun)
        for j in range(6):
            if c == v[j]:
                check = True
                break

        if not check:
            c = s[i + 1]
            check = False

            # check if next character is a vowel
            for j in range(5):
                if c == vowel[j]:
                    check = True
                    break

            if not check:
                print("NO")
                return

    print("YES")


if __name__ == "__main__":
    main()
