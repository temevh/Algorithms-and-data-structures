# Based on lecture material and openDSA 19.3
# If starting vertex is 1, no neighbors

class Graph:
    def __init__(self, grid):
        self.matrix = grid
        self.vertex_count = len(grid)
        self.visited = [False] * len(self.matrix)
        self.stack = []
        self.D = []

    def df_print(self, v):
        self.preVisit(v)
        self.visited[v] = True
        self.D.append(v)
        nList = self.neighbors(v)
        for i in range(len(nList)):
            if self.visited[nList[i]] != True:
                self.df_print(nList[i])
        self.postVisit(v)
        if len(self.stack) == 0:
            replace = [False] * len(self.matrix)
            self.visited = replace

    def preVisit(self, v):
        print(str(v)+" ", end="")
        # self.stack.append(v)
        self.stack.insert(0, v)

    def postVisit(self, v):
        self.stack.remove(v)

    def bf_print(self, v):
        self.toPrint = []
        Q = []
        Q.insert(0, v)  # Enqueue
        self.visited[v] = True
        while len(Q) > 0:
            v = Q.pop()  # Dequeue
            self.preVisit(v)
            nList = self.neighbors(v)
            for i in range(len(nList)):
                if self.visited[nList[i]] != True:
                    self.visited[nList[i]] = True
                    Q.insert(0, nList[i])  # Enqueue
        self.postVisit(v)
        if len(self.stack) == 0:
            replace = [False] * len(self.matrix)
            self.visited = replace

    def neighbors(self, v):
        nList = []
        for i in range(self.vertex_count):
            if self.matrix[v][i] != 0:
                nList.append(i)
        return nList

    def weight(self, a, b):
        if self.matrix[a][b] != 0:
            return (self.matrix[a][b])
        else:
            return -1


if __name__ == "__main__":

    matrix = [
        #    0  1  2  3  4  5
        [0, 0, 7, 0, 9, 0],  # 0
        [0, 0, 0, 0, 0, 0],  # 1
        [0, 5, 0, 1, 0, 2],  # 2
        [6, 0, 0, 0, 0, 2],  # 3
        [0, 0, 0, 0, 0, 1],  # 4
        [0, 6, 0, 0, 0, 0]  # 5
    ]

    codeMatrix = [
        [0, 5, 3, 6, 0, 6],
        [0, 0, 0, 6, 0, 2],
        [0, 1, 0, 3, 3, 4],
        [0, 0, 0, 0, 0, 1],
        [2, 2, 0, 3, 0, 4],
        [0, 0, 0, 0, 0, 0]

    ]

    graph = Graph(matrix)

    graph.df_print(0)           # 0 2 1 3 5 4
    print()
    graph.df_print(1)           # 1
    print()
    graph.df_print(2)           # 2 1 3 0 4 5
    print()
    graph.df_print(3)           # 3 0 2 1 4 5
    print()
    graph.df_print(4)           # 4 5 1
    print()
    graph.df_print(5)           # 5 1
    print()
    # graph.bf_print(0)           # 0 2 4 1 3 5
    # print()
    # print(graph.weight(0, 2))   # 7
    # print(graph.weight(3, 4))   # -1
