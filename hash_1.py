# BM40A1500 Algorithms and data structures
# Practical assignment 1, Implementing a hash table
class HashTable:
    def __init__(self) -> None:
        self.SIZE = 100
        self.arr = [None for i in range(self.SIZE)]

    def hasher(self, key):
        v = 0
        for c in str(key):
            h += ord(c)
        return h % self.SIZE
