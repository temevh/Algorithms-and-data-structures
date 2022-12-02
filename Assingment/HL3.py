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
        hSum = 0  # Initializa sum to zero
        mul = 1  # Initialize mul to 1
        if type(key) == int:  # If the type of the key is int
            # Return the multiplication of key 2654435761 and modulo of tablesize
            return (key * 2654435761) % self.tableSize
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
        h = self.hasher(key)  # Calculate the hash
        if self.find(key):  # If key already exists in the hash table
            return  # Exit the function
        addTo = self.lists[h]  # Choose which list the key should be added to
        node = Node(key)  # Give node the key as data
        if addTo.head is None:  # If the head of the linked list is empty
            addTo.head = node  # Make the current key/node head
            return
        last = addTo.head  # ITerate through the linked list
        while last.next:  # While iterator has a next node
            last = last.next  # Go to next
        last.next = node  # When the node without next is reached the node is set to that

    def find(self, key):
        h = self.hasher(key)  # Calculate the hash
        findFrom = self.lists[h]  # Choose which list to find the key from
        temp = findFrom.head  # Set temp to head of chosen list
        while temp:  # While temp exists
            if temp.data == key:  # If the data at current node equals to the key to be searched
                return True  # If key found, return true
            temp = temp.next  # Go to next node if data does not match key
        return False  # If key not found, return false

    def addFromFile(self):
        file = open("words_alpha.txt", "r", encoding="UTF-8")  # Open file
        for line in file:  # Go through the file one line at a time
            # Insert the line to hash table without newline
            self.insert(line.strip())
        file.close()  # Close the file

    def compare(self):
        matches = 0  # Set the amount of matches to 0
        file = open("kaikkisanat.txt", "r", encoding="UTF-8")  # Open file
        for line in file:  # Go through the file one line at a time
            # If the key can be found from the hash table (find = True)
            if self.find(line.strip()):
                matches += 1  # Increase matches

        print("MATCHING WORDS", matches)
        file.close()

    def minMax(self):  # Auxiliary function to determine the max and min lists
        wo = 0
        wolist = 0
        be = 15151515151
        belist = 0
        for i in range(self.tableSize):
            temp = self.lists[i].head
            count = 0
            while (temp):
                count += 1
                temp = temp.next
            if count > wo:
                wo = count
                wolist = i
            elif count < wo:
                be = count
                belist = i
        print("Worst list", wolist, "with ", wo, "elements")
        print(f'Best list {belist} with {be} elements')


total = 0
add, comp, init = 0, 0, 0

st = time.time()
ht = HashTable(10_000)
et = time.time()
init = et - st

st = time.time()
ht.addFromFile()
et = time.time()
add = et-st

st = time.time()
ht.compare()
et = time.time()
comp = et-st

runtime_total = init+add+comp
print("ACTION       |   RUNTIME(s)")
print("-------------|----------------")
print("init. table  |", "%.8f" % init)
print("Add to table |", "%.8f" % add)
print("Compare      |", "%.8f" % comp)
print("-------------|----------------")
print("Total runtime: ", "%.8f" % runtime_total)

# ht.printTable()
# ht.minMax()
