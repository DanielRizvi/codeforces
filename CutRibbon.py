import sys
sys.setrecursionlimit(10000)

# Fast I/O (optional for large inputs)
def fast_input():
    return map(int, sys.stdin.readline().split())

# Memoization dictionary
rem = {}

def find_ans(n, a, b, c):
    if n == 0:
        return 0
    if n < 0:
        return -float('inf')
    if n in rem:
        return rem[n]
    
    rem[n] = 1 + max(find_ans(n - a, a, b, c),
                     find_ans(n - b, a, b, c),
                     find_ans(n - c, a, b, c))
    return rem[n]

def main():
    n, a, b, c = map(int, input().split())
    print(find_ans(n, a, b, c))

if __name__ == "__main__":
    main()
