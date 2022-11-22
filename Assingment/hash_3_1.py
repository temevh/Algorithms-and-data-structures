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
        key = str(key)  # Make sure key is string
        found = False  # Set found to false, found is used to check if key already exists, thus not allowing duplicates
        # By using enumerate, we can implement a counter in the loop (index)
        for index, element in enumerate(self.arr[h]):
            # If the length of the element is 2 and the current element is key
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = key
                found = True  # Set found to true
                break  # Do not add the key to the array
        if not found:  # Else if the loop does not encounter the key
            # Add the key to the given list at the array
            self.arr[h].append(key)

    def addFromFile(self):  # Function to add words from a file to the hash table
        # Replace the first parameter with the file which the data should be read from
        file = open("words_alpha.txt", "r", encoding="utf-8")
        for line in file:
            # Pass the word from the file to the hash table, removing the newline(\n)
            self.adder(line.strip())

    def getter(self, key):
        h = self.hasher(key)  # Calculate the hash
        # loop through the linked list at the given index(hash)
        for element in self.arr[h]:
            if element == key:
                return 1  # If key found, return 1
        else:
            # If key not found, return 0
            return 0

    def comparer(self):
        matchList = []  # Initialize an empty list to contain the matching words
        # Open file kaikkisanat.txt
        file = open("kaikkisanat.txt", "r", encoding="utf-8")
        matches = 0
        for line in file:
            if self.getter(line.strip()) == 1:
                matches += 1
                matchList.append(line.strip())
        #file2 = open("matches.txt", "w", encoding="utf-8")
        # for item in matches:
        #    file2.write(str(item)+"\n")
        print("MATCHING WORDS:", matches)

    # Function to write (append) the results of runtimes to a file
    def writeToFile(self, init, add, comp, runtime_total):
        file = open("compareRuntimeHash100k2.txt", "a", encoding="utf-8")
        file.write("ACTION       |   RUNTIME(s)\n")
        file.write("-------------|----------------\n")
        file.write("Table init   |"+str("%.8f" % init)+"\n")
        file.write("Add to table |"+str("%.8f" % add)+"\n")
        file.write("Compare      |"+str("%.8f" % comp)+"\n")
        file.write("-------------|----------------\n")
        file.write("Total runtime: "+str("%.8f" % runtime_total))
        file.write("\nTable size: " + str(self.SIZE) + "\n")


runtime_total = 0  # Set runtime_total to 0

st = time.time()
t = HashTable(100000)  # Initialize hash table for size 100000
et = time.time()
init = et-st  # Calculate the time it takes to initialize the hash table
runtime_total += et-st  # Add time to total runtime

st = time.time()
t.addFromFile()
et = time.time()
add = et-st  # Calculate the time it takes to add words from the file "words_alpha.txt" to the hash table
runtime_total += et-st  # Add time to total runtime

st = time.time()
t.comparer()
et = time.time()
comp = et-st  # Calculate the time it takes to compare how many matching words are in words_alpha.txt and kaikkisanat.txt
runtime_total += et-st  # Add the time to total runtime

print("ACTION       |   RUNTIME(s)")
print("-------------|----------------")
print("Table init   |", "%.8f" % init)
print("Add to table |", "%.8f" % add)
print("Compare      |", "%.8f" % comp)
print("-------------|----------------")
print("Total runtime: ", "%.8f" % runtime_total)
print("Table size:", t.SIZE)
#t.writeToFile(init, add, comp, runtime_total)
