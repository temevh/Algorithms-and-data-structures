# BM40A1500 Algorithms and data structures
# Practical assignment 1, Implementing a hash table
# Collision will be handled with LINEAR PROBING
# Search will return the spot on the hash table, where the given key is stored at
# Average Case O(1)
# Worst case O(n) if all keys have the same hash, essentially the program goes through a linked list, and the complexity for list look-ups is O(n)
# Duplicates not allowed

import time


class HashTable:
    def __init__(self, sizeOfArray) -> None:
        self.SIZE = sizeOfArray  # Initialize the (fixed) size for the array
        # Fill the array with empty arrays to allow linked lists
        self.arr = [[] for i in range(self.SIZE)]

    def hasher(self, key):  # Calculate hash using string folding
        # key = str(key)  # Make sure the given key is a string
        hSum = 0  # Initializa sum to zero
        mul = 1  # Initialize mul to 1
        if type(key) == int:
            for i in range(key):
                hSum = i * mul * 256
            return hSum % self.SIZE
        else:
            # print("string")
            for i in range(len(str(key))):
                if (i % 4 == 0):  # Process the key 4 letters at a time
                    mul = 1
                else:
                    mul = mul * 256
                # Sum the ascii values of the key's characters, after multiplying with mul(tiplier)
                hSum += ord(key[i]) * mul
        # End result is converted to the range 0 to M-1 using the hash table size and modulo operators
            return hSum % self.SIZE

    def adder(self, key):
        h = self.hasher(key)  # Calculate hash
        # key = str(key)  # Make sure key is string
        found = False  # Set found to false, found is used to check if key already exists, thus not allowing duplicates
        # By using enumerate, we can implement a counter in the loop (index)
        # for index, element in enumerate(self.arr[h]):
        #print("element", element)
        # If the key is already in the table
        index = 0
        for elem in self.arr[h]:
            # if len(element) == 2 and element[0] == key:
            if elem == key:
                self.arr[h][index] = key
                found = True  # Set found to true
                break  # Do not add the key to the array
            else:
                index += 1
        if not found:  # Else if the loop does not encounter the key
            # Add the key to the given list at the array
            self.arr[h].append(key)
        self.printTable()

    def getter(self, key):
        #key = str(key)
        spot = ""  # A placeholder variable for the potential info that is to be returned if the given key is found
        h = self.hasher(key)  # Calculate the hash
        i = 0
        # loop through the linked list at the given index(hash)
        for element in self.arr[h]:
            i += 1
            if element == key:  # If the current loop element matches the key to be searched for
                spot = "Key " + str(key) + " found\nKey hash: " + \
                    str(h) + "\nKey is the " + str(i) + \
                    ". element in list " + str(h) + "\n"
                print(spot)
                return None  # Add information to the spot variable, return it
        else:
            # If key not found, return "key not found"
            print("key " + str(key) + " not found\n")

    def delete(self, key):
        h = self.hasher(key)  # Calculate the hash
        #key = str(key)
        # Loop through the through the linked list at the given index(hash) using enumerate, so we can keep trakc of the index, without needing a separate counter variable
        for index, element in enumerate(self.arr[h]):
            if element == key:  # If current element matches the key that is being looked for
                # Delete the key at the current index of the searched linked list
                del self.arr[h][index]
        return None

    def printTable(self):
        print("INDEX|ARRAY")  # Create a grid with the hearders INDEX and ARRAY
        print("-----|-----------")
        for i in range(self.SIZE):
            print(i, str("   |"), self.arr[i])  # Add the current value
        print("-----------------")


t = HashTable(3)  # Initialize hash table size to 3
t.printTable()  # Print the hash table
st = time.time()  # Set start time
t.adder(12)  # Add value 12 to the hash table
et = time.time()  # Get end time
# Runtime for adding a value is start time - end time
print("Time to add new value to table:", et-st)

t.adder('hashtable')  # Add "hashtable"
t.adder(1234)  # Add 1234
t.adder(4328989)  # Add 4328989
t.adder('BM40A1500')  # Add "BM40A1500"
t.adder(-12456)  # Add -12456
t.adder("aaaabbbbcccc")  # Add "aaaabbbbcccc"

st = time.time()  # Set start time
t.getter(-12456)  # Get value -12456 from hash table
et = time.time()  # Set end time
# Runtime for getting a value is start time - end time
print("Time to get a value to table:", et-st, "\n")
t.getter("hashtable")  # Get value "hashtable" from hash table
t.getter(1235)  # Try to get a non-existing value from the table

st = time.time()  # Set start time
t.delete(1234)  # Delete value 1234 from the hash table
et = time.time()  # Set end time
# Runtime for deleting a value is start time - end time
print("Time to remove a value from table:", et-st, "\n")
t.delete('BM40A1500')  # Delete "BM40A1500" from hash table
t.delete("aaaabbbbcccc")

t.printTable()  # Print the final hash table
