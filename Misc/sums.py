def sums(items):
    arr = [[]]
    toReturn = []
    for i in range(len(items)):
        for num in arr[:]:
            tmp = [items[i]] + num
            arr.append(tmp)
            toReturn.append(sum(tmp))
    return len(list(dict.fromkeys(toReturn)))


if __name__ == "__main__":
    print(sums([1, 2, 3]))                  # 6
    print(sums([2, 2, 3]))                  # 5
    print(sums([1, 3, 5, 1, 3, 5]))         # 18
    print(sums([1, 15, 5, 23, 100, 55, 2]))  # 121
