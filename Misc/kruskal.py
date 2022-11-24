from graph import Graph

class parTree:
    def __init__(self, M) -> None:
            self.arr = [-1 for i in range(M)]

    def UNION(self, i, j):
        root1 = self.FIND(i)
        root2 = self.FIND(j)
        if (root1 != root2):
            self.arr[root1] = root2
            return True
        else:
            return False

    def FIND(self,curr):
        while self.arr[curr] != -1:
            curr = self.arr[curr]
        return curr

def kruskal(graph):
    E = []
    result = []
    kru = parTree(graph.vertex_count)
    for i in range(graph.vertex_count):
        nList = graph.neighbors(i)
        for w in range(len(nList)):
            E.append([graph.weight(i, nList[w]), [i, nList[w]]])
    E = sorted(E, key=lambda item: item[0])  # Sort by weight
    numMST = graph.vertex_count
    while numMST > 1:
        temp = E.pop(0)
        #temp = E.pop()
        if temp == None:
            return
        v = temp[1][0]
        u = temp[1][1]
        if kru.UNION(v,u):
            result.append([v,u])
            numMST -= 1
    matrixified = [[0 for i in range(graph.vertex_count)] for j in range(graph.vertex_count)]
    for i in range(len(result)):
        a = result[i][0]
        b = result[i][1]
        if graph.weight(a,b) == -1:
            continue
        matrixified[a][b] = graph.weight(a,b)
        matrixified[b][a] = graph.weight(a,b)
    graph.matrix =  matrixified
    return graph


if __name__ == "__main__":

    matrix = [
        #    0  1  2  3  4  5
        [0, 0, 7, 6, 9, 0],  # 0
        [0, 0, 5, 0, 0, 6],  # 1
        [7, 5, 0, 1, 0, 2],  # 2
        [6, 0, 1, 0, 0, 2],  # 3
        [9, 0, 0, 0, 0, 1],  # 4
        [0, 6, 2, 2, 1, 0]  # 5
    ]
    graph = Graph(matrix)
    graph.bf_print(0)   # 0 2 3 4 1 5
    mst = kruskal(graph)
    mst.bf_print(0)     # 0 3 2 1 5 4
