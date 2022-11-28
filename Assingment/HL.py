class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
class HashTable:
    def __init__(self, M) -> None:
        self.tableSize = M
        self.lists = [LinkedList() for j in range(self.tableSize)]


    def hasher(self, key):  # Calculate hash using string folding
        # key = str(key)  # Make sure the given key is a string
        hSum = 0  # Initializa sum to zero
        mul = 1  # Initialize mul to 1
        if type(key) == int:
            for i in range(key):
                hSum = i * mul * 256
            return hSum % self.tableSize
        else:
            for i in range(len(str(key))):
                if (i % 4 == 0):  # Process the key 4 letters at a time
                    mul = 1
                else:
                    mul = mul * 256
                # Sum the ascii values of the key's characters, after multiplying with mul(tiplier)
                hSum += ord(key[i]) * mul
        # End result is converted to the range 0 to M-1 using the hash table size and modulo operators
            return hSum % self.tableSize

    #Function to insert keys to the hash table/linked list
    def insert(self, key):
        h = self.hasher(key)   #Calculate the hash for the key, store in h
        if self.find(key):  #If the key is already stored in the hash table
            return #Exit the insert function
        addTo = self.lists[h] #Determine which linked list the key should be added to
        node = Node(key) #Create a Node class object with key
        if addTo.head is None: #If the head of the linked list is None
            addTo.head = node  #Make the key the head
            return #Exit function
        last = addTo.head #Else if head is not empty set last to head 
        while last.next: #Cycle through list elements 
            last = last.next 
        last.next = node #When there is no more elements to cycle through, add the key

    def printTable(self):
        for i in range(self.tableSize): #Initialize the loop to go through all of the linked lists
            x = self.lists[i] #Current list chosen with index
            itr = x.head #initialize itr to head of current list
            strList = [] #Empty array for list elements
            #print("INDEX   LIST")
            while itr: #While iterator has data
                strList.append(itr.data) #Append the data to strList 
                itr = itr.next #Go to next element
            print(i, strList) #Print the list with iterator index 
        print()
    
    def delete(self, key):
        h = self.hasher(key)  #Determine the hash
        delFrom = self.lists[h] #Choose the correct list to delete from
        temp = delFrom.head #Set temp to head of the chosen list
        if temp is not None: #If the head is not empty
            if temp.data == key: #If the head data matches the desired key
                delFrom.head = temp.next #Set head to the next key from temp ("skip over the key to delete")
                temp = None #Set temp to None
                return #Exit function
        while temp is not None: #While an element exists in temp 
            if temp.data == key: #If temp.data is the desired key
                break #Stop the loop
            prev = temp #Set previous to temp 
            temp = temp.next #Temp is the next element
        if temp == None: #If there is no next element from temp (desired key is the last element)
            return #Exit the function
        prev.next = temp.next #Set prev.next to temp.next
        temp = None #Set temp to None

    def find(self, key):
        h = self.hasher(key) #Determine the hash
        findFrom = self.lists[h] #Choose which list to find from 
        temp = findFrom.head #Set temp to head of chosen list
        while temp: #While an element exists 
            if temp.data == key: #If current data matches the key
                return True #Return true (key can be found)
            temp = temp.next #Move temp one element forward
        return False #If whole list has been examined without finding element, its safe to assume that 
        #It does not exist and False will be returned to signify this.

    def findPrint(self, key):
        h = self.hasher(key) #Determine the hash
        result = self.find(key) #Get result from find function
        if result == True: #If key exists in list
            print("KEY", key, "FOUND IN LIST" , h) #Inform the user
        elif result == False: #Else the key does not exist
            print("KEY", key, "NOT FOUND") #Inform the user
        


ht = HashTable(3)
ht.insert("testi")
ht.insert("testi")
ht.printTable()