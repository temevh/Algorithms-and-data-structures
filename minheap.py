class MinHeap:
    


if __name__ == "__main__":
    items = [4, 8, 6, 5, 1, 2, 3]
    heap = MinHeap()
    [heap.push(key) for key in items]
    heap.print()        # 1 4 2 8 5 6 3 
    print(heap.pop())   # 1
    heap.print()        # 2 4 3 8 5 6 