from graph import Graph


def dijkstragraph(graph, start):
    graph.D = [10000000000000] * len(graph.matrix)


def minvertex(G, D=[]):
    v = 0
    i = 0
    while i < len(graph.matrix):
        if graph.visited[i] != True:
            v = i
            break


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
    # new_graph.df_print(0)           # 0 1 2 3 4 5 6 7 9 8
    # new_graph.bf_print(0)           # 0 1 2 3 4 5 6 7 8 9
    # print(new_graph.weight(3, 6))   # 4
    # print(new_graph.weight(5, 8))   # -1
