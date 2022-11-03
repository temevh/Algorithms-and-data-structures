# BM40A1500 Algorithms and data structures
# Practical assignment 1, Implementing a hash table
# Collision will be handled with LINEAR PROBING
class HashTable:
    def __init__(self) -> None:
        self.SIZE = 10
        # Filling the array with NONE using list comprehension
        self.arr = [None for i in range(self.SIZE)]

    def hasher(self, key):
        v = 0
        for c in str(key):
            v += ord(c)
        return v % self.SIZE

    def adder(self, key):
        h = self.hasher(key)
        self.arr[h] = key

    def getter(self, key):
        h = self.hasher(key)
        return self.arr[h]

    def delete(self, key):
        h = self.hasher(key)
        self.arr[h] = None


t = HashTable()
print(t.arr)
t.adder("Teemu H")
print(t.arr)
t.adder(12451215)
print(t.arr)
print(t.getter("Teemu H"))
t.delete("Teemu H")
print(t.arr)
