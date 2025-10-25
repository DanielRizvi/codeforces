def find_depth(depth, employee, supervisor):
    if supervisor[employee] == -1:
        return depth
    else:
        return find_depth(depth + 1, supervisor[employee], supervisor)


def main():
    n = int(input())
    supervisor = [-1]  # index 0 unused for 1-based indexing

    # Input supervisors for each employee
    for _ in range(1, n + 1):
        temp = int(input())
        supervisor.append(temp)

    # Find maximum depth
    max_depth = 1
    for i in range(1, n + 1):
        depth = find_depth(1, i, supervisor)
        if depth > max_depth:
            max_depth = depth

    print(max_depth)


if __name__ == "__main__":
    main()
