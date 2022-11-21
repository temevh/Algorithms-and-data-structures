# Based on lecture materials and 19.8/9.1 openDSA material
from graph import Graph


def floyd(graph):
    for i in range(graph.vertex_count):
        for j in range(graph.vertex_count):

            if graph.weight(i, j) > 0:
                #print("i:", i, "j", j, "weight:", graph.weight(i, j))
                graph.D[i][j] = graph.weight(i, j)
            else:
                graph.D[i][j] = 0

    for k in range(graph.vertex_count):
        for i in range(graph.vertex_count):
            for j in range(graph.vertex_count):
                if (graph.D[i][k] != 0) and (graph.D[k][j] != 0) and ((graph.D[i][j] > (graph.D[i][k] + graph.D[k][j])) or graph.D[i][j] == 0):
                    graph.D[i][j] = graph.D[i][k] + graph.D[k][j]

    for i in range(graph.vertex_count):
        graph.D[i][i] = 0

    return graph.D


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
    D = floyd(graph)
    for i in range(6):
        for j in range(6):
            print(f"{D[i][j]:2d}", end=" ")
        print()
    #  0 12  7  8  9  9
    #  0  0  0  0  0  0
    #  7  5  0  1 16  2
    #  6  8 13  0 15  2
    #  0  7  0  0  0  1
    #  0  6  0  0  0  0
