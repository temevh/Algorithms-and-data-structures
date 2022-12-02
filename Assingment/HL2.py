import time


class Node:
    def __init__(self, data, next=None):
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
            # for i in range(key):
            #    hSum = i * mul * 12
            print((key * 111) % self.tableSize)
            return (key * 111) % self.tableSize
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
        h = self.hasher(key)  # Calculate hash
        addTo = self.lists[h]  # Choose which list the key should be added to
        node = Node(key)  # Give the key as data for node
        if addTo.head is None:  # If the head of the linked list is empty
            addTo.head = node  # Make the current key/node head
            # self.printTable()
            return
        last = addTo.head  # ITerate through the linked list
        while last.next:  # While iterator has a next node
            last = last.next  # Go to next
        last.next = node  # When the node without next is reached the node is set to that
        # self.printTable()

    def printTable(self):
        for i in range(self.tableSize):
            x = self.lists[i]  # x is the current list to print
            itr = x.head  # Set iterator to the head of the current list
            strList = []  # Initiate an empty array for the list elements
            while itr:  # While list elements exist
                strList.append(itr.data)  # append list element to strList
                itr = itr.next  # Move to next element
            print(i, strList)  # Print the current index and the element
        print()

    def find(self, key):
        h = self.hasher(key)
        findFrom = self.lists[h]
        temp = findFrom.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def search(self, key):
        h = self.hasher(key)  # Determine the hash
        result = self.find(key)  # Get result from find function
        if result == True:  # If key exists in list
            if type(key) == int:
                print("KEY", key, "FOUND IN LIST", h, "\n")  # Inform the user
            else:
                print("KEY '" + str(key) + "' FOUND IN LIST", h, "\n")
        elif result == False:  # Else the key does not exist
            if type(key) == int:
                print("KEY", key, "NOT FOUND", "\n")  # Inform the user
            else:
                print("KEY '" + str(key) + "' NOT FOUND", "\n")

    def delete(self, key):
        h = self.hasher(key)
        delFrom = self.lists[h]
        temp = delFrom.head
        if temp is not None:
            if temp.data == key:
                delFrom.head = temp.next
                temp = None
                print("REMOVED KEY ", key, "\n")
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
        print("REMOVED KEY ", key, "\n")


ht = HashTable(3)

st = time.time()
ht.insert(12)
ht.insert("hashtable")
ht.insert(1234)
ht.insert("BM40A1500")
ht.insert(-12456)
ht.insert("aaaabbbbcccc")
ht.insert(151125125125)
et = time.time()
# ht.printTable()


# ht.search(-12456)
# ht.search("hashtable")
# ht.search(1235)

# ht.delete("BM40A1500")
# ht.delete(1234)
# ht.delete("aaaabbbbcccc")

# ht.printTable()
print("TIME TO ADD", (et-st)/6)
