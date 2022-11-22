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
        #key = str(key)
        spot = ""  # A placeholder variable for the potential info that is to be returned if the given key is found
        h = self.hasher(key)  # Calculate the hash
        #print("Etsittävä hash ", h)
        i = 0
        # loop through the linked list at the given index(hash)
        for element in self.arr[h]:
            i += 1
            if element == key:  # If the current loop element matches the key to be searched for
                spot = "Key ["+str(key) + "] found\nKey hash: " + \
                    str(h) + "\nKey is the " + str(i) + \
                    ". element in list " + str(h+1) + "\n"
                print(spot)
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
        print("INDEX|ARRAY")  # Create a grid with the hearders INDEX and ARRAY
        print("-----|-----------")
        for i in range(self.SIZE):
            print(i, str("   |"), self.arr[i])  # Add the current value
        print("-----------------")

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


t = HashTable(5)  # Initialize hash table with size 5
t.adder("test")  # Add words and integers to hash table
t.adder(1234)
t.adder("AAAA")
t.adder("BBBB")
t.adder(-12942)
t.adder(420)
t.adder("BM40A1500")

t.getter(-12942)  # Seach the hash table for -12942, "test" and "BM40A1500"
t.getter("test")
t.getter("BM40A1500")

t.delete("test")  # Delete test and -12942
t.delete(-12942)

t.printTable()
