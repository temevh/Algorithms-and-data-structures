def jumps(n, a, b):
    if a < n and b > n:
        return -1
    if a == n or b == n:
        return 1
    return (jumps(n-1, a, b) + jumps(n-2, a, b))


if __name__ == "__main__":
    print(jumps(4, 1, 2))  # 5
    print(jumps(8, 2, 3))  # 4
    print(jumps(11, 6, 7))  # 0
    print(jumps(30, 3, 5))  # 58
    print(jumps(100, 4, 5))  # 1167937
