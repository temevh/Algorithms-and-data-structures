#A quicksort algorithm with the following parameters
#A: list of integers, i: start index of the partition, j: end indx of selected partition

def qsort(A, i, j):
    pivot = findpivot(A,i,j)
    


def findpivot(A, i, j):
    return((i+j)/2)

    
    
  
if __name__ == "__main__":
    A = [9, 7, 1, 8, 5, 3, 6, 2, 4]
    print(A)    # [9, 7, 1, 8, 5, 3, 6, 2, 4]
    qsort(A, 0, len(A)-1)
    print(A)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]