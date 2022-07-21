
def dfsRec(g, visited, v):
    visited[v] = True
    for adj in g[v]:
        if not visited[adj]:
            dfsRec(g, visited, adj)


def dfs(g):
    n = len(g)
    visited = [False] * n
    ccn = 0
    for v in range(0,n):
        if not visited[v]:
            dfsRec(g, visited, v)
            ccn += 1

    print(ccn)


n, m = map(int, input().strip().split()) #Número de asistentes y relaciones entre cada uno de ellos
g = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().strip().split())
    g[a].append(b)
    g[b].append(a)

dfs(g)