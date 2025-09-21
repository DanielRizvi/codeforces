def main():
    # Input n and m
    n, m = map(int, input().split())
    
    # Create a list to mark covered segments
    segment = [False] * (m + 1)
    cnt = 0
    
    # Read n pairs (x, y)
    for _ in range(n):
        x, y = map(int, input().split())
        if x > y:
            x, y = y, x
        for k in range(x, y + 1):
            if not segment[k]:
                cnt += 1
                segment[k] = True
    
    # Count uncovered positions
    cnt = m - cnt
    print(cnt)
    
    # Print all uncovered positions
    for i in range(1, m + 1):
        if not segment[i]:
            print(i, end=" ")

if __name__ == "__main__":
    main()
