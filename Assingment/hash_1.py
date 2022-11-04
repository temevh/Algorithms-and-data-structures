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
        self.SIZE = sizeOfArray+1  # Initialize the (fixed) size for the array
        # Fill the array with empty arrays to allow linked lists
        self.arr = [[] for i in range(self.SIZE)]

    def hasher(self, key):  # Calculate the hash
        v = 0  # Initialize the (v)alue to zero
        for c in str(key):  # Loop through the given key, which will be converted to string, to handle int and str cases
            v += ord(c)  # Calculate the sum of ascii values
        return v % self.SIZE  # Return the module of ascii sum and the size of the array

    def adder(self, key):
        h = self.hasher(key)  # Calculate the hash
        contains = False  # Set the variable contains to false, this will be used to see if the key already exists in the hash table
        # Loop through the linked list at the given index (from the hash value)
        for index in range(len(self.arr[h])):
            if self.arr[h][index] == key:  # If the key is already found in the linked list
                contains = True  # Set contains to true
                break  # Break out of the loop, do not add anything to the list/hash table
        # If the key is not found in the list/table (contains stays as False)
        if not contains:
            # Append the key to the appropriate linked list
            self.arr[h].append(key)

    def getter(self, key):
        spot = ""
        h = self.hasher(key)  # Calculate the hash
        # loop through the linked list at the given index(hash)
        for element in self.arr[h]:
            if element == key:  # If the key to be searched matches the current loop element
                # return key  # return key
                spot = ("Key found at list " + str(h))
                return spot
            else:  # Else if key not found
                return "Key not found"  # Return "key not found"

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
        file = open("sanatPieni.txt", "r")
        for line in file:
            # Pass the word from the file to the hash table, removing the newline(\n)
            self.adder(line.strip())

    def writeToFile(self):
        file = open("hashResult.txt", "w")
        for element in self.arr:
            file.write(str(element)+"\n")


t = HashTable(800)
t.addFromFile()
st = time.time()  # Implementing a timer to calculate the running time
print(t.getter("ajankohtainen"))
et = time.time()
time_taken = et-st
print("Execution time: ", time_taken, "seconds")
t.writeToFile()
