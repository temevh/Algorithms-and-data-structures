class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
class hashTable:
    def __init__(self, size) -> None:
        self.tableSize = size
        self.lists = [Node(None) for i in range(self.tableSize)]

    def adder(self, data):
        h = self.hasher(data)

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

                

class LinkedList:
    def __init__(self):
        self.head = None
        self


    

if __name__ == "__main__":
    ht = hashTable(3)

