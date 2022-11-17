# Based on lecture material and openDSA 19.3

class Graph:
    def __init__(self, grid):
        self.matrix = grid
        self.visited = [False] * len(self.matrix)
        self.stack = []

    def df_print(self, v):
        self.preVisit(v)
        self.visited[v] = True
        print(str(v)+" ", end="")
        nList = self.neighbors(v)
        for i in range(len(nList)):
            if self.visited[nList[i]] != True:
                self.df_print(nList[i])
        self.postVisit(v)

    def bf_print(self, v):
        Q = []
        Q.insert(0, v)
        self.visited[v] = True
        while len(Q) > 0:
            v = Q.pop()
            self.preVisit(v)
            nList = self.neighbors(v)
            for i in range(len(nList)):
                if self.visited[nList[i]] != True:
                    self.visited[nList[i]] = True
                    Q.remove(nList[i])
        self.postVisit(v)

    def preVisit(self, v):
        self.stack.append(v)

    def postVisit(self, v):
        self.stack.remove(v)

    def neighbors(self, v):
        nList = []
        nums = self.matrix[v]
        for i in nums:
            if i != 0:
                nList.append(nums.index(i))
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

    graph = Graph(matrix)

    graph.df_print(0)           # 0 2 1 3 5 4
    graph.bf_print(0)           # 0 2 4 1 3 5
    # print(graph.weight(0, 2))   # 7
    # print(graph.weight(3, 4))   # -1
