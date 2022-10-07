    if i > biggest:
            biggest = i
    biggestIndex = T.index(biggest)

    for j in range(0,biggestIndex):
        print(T[j])
    


    count = 0
    biggest = 0
    for i in T:
        if i > biggest:
            biggest = i

        if biggest < T[i+1]:
            return count
        elif biggest > T[i+1]:
            count += 1
            
    return count    



    biggest = 0
    smallest = T[0]
    if T[0] > T[1]:
            return 0

    for i in T:
        if i > biggest:
            biggest = i
        elif i < smallest:
            smallest = i
        

    print("biggest: ", biggest, "smallest:", smallest)



    arr = [2,1,2,5,7,6]
max(arr[:-1]) <  arr[5] # max([2,1,2,5,7]) < 6
max(arr[:-2]) <  arr[4] # max([2,1,2,5]) < 7
max(arr[:-3]) <  arr[3] # max([2,1,2]) < 5





auxlist = []
    biggest = T[0]
    auxlist.append(biggest)
    for i in T:
        if i > biggest:
            biggest = i
            auxlist.append(biggest)
        elif i < biggest:
            auxlist.append(biggest)
    print(auxlist)

    for i in auxlist:
        if max(T[:i]) < min(T[i:], default=0):
            count += 1
    