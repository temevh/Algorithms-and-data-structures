from graph import Graph

# ParPerTree =
# KVPair =
#MinHeap = not needed


def kruskal(graph):
    E = []

    for i in range(graph.vertex_count):
        nList = graph.neighbors(i)
        for w in range(len(nList)):
            E.append([graph.weight(i, nList[w]), [i, nList[w]]])
    E = sorted(E, key=lambda item: item[0])  # Sorted by weight
    numMST = graph.vertex_count


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
    # graph.bf_print(0)   # 0 2 3 4 1 5
    mst = kruskal(graph)
    # mst.bf_print(0)     # 0 3 2 1 5 4
