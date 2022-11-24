graph = {0: [2, 4], 1: [], 2: [1, 3, 5],
         3: [0, 5], 4: [5], 5: [1]}
#print("The adjacency List representing the graph is:")
# print(graph)


def dfs(graph, vertex, path=[]):
    path += [vertex]
    for n in graph[vertex]:
        if n not in path:
            path = dfs(graph, n, path)
    return path


#print("DFS traversal of graph with source 0 is:")
print(dfs(graph, 0))
