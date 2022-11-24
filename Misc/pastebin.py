def dijkstragraph(G, s):
    G.D = [10000000000000] * graph.vertex_count
    G.D[s] = 0
    for i in range(graph.vertex_count):
        v = minvertex(G)
        graph.visited[v] = True
        if G.D[v] == 10000000000000:
            return
        nList = graph.neighbors(v)
        for j in range(len(nList)):
            w = nList[j]
            if (G.D[w]) > (G.D[v]) + G.weight(v, w):
                G.D[w] = G.D[v] + G.weight(v, w)
    return G


def minvertex(G):
    v = 0
    for i in range(graph.vertex_count):
        if graph.visited[i] != True:
            v = i
            break
    for i in range(graph.vertex_count):
        if graph.visited[i] != True and G.D[i] < G.D[v]:
            v = i
    return v
