def main():
    n, d = map(int, input().split())
    current = -1
    total = 0
    
    temps = list(map(int, input().split()))
    
    for temp in temps:
        if current < temp:
            current = temp
        else:
            times = 1 + (current - temp) // d
            current = temp + times * d
            total += times
    
    print(total)


if __name__ == "__main__":
    main()
