def sums(items):
    arr = helper(items)
    toReturn = []
    arr.pop(0)
    summa = 0
    for elem in arr:
        summa = sum(elem)
        if summa not in toReturn:
            toReturn.append(summa)
    return len(toReturn)


def helper(items):
    res = [[]]

    for i in range(len(items)):
        for num in res[:]:
            tmp = [items[i]] + num
            tmp.sort()
            if (tmp not in res):
                res.append(tmp)
    res.sort()
    return res


if __name__ == "__main__":
    print(sums([1, 2, 3]))                  # 6
    print(sums([2, 2, 3]))                  # 5
    print(sums([1, 3, 5, 1, 3, 5]))         # 18
    print(sums([1, 15, 5, 23, 100, 55, 2]))  # 121
