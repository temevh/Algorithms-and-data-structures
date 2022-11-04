# BM40A1500 Algorithms and data structures
# Practical assignment 1, Implementing a hash table
# Collision will be handled with LINEAR PROBING
# Search will return the spot on the hash table, where the given key is stored at
# Average Case O(1)
# Worst case O(n) if all keys have the same hash, essentially the program goes through a linked list, and the complexity for list look-ups is O(n)
class HashTable:
    def __init__(self) -> None:
        self.SIZE = 10  # Initialize the (fixed) size for the array
        # Fill the array with empty arrays to allow linked lists
        self.arr = [[] for i in range(self.SIZE)]

    def hasher(self, key):  # Calculate the hash
        v = 0  # Initialize the (v)alue to zero
        for c in str(key):  # Loop through the given key, which will be converted to string, to handle int and str cases
            v += ord(c)  # Calculate the sum of ascii values
        return v % self.SIZE  # Return the module of ascii sum and the size of the array

    def adder(self, key):
        h = self.hasher(key)
        #print("adder h", h)
        contains = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = key
                contains = True
                break
        if not contains:
            self.arr[h].append(key)

    def getter(self, key):
        h = self.hasher(key)
        for element in self.arr[h]:
            if element[0] == key:
                return key
        return self.arr[h]

    def delete(self, key):
        h = self.hasher(key)
        for index, element in enumerate(self.arr[h]):
            if element == key:
                del self.arr[h][element]
        return None

    def printTable(self):
        print(self.arr)


t = HashTable()
t.adder("testi2")
t.adder(12512512)
t.printTable()
t.delete("testi2")
t.printTable()
