def permutation(k):
    numbers = []
    n = 5
    if k == n:
        print(numbers)
    else:
        for i in range(1, n):
            if i not in numbers:
                numbers[k] = i
                included = True
                permutation(k+1)
                included = False


permutation(1)
