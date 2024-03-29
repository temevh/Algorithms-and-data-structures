def jumps(n, a, b):
    nums = [a, b]
    values = [0] * (n+1)
    values[0] = 1
    for i in range(n+1):
        for num in nums:
            if i >= num:
                values[i] += values[i-num]
    return values[-1]


if __name__ == "__main__":
    print(jumps(4, 1, 2))  # 5
    print(jumps(8, 2, 3))  # 4
    print(jumps(11, 6, 7))  # 0
    print(jumps(30, 3, 5))  # 58
    print(jumps(100, 4, 5))  # 1167937
