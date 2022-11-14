class Graph:

    def df_print(self, start):
        pass

    def bf_print(self, start):
        pass

    def weight(self, v1, v2):
        pass


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
    print(graph.weight(0, 2))   # 7
    print(graph.weight(3, 4))   # -1
