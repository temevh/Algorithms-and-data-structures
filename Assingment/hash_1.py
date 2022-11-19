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
        key = str(key)  # Make sure the given key is a string
        sum = 0  # Initializa sum to zero
        mul = 1  # Initialize mul to 1
        for i in range(len(str(key))):
            if (i % 4 == 0):  # Process the key 4 letters at a time
                mul = 1
            else:
                mul = mul * 256
            # Sum the ascii values of the key's characters, after multiplying with mul(tiplier)
            sum += ord(key[i]) * mul
        # End result is converted to the range 0 to M-1 using the hash table size and modulo operators
        return sum % self.SIZE

    def adder(self, key):
        h = self.hasher(key)  # Calculate hash
        key = str(key)  # Make sure key is string
        found = False  # Set found to false, found is used to check if key already exists, thus not allowing duplicates
        # By using enumerate, we can implement a counter in the loop (index)
        for index, element in enumerate(self.arr[h]):
            # If the key is already in the table
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = key
                found = True  # Set found to true
                break  # Do not add the key to the array
        if not found:  # Else if the loop does not encounter the key
            # Add the key to the given list at the array
            self.arr[h].append(key)

    def getter(self, key):
        key = str(key)
        spot = ""  # A placeholder variable for the potential info that is to be returned if the given key is found
        h = self.hasher(key)  # Calculate the hash
        # print("Etsittävä hash ", h)
        i = 0
        # loop through the linked list at the given index(hash)
        for element in self.arr[h]:
            # print(element)
            i += 1
            if element == key:  # If the current loop element matches the key to be searched for
                spot = "Key ["+str(key) + "] found\nKey hash: " + \
                    str(h) + "\nKey is the " + str(i) + \
                    ". element in list " + str(h+1)
                return spot  # Add information to the spot variable, return it
                # return "key found"
        else:
            print("key not found")  # If key not found, return "key not found"

    def delete(self, key):
        h = self.hasher(key)  # Calculate the hash
        # Loop through the through the linked list at the given index(hash) using enumerate, so we can keep trakc of the index, without needing a separate counter variable
        for index, element in enumerate(self.arr[h]):
            if element == key:  # If current element matches the key that is being looked for
                # Delete the key at the current index of the searched linked list
                del self.arr[h][index]
        return None

    def printTable(self):
        print("INDEX|ARRAY")
        for i in range(self.SIZE):
            print(i, str("   |"), self.arr[i])

    def addFromFile(self):  # Function to add words from a file to the hash table
        # Replace the first parameter with the file which the data should be read from
        file = open("kaikkisanat.txt", "r", encoding="utf-8")
        for line in file:
            # Pass the word from the file to the hash table, removing the newline(\n)
            self.adder(line.strip())

    # A test function to write the hash table to file, to make sure everything gets added
    def writeToFile(self):
        file = open("hashResult.txt", "w", encoding="utf-8")
        for element in self.arr:
            file.write(str(element)+"\n")
        file.close()
        print("hash table written to file hashResult.txt")

    # A function to write each hash table element on its own line to help with troubleshooting etc.
    def writeToFile2(self):
        file = open("hashResult.txt", "w", encoding="utf-8")
        for line in self.arr:
            for elem in line:
                file.write(str(elem)+"\n")

    # A function to write each hash table element in a sorted order to help with troubleshooting
    def writeOrdered(self):
        words = []
        file = open("hashOrdered.txt", "w", encoding="utf-8")
        for line in self.arr:
            for elem in line:
                words.append(elem)
        words.sort()
        for elem in words:
            file.write(str(elem)+"\n")


st = time.time()  # Initialize start time to system time
t = HashTable(100)  # Initialize hash table with size 10 000
# t.addFromFile()  # Add words from kaikkisanat.txt to the hash table
# Seach for the word "kirkkoväki" from the hash table
t.adder(1254121)
t.adder("testi")
t.adder("AAAAAAAAAA")
t.adder("R4PORPIHREHR")
t.adder("rthkke+e")
t.adder(15001)
t.adder("kirkkoväki")
print(t.getter("kirkkoväki"))
et = time.time()  # Initialize end time to system time
print("Total runtime: ", str(et-st)+"s")
t.writeToFile()  # Write the complete hash table to file
