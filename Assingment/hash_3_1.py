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
            # If the length of the element is 2 and the current element is key
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = key
                found = True  # Set found to true
                break  # Do not add the key to the array
        if not found:  # Else if the loop does not encounter the key
            # Add the key to the given list at the array
            self.arr[h].append(key)
        # self.printTable()

    def getter(self, key):
        key = str(key)
        spot = ""  # A placeholder variable for the potential info that is to be returned if the given key is found
        h = self.hasher(key)  # Calculate the hash
        i = 0
        # loop through the linked list at the given index(hash)
        for element in self.arr[h]:
            i += 1
            if element == key:  # If the current loop element matches the key to be searched for
                return 1  # Add information to the spot variable, return it
        else:
            # If key not found, return "key not found"
            return 0

    def addFromFile(self):  # Function to add words from a file to the hash table
        # Replace the first parameter with the file which the data should be read from
        file = open("words_alpha.txt", "r", encoding="utf-8")
        for line in file:
            # Pass the word from the file to the hash table, removing the newline(\n)
            self.adder(line.strip())

    def printTable(self):
        print("INDEX|ARRAY")  # Create a grid with the hearders INDEX and ARRAY
        print("-----|-----------")
        for i in range(self.SIZE):
            print(i, str("   |"), self.arr[i])  # Add the current value
        print("-----------------")

    def writeOrdered(self):
        words = []
        file = open("hashOrdered.txt", "w", encoding="utf-8")
        for line in self.arr:
            for elem in line:
                words.append(elem)
        words.sort()
        for elem in words:
            file.write(str(elem)+"\n")

    def comparer(self):
        samat = []
        file = open("kaikkisanat.txt", "r", encoding="utf-8")
        matches = 0
        for line in file:
            # print(line.strip())
            if self.getter(line.strip()) == 1:
                matches += 1
                samat.append(line.strip())
                # print(samat)
            # time.sleep(0.1)
        file2 = open("matches.txt", "w", encoding="utf-8")
        for item in samat:
            file2.write(str(item)+"\n")
        print("Matches:", matches)


runtime_total = 0
st = time.time()
t = HashTable(10000)
et = time.time()
init = et-st
runtime_total += et-st
st = time.time()
t.addFromFile()
et = time.time()
add = et-st
runtime_total += et-st
st = time.time()
t.comparer()
et = time.time()
comp = et-st
runtime_total += et-st
print("Action       |   Runtime")
print("-------------|----------------")
print("table init   |", "%.8f" % init)
print("add to table |", "%.8f" % add)
print("compare      |", "%.8f" % comp)
print("-------------|----------------")
print("Total runtime: ", "%.8f" % runtime_total)
