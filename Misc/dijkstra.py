from graph import Graph


def dijkstragraph(graph, start):
    # Initialize visited array/stack to "infinity"
    graph.visited = [1000000] * graph.v
    graph.visited[start] = 0
    for i in range(0, graph.v):
        value = minvertex(graph)
        graph[value] = "VISITED"
        if graph.visited[value] == 1000000:
            return


def minvertex(graph):
    value = 0
    for i in range(0, graph.v):
        if graph.visited[i] != "VISITED":
            value = i
            break
    for i in range(0, graph.v):
        if graph.visited[i] != "VISITED" and graph.visited[i] < graph.visited[value]:
            value = i

    return value


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
