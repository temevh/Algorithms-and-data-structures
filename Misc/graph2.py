# Neighbors
# Post/previsit

class Graph:
    def __init__(self, grid):
        self.matrix = grid
        #self.visited = [False] * len(grid)
        self.visited = [0] * len(self.matrix)
        self.vertex_count = len(self.matrix)

    def df_print(self, v):
        self.preVisit(v)
        #self.matrix[v] = True
        nList = self.neighbors(v)

    def bf_print(self, v):
        pass

    def preVisit(self, v):
        self.visited[v] = False

    def postVisit(self, v):
        self.visited[v] = True

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
