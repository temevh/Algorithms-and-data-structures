class MinHeap:

    def __init__(self):
        self.size = 0
        self.heap = []

    def push(self, data):
        self.heap.append(data)
        self.heap_up()

    def heap_up(self):
        child = len(self.heap) - 1
        parent = (child - 1) // 2
        while self.heap[child] < self.heap[parent] and child != 0:
            self.heap[child], self.heap[parent] = self.heap[parent], self.heap[child]
            child = parent
            parent = (child - 1) // 2

    def print(self):
        for i in self.heap:
            print(str(i)+" ", end="")
        print()

    def pop(self):
        if not self.heap:
            return False
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        data = self.heap.pop()
        self.heap_down()
        return data

    def heap_down(self):
        i = 0
        while (2*i+1) < len(self.heap):
            min = 2*i+1
            if (2*i+2) < len(self.heap) and self.heap[2*i+2] < self.heap[2*i+1]:
                min = 2*i+2
            if self.heap[min] > self.heap[i]:
                return
            self.heap[min], self.heap[i] = self.heap[i], self.heap[min]
            i = min

if __name__ == "__main__":
    items = [4, 8, 6, 5, 1, 2, 3]
    heap = MinHeap()
    [heap.push(key) for key in items]
    heap.print()        # 1 4 2 8 5 6 3 
    print(heap.pop())   # 1
    heap.print()        # 2 4 3 8 5 6 