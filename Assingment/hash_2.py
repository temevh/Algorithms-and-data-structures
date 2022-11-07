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
                spot = "Key found\nKey hash: " + \
                    str(h) + "\nKey is the " + str(i) + \
                    " nth element in list " + str(h)
                return spot  # Add information to the spot variable, return it
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
        print("-----|-----------")
        for i in range(self.SIZE):
            print(i, str("   |"), self.arr[i])
        print("-----------------")

    # A test function to write the hash table to file, to make sure everything gets added

    def writeToFile(self):
        file = open("hashResult.txt", "w", encoding="utf-8")
        file.write("INDEX|ARRAY\n")
        file.write("-----|-----------\n")
        for i in range(self.SIZE):
            file.write(str(i) + str("    | ")+str(self.arr[i])+"\n")
        file.write("-----------------")


t = HashTable(3)
t.adder(12)
t.adder('hashtable')
t.adder(1234)
t.adder(4328989)
t.adder('BM40A1500')
t.adder(-12456)
t.adder("aaaabbbbcccc")
t.adder("Leevi on tyhmä")
t.delete('BM40A1500')
t.delete(1234)
t.delete("aaaabbbbcccc")
t.printTable()
t.writeToFile()