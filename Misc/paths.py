def paths(n, a, b):
    possible = 0
    while True:
        if n >= a:
            n = n-a
            possible += 1
        elif n >= b:
            n = n-b
            possible += 1
        if n == 0:
            break
        print("n: ", n)

    return possible


if __name__ == "__main__":
    print(paths(4, 1, 2))  # 5
    # print(paths(8, 2, 3))  # 4
    # print(paths(11, 6, 7))  # 0
    # print(paths(30, 3, 5))  # 58
    # print(paths(100, 4, 5))  # 1167937
