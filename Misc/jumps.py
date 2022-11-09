def jumps(n, a, b):
    values = [0] * n
    if n in (a, b):
        return 1
    if n < a and n < b:
        return 0
    if values[n-1] == 0:
        values[n-1] = jumps(n-a, a, b) + jumps(n-b, a, b)
    return values[n-1]


if __name__ == "__main__":
    print(jumps(4, 1, 2))  # 5
    print(jumps(8, 2, 3))  # 4
    print(jumps(11, 6, 7))  # 0
    print(jumps(30, 3, 5))  # 58
    print(jumps(100, 4, 5))  # 1167937
