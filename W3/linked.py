from operator import index
from traceback import print_tb


class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        #node = Node(data, self.head)
        #self.head = node
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = node

    def print(self):
        itr = self.head 
        llstr = ''
        while itr:
            llstr += str(itr.data)
            if itr.next:
                llstr += " -> "
            itr = itr.next

        print(llstr)

    def insert_at_head(self, data):
        node = Node(data, self.head)
        self.head = node

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        
        return count

    def delete(self, position):
        if position<0 or position >= self.get_length():
            return

        if position == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == position - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1


    def insert(self, data, index):
        if index == 0:
            node = Node(data, self.head)
            self.head = node
            #self.insert_at_head(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def index(self, tofind):
        current = self.head
        count = 0
        while current != None:
            if current.data == tofind:
                return count
            current = current.next
            count += 1
        return -1
    

if __name__ == "__main__":
    L = LinkedList()
    L.append(2)
    L.append(3)
    L.append(1)
    L.append(4)
    L.print()
    L.insert(4,3)
    L.insert(1,0)
    L.insert(3,2)
    L.insert(2,1)
    L.print()
    print(L.index(0))
    print(L.index(3))
    print(L.index(4))
    print(L.index(2))
    L.delete(0)
    L.delete(1)
    L.delete(4)
    L.delete(5)
    L.print()

