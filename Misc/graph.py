from queue import Queue


class Graph():
    def __init__(self, grid):
        self.matrix = grid

    def convert(self, a):
        # adjadency matrix -> adjadency list
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
        return converted

    def df_print(self, start):

        graph = self.convert(self.matrix)
        df = self.dfs(graph, start)
        for elem in df:
            print(elem, end=" ")
        print()

    def dfs(self, graph, start, path=[]):
        path += [start]
        for elem in graph[start]:
            if elem not in path:
                path = self.dfs(graph, elem, path)
        return path

    def bf_print(self, start):
        graph = self.convert(self.matrix)
        bf = self.bfs(graph, start)
        for elem in bf:
            print(elem, end=" ")
        print()

    def bfs(self, graph, source):
        toReturn = []
        q = Queue()
        visited = set()
        q.put(source)
        visited.update({0})
        while not q.empty():
            vertex = q.get()
            toReturn.append(vertex)
            for elem in graph[vertex]:
                if elem not in visited:
                    q.put(elem)
                    visited.update({elem})
        return toReturn

    def weight(self, v1, v2):
        if self.matrix[v1][v2] != 0:
            return (self.matrix[v1][v2])
        else:
            return -1


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
    graph.bf_print(0)           # 0 2 4 1 3 5
    print(graph.weight(0, 2))   # 7
    print(graph.weight(3, 4))   # -1
