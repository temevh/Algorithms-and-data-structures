def split(T):
    count = 0
    LeftList = [0] * len(T)   #Fill the lists to avoid index out of bounds errors
    RightList = [0] * len(T) 
    edellmax = 0
    edellmin = T[-1]          #Set the edellmin variable to the last element on input array
    RightList[-1] = T[-1]     #Set the rightlists last element to the last element of input array

    for i in range(1, len(T)): 
        if T[-i] < edellmin:    #Looping backwards, if current element is smaller than edellmin
            edellmin = T[-i]    # Change edellmin to it
            RightList[-i] = edellmin  #Add the element to the list of "right" elements
        else: 
            RightList[-i]= edellmin  
    
        if T[i-1] > edellmax:  #Looping forwards, check if previous element if bigger than the max
            edellmax = T[i-1]  #change max to element
            LeftList[i-1] = edellmax #add element to the list of "left" elements
        else: 
            LeftList[i-1] = edellmax

    #print(LeftList)
    #print(RightList)
    for i in range(1, len(T)):
        if LeftList[i-1] < RightList[i]:    #if element at the leftlist (index-1) is smaller than the elemnt at rightlist
            count += 1                      #increase count
    
    return count



if __name__ == "__main__":
    print(split([1,2,3,4,5])) # 4
    print(split([5,4,3,2,1])) # 0
    print(split([2,1,2,5,7,6,9])) # 3
    print(split([1,2,3,1])) # 0