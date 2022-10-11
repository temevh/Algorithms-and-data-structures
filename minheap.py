from multiprocessing.resource_sharer import stop


class MinHeap:

    def __init__(self):
        self.size = 0
        self.heap_list = [0]

    def shift_up(self, i):
        Stop = False
        while (i // 2 > 0) and Stop == False:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
                Stop = True
            i = i // 2

    def push(self, key):
        self.heap_list.append(key)
        self.size += 1
        self.shift_up(self.size)

    def print(self):
        

    


if __name__ == "__main__":
    items = [4, 8, 6, 5, 1, 2, 3]
    heap = MinHeap()
    [heap.push(key) for key in items]
    heap.print()        # 1 4 2 8 5 6 3 
    print(heap.pop())   # 1
    heap.print()        # 2 4 3 8 5 6 