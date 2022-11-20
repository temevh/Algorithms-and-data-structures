# Based on lecture material and openDSA 19.5
from graph import Graph


def dijkstragraph(G, s):
    G.D = [10000000000000] * graph.vertex_count
    G.D[s] = 0
    for i in range(graph.vertex_count):
        v = minvertex(G)
        graph.visited[v] = True
        if G.D[v] == 10000000000000:
            return
        nList = graph.neighbors(v)
        for j in range(len(nList)):
            w = nList[j]
            if (G.D[w]) > (G.D[v]) + G.weight(v, w):
                G.D[w] = G.D[v] + G.weight(v, w)
    return G


def minvertex(G):
    v = 0
    for i in range(graph.vertex_count):
        if graph.visited[i] != True:
            v = i
            break
        for i in range(graph.vertex_count):
            if graph.visited[i] != True and G.D[i] < G.D[v]:
                v = i
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
    # new_graph.bf_print(0)           # 0 1 2 3 4 5 6 7 8 9
    # print(new_graph.weight(3, 6))   # 4
    # print(new_graph.weight(5, 8))   # -1
