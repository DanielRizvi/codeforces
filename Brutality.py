import heapq

def main():
    hit, k = map(int, input().split())
    v = list(map(int, input().split()))
    s = input().strip()

    ans = 0
    pq = []
    
    # Using a min-heap with negative values to simulate a max-heap
    heapq.heappush(pq, -v[0])

    for i in range(1, hit):
        if s[i] == s[i - 1]:
            heapq.heappush(pq, -v[i])
        else:
            temp = k
            while temp and pq:
                ans += -heapq.heappop(pq)
                temp -= 1
            pq = []
            heapq.heappush(pq, -v[i])

    temp = k
    while temp and pq:
        ans += -heapq.heappop(pq)
        temp -= 1

    print(ans)


if __name__ == "__main__":
    main()
