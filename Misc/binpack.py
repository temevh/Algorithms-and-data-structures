def binpack(items, B):
    bins, bin = [], []
    size = B

    # Useampi kori -> käy koreja läpi kunnes esine mahtuu
    # Jos ei mahdu mihinkää, luo uusi
    ctr = len(items)
    counter = ctr
    items.sort(reverse=True)
    print(items)
    while items != []:
        for i in items:
            counter += 1
            if i <= size:
                size -= i
                bin.append(i)
                items.remove(i)
                counter = ctr
            elif i > size:  # Jos liian iso, lisää "seuraavaan" koriin
                pass
            if counter == 0:
                break

        bins.append(bin)
        bin = []
        size = B

    return bins


if __name__ == "__main__":

    items = [9, 3, 3, 6, 10, 4, 6, 8, 6, 3]
    #items = [9, 3, 3, 4, 6, 3, 10, 6, 8, 6]
    B = 10

    bins = binpack(items, B)

    for i in range(len(bins)):
        print(f"bin {i+1}: {bins[i]}")

# A possible output:
#   bin 1: [9]
#   bin 2: [3, 3, 4]
#   bin 3: [6, 3]
#   bin 4: [10]
#   bin 5: [6]
#   bin 6: [8]
#   bin 7: [6]


'''
def binpack(items, S):
    bins, bin = [], []
    size = S

    ctrSize = len(items) ** 0.7
    counter = ctrSize
    items.sort(reverse=True)
    print(items)
    while items != []:
        for i in items:
            counter += 1
            if i <= size:
                size -= i
                bin.append(i)
                items.remove(i)
                counter = ctrSize
            if counter == 0:
                break

        bins.append(bin)
        bin = []
        size = S

    return bins
'''
