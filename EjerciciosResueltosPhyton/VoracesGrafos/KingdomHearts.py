def selectMin_prim(short_edges, visited):
    min_dist = float("inf")
    vertex = 0
    for i in range(1, len(short_edges)):
        if short_edges[i] < min_dist and not visited[i]:
            min_dist = short_edges[i]
            vertex = i
    return vertex, min_dist


def prim(g, initial):
    initial = initial
    short_edges = [float("inf")] * len(g)
    visited = [False] * len(g)
    visited[initial] = 0
    mst = 0
    for start, end, weight in g[initial]:
        short_edges[end] = weight
    for i in range(1, len(g)):
        next_node, cost = selectMin_prim(short_edges, visited)
        visited[next_node] = True
        mst += cost
        for start, end, weight in g[next_node]:
            if not visited[end]:
                short_edges[end] = min(short_edges[end], weight)
    return mst


n,m = map(int, input().strip().split()) #Número de universos disney y número de carreteras que los conectan
g = []
for i in range(n):
    g.append([])
for i in range(m):
    u,v,e = map(int,input().strip().split())
    g[u].append((u,v,e))
    g[v].append((v,u,e))

print(prim(g, 0))