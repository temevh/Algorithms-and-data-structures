def paths(n, a, b):
    if (a <= n or b <= a):
        return -1


if __name__ == "__main__":
    print(paths(4, 1, 2))  # 5
    print(paths(8, 2, 3))  # 4
    print(paths(11, 6, 7))  # 0
    print(paths(30, 3, 5))  # 58
    print(paths(100, 4, 5))  # 1167937
