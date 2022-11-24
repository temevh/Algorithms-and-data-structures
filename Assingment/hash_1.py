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


t = HashTable(3)  # Initialize hash table with size 5
t.adder(4328989)
t.adder(4328989)

t.adder("test")  # Add words and integers to hash table
t.adder("testi123")
t.adder("BBBB")
t.adder(-12942)
t.adder(420)
t.adder("kush")


t.getter(-12942)  # Seach the hash table for -12942, "test" and "BM40A1500"
t.getter("test")
t.getter("BM40A1500")

t.delete("test")  # Delete test and -12942
t.delete(-12942)

t.printTable()
