# https://www.askpython.com/python/examples/depth-first-search-in-a-graph
# https://www.codingninjas.com/codestudio/library/implementation-of-dfs-using-adjacency-matrix
class Graph():
    def __init__(self, grid):
        self.matrix = grid

    def convert(self, a):
        converted = {}
        i = 0
        for j in range(len(a)):
            converted[i] = []
            i += 1
        k = 0
        for elem in a:
            for i in elem:
                if i != 0:
                    converted[k].append(elem.index(i))
            k += 1
        print(converted)

    def df_print(self, start):
        # adjency matrix -> adjency list
        graph = self.convert(self.matrix)
        print(graph)

    def df_help(self, graph, vertex, path=[]):
        path += [vertex]
        for n in graph[vertex]:
            if n not in path:
                path = self.df_help(graph, n, path)

        return path

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
    x = {0: [2, 4], 1: [], 2: [1, 3, 5],
         3: [0, 5], 4: [5], 5: [1]}
    graph = Graph(matrix)

    graph.df_print(0)           # 0 2 1 3 5 4
    # graph.bf_print(0)           # 0 2 4 1 3 5
    # print(graph.weight(0, 2))   # 7
    # print(graph.weight(3, 4))   # -1
