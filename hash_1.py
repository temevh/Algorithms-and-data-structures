# BM40A1500 Algorithms and data structures
# Practical assignment 1, Implementing a hash table
# Collision will be handled with LINEAR PROBING
class HashTable:
    def __init__(self) -> None:
        self.SIZE = 10  # Initialize the (fixed) size for the array
        # Fill the array with NONE elements
        self.arr = [[] for i in range(self.SIZE)]

    def hasher(self, key):  # Calculate the hash
        v = 0  # Initialize the (v)alue to zero
        for c in str(key):  # Loop through the given key, which will be converted to string, to handle int and str cases
            v += ord(c)  # Calculate the sum of ascii values
        return v % self.SIZE  # Return the module of ascii sum and the size of the array

    def adder(self, key):
        h = self.hasher(key)

    def getter(self, key):
        h = self.hasher(key)
        return self.arr[h]

    def delete(self, key):
        h = self.hasher(key)
        self.arr[h] = None


t = HashTable()
print(t.arr)
