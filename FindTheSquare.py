def main():
    n, m = map(int, input().split())
    
    # Read the grid
    grid = []
    for _ in range(n):
        row = list(input().strip())
        grid.append(row)

    # Function to check for the plus-center
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 'B':
                continue
            
            # Count up
            up = 0
            k = i
            while k >= 0 and grid[k][j] == 'B':
                up += 1
                k -= 1
            
            # Count down
            down = 0
            k = i
            while k < n and grid[k][j] == 'B':
                down += 1
                k += 1
            
            # Count left
            left = 0
            k = j
            while k >= 0 and grid[i][k] == 'B':
                left += 1
                k -= 1
            
            # Count right
            right = 0
            k = j
            while k < m and grid[i][k] == 'B':
                right += 1
                k += 1
            
            # Check if it is the center of the plus
            if up == down and down == left and left == right:
                # Output is 1-based index like in C++ code
                print(i + 1, j + 1)
                return

if __name__ == "__main__":
    main()
