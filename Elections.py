import sys
import time

# FAST_IO equivalent
file = False
rt = True

if rt and file:
    tStart = time.time()

def main():
    # Input n
    n = int(input())
    a = list(map(int, input().split()))
    
    k = max(a)            # maximum value in the list
    elodriep = sum(a)     # sum of all elements
    
    # Start from k and search for the answer
    i = k
    while True:
        awruk = sum(i - j for j in a)
        if awruk > elodriep:
            print(i)
            break
        i += 1

if __name__ == "__main__":
    main()
    
    if rt and file:
        print("\nTime taken: {:.6f}s".format(time.time() - tStart))
