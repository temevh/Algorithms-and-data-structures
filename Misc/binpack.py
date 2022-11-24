def binpack(items, S):
    bins = []
    bin = []
    size = S

    ctrSize = len(items) ** 10
    counter = ctrSize
    items.sort()
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

    
 
if __name__ == "__main__":

    items = [9, 3, 3, 6, 10, 4, 6, 8, 6, 3]
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