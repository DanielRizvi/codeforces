import sys
from itertools import combinations

def main():
    n = int(input())
    vitamins = []
    
    A = B = C = ABC = -1
    
    for _ in range(n):
        temp, s = input().split()
        temp = int(temp)
        final = ['0', '0', '0']
        if 'A' in s:
            final[0] = '1'
        if 'B' in s:
            final[1] = '1'
        if 'C' in s:
            final[2] = '1'
        final_str = ''.join(final)
        vitamins.append((temp, final_str))
        
        if final_str == "100":
            A = temp if A == -1 else min(A, temp)
        elif final_str == "010":
            B = temp if B == -1 else min(B, temp)
        elif final_str == "001":
            C = temp if C == -1 else min(C, temp)
        elif final_str == "111":
            ABC = temp if ABC == -1 else min(ABC, temp)
    
    ans = sys.maxsize
    flag = False
    
    # Combination of A, B, C
    if A != -1 and B != -1 and C != -1:
        ans = A + B + C
        flag = True
    
    # Single ABC vitamin
    if ABC != -1:
        ans = min(ans, ABC)
        flag = True
    
    # Any two combinations
    for i in range(n-1):
        a_val, a_str = vitamins[i]
        for j in range(i+1, n):
            b_val, b_str = vitamins[j]
            if all(a_str[k] == '1' or b_str[k] == '1' for k in range(3)):
                ans = min(ans, a_val + b_val)
                flag = True
    
    print(ans if flag else -1)

if __name__ == "__main__":
    main()
