#A program to create subsets with a given int.
#For example subsets(int 3) -> [1],[2],[3],[1,2],[2,3][1,2,3] (powerset?)

'''
def subsets(n: int) -> list:
    subs = []
    aux = []
    max = 0
    for i in range(1, n+1):
        sub = [i]
        subs.append(sub)
        max = i
        for j in range(1, max):
            aux.append(j)
        subs.append(aux)

    return subs
'''
def subsets(n: int) -> list:
    fullset = []
    for i in range(1, n+1):
        fullset.append(i)
    print(fullset)
    subs = []
    for i in range(2**len(fullset)):
        subset = []
        for k in range(len(fullset)):
            if i & 1<<k:
                subset.append(fullset[k])
        subs.append(subset)
    subs.pop(0)
    return subs


if __name__ == "__main__":
    print(subsets(3))   # [[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

    #print(subsets(4))   # [[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3],
                        #  [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4],
                        #  [2, 3, 4], [1, 2, 3, 4]]

    #S = subsets(10)
    #print(S[95])    # [6, 7]
    #print(S[254])   # [1, 2, 3, 4, 5, 6, 7, 8]
    #print(S[826])   # [1, 2, 4, 5, 6, 9, 10]