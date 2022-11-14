graph = {0: [2, 4], 1: [], 2: [1, 3, 5],
         3: [0, 5], 4: [5], 5: [2]}
print("The adjacency List representing the graph is:")
print(graph)


def dfs(graph, source):
    S = list()
    visited_vertices = list()
    S.append(source)
    visited_vertices.append(source)
    while S:
        vertex = S.pop()
        print(vertex, end="-->")
        for u in graph[vertex]:
            if u not in visited_vertices:
                S.append(u)
                visited_vertices.append(u)


print("DFS traversal of graph with source 0 is:")
dfs(graph, 0)
