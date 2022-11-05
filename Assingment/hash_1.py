# BM40A1500 Algorithms and data structures
# Practical assignment 1, Implementing a hash table
# Collision will be handled with LINEAR PROBING
# Search will return the spot on the hash table, where the given key is stored at
# Average Case O(1)
# Worst case O(n) if all keys have the same hash, essentially the program goes through a linked list, and the complexity for list look-ups is O(n)
# Duplicates not allowed
# Using % self.size as the hasher, with large files most of the linked lists are left empty

import time


class HashTable:
    def __init__(self, sizeOfArray) -> None:
        self.SIZE = sizeOfArray  # Initialize the (fixed) size for the array
        # Fill the array with empty arrays to allow linked lists
        self.arr = [[] for i in range(self.SIZE)]

    def hasher(self, key):  # Calculate hash using string folding
        key = str(key)
        sum = 0
        mul = 1
        for i in range(len(str(key))):
            if (i % 4 == 0):
                mul = 1
            else:
                mul = mul * 256
            sum += ord(key[i]) * mul
        return sum % self.SIZE

    def adder(self, key):
        h = self.hasher(key)
        key = str(key)
        # print("hastattu", h)
        found = False
        for index, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = key
                found = True
                break
        if not found:
            self.arr[h].append(key)

    def getter(self, key):
        key = str(key)
        spot = ""
        h = self.hasher(key)  # Calculate the hash
        # loop through the linked list at the given index(hash)
        # for element in self.arr[h]:
        i = 0
        for element in self.arr[h]:
            i += 1
            if element == key:
                spot = "Key found\nKey hash: " + \
                    str(h) + "\nKey is the " + str(i) + \
                    " nth element in list " + str(h)
                return spot
        else:
            print("key not found")

    def delete(self, key):
        h = self.hasher(key)  # Calculate the hash
        # Loop through the through the linked list at the given index(hash) using enumerate, so we can keep trakc of the index, without needing a separate counter variable
        for index, element in enumerate(self.arr[h]):
            if element == key:  # If current element matches the key that is being looked for
                # Delete the key at the current index of the searched linked list
                del self.arr[h][index]
        return None

    def printTable(self):
        print(self.arr)  # Print the hash table

    def addFromFile(self):  # Function to add words from a file to the hash table
        # Replace the first parameter with the file which the data should be read from
        file = open("kaikkisanat.txt", "r", encoding="utf-8")
        for line in file:
            # Pass the word from the file to the hash table, removing the newline(\n)
            self.adder(line.strip())

    def writeToFile(self):
        file = open("hashResult.txt", "w", encoding="utf-8")
        for element in self.arr:
            file.write(str(element)+"\n")


t = HashTable(10)
t.adder(35355125)
t.adder(141)
t.adder("teesti")
t.adder("auton moottori")
t.adder("tietokone")
t.adder(11115111111)
t.writeToFile()
print(t.getter(141))
print(t.getter("teesti"))
print(t.getter("tietokone"))
