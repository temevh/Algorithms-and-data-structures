#A quicksort algorithm with the following parameters
#A: list of integers, i: start index of the partition, j: end index of selected partition

def qsort(A, i, j):
    #pivot = findpivot(i,j)
    #A[pivot], A[j] = A[j], A[pivot]
    #print(A)
    if i >= j:
        return
    k = partition(A, i, j, A[i])
    #A[k], A[j] = A[j], A[k]
    #if ((k-i) > 1):
    qsort(A, i, k-1)
    #if ((j-k) > 1):
    qsort(A, k+1, j)


def partition(A, i, right, pivot):
    left = i + 1
    while True:
        while left <= right and A[right] >= pivot:
            right -=1
        while left <= right and A[left] <= pivot:
            left += 1
        if left <= right:
            A[left], A[right] = A[right], A[left]
        else:
            break
    A[i], A[right] = A[right], A[i]

    return right


def findpivot(i, j):
    return(int((i+j)/2))

if __name__ == "__main__":
    A = [9, 7, 1, 8, 5, 3, 6, 2, 4]
    print(A)    # [9, 7, 1, 8, 5, 3, 6, 2, 4]
    qsort(A, 0, len(A)-1)
    print(A)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]