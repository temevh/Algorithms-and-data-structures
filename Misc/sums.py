def sums(items):
    arr = [[]]
    toReturn = []
    for i in range(len(items)):
        for num in arr[:]:
            tmp = [items[i]] + num
            tmp.sort()
            if (tmp not in toReturn):
                arr.append(tmp)
    arr.sort()
    for item in arr:
        summa = sum(item)
        if summa not in toReturn:
            toReturn.append(summa)
    return len(toReturn)-1


if __name__ == "__main__":
    print(sums([1, 2, 3]))                  # 6
    print(sums([2, 2, 3]))                  # 5
    print(sums([1, 3, 5, 1, 3, 5]))         # 18
    print(sums([1, 15, 5, 23, 100, 55, 2]))  # 121
