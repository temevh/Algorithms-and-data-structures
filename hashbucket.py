from pickle import NONE
import re


class HashBucket:
    def __init__(self, M, B):
        self.len = M
        self.bucket = B
        self.bucketlen = M//B
        self.overFlow = [None] * M
        self.arr = [None] * M

    def insert(self, data):
        i = HashBucket.hasher(data, self)
        for j in range((i*self.bucketlen),((i+1)*self.bucketlen)):
            if self.arr[j] == data:
                return
            elif self.arr[j] == None or self.arr[j] == -1:
                self.arr[j] = data
                return
        for j in range(0, self.bucketlen):
            if self.overFlow[j] == data:
                return
            elif self.overFlow[j] == -1 or self.overFlow[j] == None:
                self.overFlow[j] = data
                return

    def hasher(data, self):
        sum = 0
        i = 0
        for i in range(len(data)):
            sum += int(ord(data[i]))
        return sum % self.bucket

    def print(self):
        ar = []
        for x in self.arr:
            if x != None and x != -1:
                ar.append(x)
        for y in self.overFlow:
            if y != None and y != -1:
                ar.append(y)
        print(*ar, sep=' ')

    def delete(self, data):
        i = HashBucket.hasher(data, self)
        for j in range((i*self.bucketlen),((i+1)*self.bucketlen)):
            if self.arr[j] == data:
                self.arr[j] = -1
                return
            elif self.arr[j] == None:
                break
        
        for j in range(0,self.bucketlen-1):
            if self.overFlow[j] == data:
                self.overFlow[j] = -1
                return
            elif self.overFlow[i] == None:
                break

if __name__ == "__main__":
    table = HashBucket(8, 4)
    table.insert("BM40A1500")
    table.insert("fOo")
    table.insert("123")
    table.insert("Bar1")
    table.insert("10aaaa1")
    table.insert("BM40A1500")
    table.print()   # fOo BM40A1500 123 Bar1 10aaaa1
    table.delete("fOo")
    table.delete("Some arbitary string which is not in the table")
    table.delete("123")
    table.print()   # BM40A1500 Bar1 10aaaa1


