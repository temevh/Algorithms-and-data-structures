# Based on lecture material and openDSA 19.5
from graph import Graph


def dijkstragraph(G, s):
    G.alreadySeen = []
    G.D = [10000000000000] * G.vertex_count
    G.D[s] = 0
    toReturn = [[0 for i in range(G.vertex_count)]
                for j in range(G.vertex_count)]
    for j in range(G.vertex_count):
        G.alreadySeen.append([j, None])
    for i in range(G.vertex_count):
        G.lastNodes.append([0, 0])
    for i in range(G.vertex_count):
        v = minVertex(G, G.D)
        G.alreadySeen[v][1] = True
        if G.D[v] == 10000000000000:
            continue
        nList = G.neighbors(v)
        for j in range(len(nList)):
            w = nList[j]
            if (G.D[w]) > ((G.D[v]) + G.weight(v, w)):
                G.D[w] = G.D[v] + G.weight(v, w)
                G.lastNodes[w] = [v, w]
    for i in range(len(G.lastNodes)):
        x = G.lastNodes[i][0]
        y = G.lastNodes[i][1]
        if G.weight(x, y) == -1:
            continue
        toReturn[x][y] = G.weight(x, y)
    G.matrix = toReturn
    return G


def minVertex(G, distances):
    v = 0
    for i in range(G.vertex_count):
        if G.alreadySeen[i][1] != True:
            v = i
            break
    for i in range(G.vertex_count):
        if G.alreadySeen[i][1] != True and distances[i] < distances[v]:
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

    matrix2 = [
        [0, 3, 5, 6, 0, 0, 0, 5],
        [3, 0, 8, 0, 7, 8, 0, 1],
        [5, 8, 0, 5, 7, 0, 6, 0],
        [6, 0, 5, 0, 0, 6, 0, 0],
        [0, 7, 7, 0, 0, 0, 8, 2],
        [0, 8, 0, 6, 0, 0, 5, 0],
        [0, 0, 6, 0, 8, 5, 0, 0],
        [5, 1, 0, 0, 2, 0, 0, 0]
    ]

    graph = Graph(matrix2)
    new_graph = dijkstragraph(graph, 0)
    new_graph.df_print(0)           # 0 1 2 3 4 5 6 7 9 8
    new_graph.bf_print(0)           # 0 1 2 3 4 5 6 7 8 9
    print(new_graph.weight(3, 6))   # 4
    print(new_graph.weight(5, 8))   # -1
