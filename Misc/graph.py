class Graph():
    def __init__(self, grid):
        self.matrix = matrix

    def df_print(self, start):
        stack = [[0, 0]]

        while len(stack) != 0:
            value = stack.pop(0)
            self.matrix[value[0]][value[1]] = '1'

            if (value[0] < len(self.matrix)-1):
                down = [value[0]+1, value[1]]
                matrixValue = matrix[down[0]][down[1]]
                if (matrixValue != '1'):
                    stack.append(down)

            if (value[1] < len(matrix[0]) - 1 and value[0] < len(matrix) - 1):
                diagonal = [value[0] + 1, value[1] + 1]
                matrixValue = self.matrix[diagonal[0]][diagonal[1]]
                if matrixValue != '1':
                    stack.append(diagonal)

            if (value[1] < len(matrix[0]) - 1):
                right = [value[0], value[1] + 1]
                matrixValue = self.matrix[right[0]][right[1]]
                if matrixValue != '1':
                    stack.append(right)

        print(self.matrix)
        print(stack)

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
    # graph.bf_print(0)           # 0 2 4 1 3 5
    # print(graph.weight(0, 2))   # 7
    # print(graph.weight(3, 4))   # -1
