while n != 0:
        if n >= a:
            n = n-a
            possible += 1
        elif n >= b:
            n = n-b
            possible += 1
    print("n:", n)
    return possible


possible = 0
    if (a + b) > n:
        return 0
    i = 0
    total = 0
    while total <= n:
        total += a
        i += 1
    return ((n-i) % b)
