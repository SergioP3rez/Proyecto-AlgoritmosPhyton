def dfsRec(g, visited, v):
    visited[v] = True
    for adj in g[v]:
        if not visited[adj]:
            dfsRec(g, visited, adj)

def dfs(g, coste):
    n = len(g)
    sumaCoste = 0
    for v in range(0,n):
        visited = [False] * n
        ccn = 0
        for k in range(0,n):
            visited[v] = True
            if not visited[k]:
                dfsRec(g, visited, k)
                ccn += 1
        if ccn > 1:
            sumaCoste += coste[v]
    print(sumaCoste)


n,m = map(int, input().strip().split()) #Número de nodos y conexiones
g = [[] for i in range(n)]
coste = []
for i in range(n):
    c = int(input())
    coste.append(c)
for i in range(m):
    a,b = map(int, input().strip().split())
    g[a].append(b)
    g[b].append(a)

dfs(g, coste)