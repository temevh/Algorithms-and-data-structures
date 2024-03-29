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

    def insert(self, key):
        h = self.hasher(key)
        x = self.find(key)
        if x == True:  #Check if key is already in the table
            return #If key already found, return, to not allow duplicates
        addTo = self.lists[h]
        node = Node(key)
        if addTo.head is None:
            addTo.head = node
            return
        last = addTo.head
        while last.next:
            last = last.next
        last.next = node

    def printTable(self):
        for i in range(self.tableSize):
            x = self.lists[i]
            itr = x.head
            strList = []
            while itr:
                strList.append(itr.data)
                itr = itr.next
            print(i, strList)
        print()
    
    def delete(self, key):
        h = self.hasher(key)
        delFrom = self.lists[h]
        temp = delFrom.head
        if temp is not None:
            if temp.data == key:
                delFrom.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None

    def find(self, key):
        h = self.hasher(key)
        findFrom = self.lists[h]
        temp = findFrom.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def findPrint(self, key):
        h = self.hasher(key)
        result = self.find(key)
        if result == True:
            print("KEY", key, "FOUND IN LIST" , h)
        elif result == False:
            print("KEY", key, "NOT FOUND")
        


ht = HashTable(3)
ht.insert("testi")
ht.insert("uhuh")
ht.insert(2141)
ht.insert("ääkkösiä")
ht.printTable()
ht.insert("testi")
ht.printTable()
ht.findPrint("testi")