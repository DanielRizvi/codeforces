def longest_subsequence_length(arr):
    n = len(arr)
    ans = 1
    temp = 1
    
    for i in range(1, n):
        if arr[i - 1] * 2 >= arr[i]:
            temp += 1
        else:
            ans = max(ans, temp)
            temp = 1
    return max(ans, temp)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(longest_subsequence_length(arr))
