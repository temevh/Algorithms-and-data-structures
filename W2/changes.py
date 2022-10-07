from random import randint
import random

def changes(A):
    count = 0
    try:
        for i in range(len(A)):
            if A[i] == A[i+1]:
                A[i+1] = random.randint(0,100000000000000000000000)
                count = count + 1
                i = i + 1
    except:
        return(count)
    

if __name__ == "__main__":
    print(changes([1, 1, 2, 2, 2]))     # 2
    print(changes([1, 2, 3, 4, 5]))     # 0
    print(changes([1, 1, 1, 1, 1]))     # 2  