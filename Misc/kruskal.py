from graph import Graph

class parTree:
    def __init__(self, M) -> None:
            self.arr = self.treePar(M)

    def treePar(self, M):
        arr = []
        for i in range(M):
            arr.append(-1)
        return arr

    def UNION(self, i, j, arr):
        root1 = FIND(i, arr)
        root2 = FIND(j, arr)
        if (root1 != root2):
            array[root1] = root2
            return True
        else:
            return False

    def FIND(self,curr, arr):
        while graph[curr] != -1:
            curr = graph[curr]

        return curr

def kruskal(graph):
    E = []
    result = []
    A = parTree(graph.vertex_count)
    print(A)
    for i in range(graph.vertex_count):
        nList = graph.neighbors(i)
        for w in range(len(nList)):
            E.append([graph.weight(i, nList[w]), [i, nList[w]]])
    E = sorted(E, key=lambda item: item[0])  # Sorted by weight
    numMST = graph.vertex_count
    while numMST > 1:
        temp = E.pop(0)
        if temp == None:
            return
        v = temp[0]
        u = temp[1]
        if UNION(v,u):
            result.append([v,u])
            numMST -= 1




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
    # mst.bf_print(0)     # 0 3 2 1 5 4
