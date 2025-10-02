# Python equivalent of the given C++ code

import bisect

def main():
    n, per_day, need_break = map(int, input().split())
    v = list(map(int, input().split()))
    
    Map = {val: idx for idx, val in enumerate(v)}
    Set = []  # will maintain a sorted list
    ans = [0] * n
    day = 0

    # Sort the array
    v_sorted = sorted(v)

    for x in v_sorted:
        # Find index of first element >= x - need_break
        idx = bisect.bisect_left(Set, x - need_break)
        
        if len(Set) == 0 or idx == 0:
            # No suitable previous element, assign new day
            day += 1
            ans[Map[x]] = day
        else:
            # Use the largest element < x - need_break
            value = Set[idx - 1]
            ans[Map[x]] = ans[Map[value]]
            # Remove it from the set
            Set.pop(idx - 1)
        
        # Insert current x to the sorted list
        bisect.insort(Set, x)
    
    print(day)
    print(' '.join(map(str, ans)))


if __name__ == "__main__":
    main()
