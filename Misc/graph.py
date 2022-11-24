# Based on lecture material and openDSA 19.3
# If starting vertex is 1, no neighbors

class Graph:
    def __init__(self, grid):
        self.matrix = grid
        self.vertex_count = len(grid)
        self.visited = [False] * len(self.matrix)
        self.stack = []
        self.D = [[0 for i in range(self.vertex_count)]
                  for j in range(self.vertex_count)]

        self.alreadySeen = []
        self.Backup = grid
        self.lastNodes = []
        self.BackUp = self.matrix

    def df_print(self, v):
        self.preVisit(v)
        self.visited[v] = True
        nList = self.neighbors(v)
        for i in range(len(nList)):
            if self.visited[nList[i]] != True:
                self.df_print(nList[i])
        self.postVisit(v)
        if len(self.stack) == 0:
            replace = [False] * len(self.matrix)
            self.visited = replace
            print()

    def preVisit(self, v):
        print(str(v)+" ", end="")
        self.stack.insert(0, v)

    def postVisit(self, v):
        self.stack.remove(v)

    def bf_print(self, v):
        Q = []
        Q.append(v)
        self.visited[v] = True
        while len(Q) > 0:
            v = Q.pop(0)  # Dequeue
            self.preVisit(v)
            nList = self.neighbors(v)
            for i in range(len(nList)):
                if self.visited[nList[i]] != True:
                    self.visited[nList[i]] = True
                    Q.append(nList[i])
            self.postVisit(v)
        if len(self.stack) == 0:
            replace = [False] * len(self.matrix)
            self.visited = replace
        print()

    def neighbors(self, v):
        nList = []
        for i in range(self.vertex_count):
            if self.matrix[v][i] != 0:
                nList.append(i)
        return nList

    def weight(self, a, b):
        if a >= self.vertex_count or b >= self.vertex_count:
            return -1
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
    graph.bf_print(0)           # 0 2 4 1 3 5
    print(graph.weight(0, 2))   # 7
    print(graph.weight(3, 4))   # -1
