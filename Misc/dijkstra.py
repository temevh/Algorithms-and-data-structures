# Based on lecture material and openDSA 19.5
from graph import Graph


def dijkstragraph(graph, s):
    graph.D = [100000000000000000] * len(graph.matrix)
    graph.D[s] = 0
    for i in range(len(graph.matrix)):
        v = minvertex()
        graph.visited[v] = True
        if graph.D[v] == 100000000000000000:
            return
        nList = graph.neighbors(v)
        j = 0
        while j < len(nList):
            w = nList[j]
            if graph.D[w] > (graph.D[v] + graph.weight(v, w)):
                graph.D[w] = graph.D[v] + graph.weight(v, w)
            j += 1
    return graph


def minvertex():
    v = 0

    for i in range(len(graph.matrix)):
        if graph.visited[i] != True:
            v = i
            break
    for j in range(len(graph.matrix)):
        if (graph.visited[j] != True) and (graph.D[j] < graph.D[v]):
            v = j

    return v


if __name__ == "__main__":

    matrix = [
        [0, 25,  6,  0,  0,  0,  0,  0,  0,  0],
        [0,  0,  0, 10,  3,  0,  0,  0,  0,  0],
        [0,  0,  0,  7,  0, 25,  0,  0,  0,  0],
        [0,  0,  0,  0, 12, 15,  4, 15, 20,  0],
        [0,  0,  0,  0,  0,  0,  0,  2,  0,  0],
        [0,  0,  0,  0,  0,  0,  0,  0,  2,  0],
        [0,  0,  0,  0,  0,  0,  0,  8, 13, 15],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  5],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  1],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
    ]

    graph = Graph(matrix)
    new_graph = dijkstragraph(graph, 0)
    new_graph.df_print(0)           # 0 1 2 3 4 5 6 7 9 8
    print()
    # new_graph.bf_print(0)           # 0 1 2 3 4 5 6 7 8 9
    # print(new_graph.weight(3, 6))   # 4
    # print(new_graph.weight(5, 8))   # -1
