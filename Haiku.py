def check(s: str) -> str:
    vowels = "aeiou"
    cnt = sum(1 for ch in s if ch in vowels)
    return str(cnt) if cnt < 10 else '0'


def main():
    ans = ""
    for _ in range(3):
        s = input().strip()
        ans += check(s)

    if ans == "575":
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
