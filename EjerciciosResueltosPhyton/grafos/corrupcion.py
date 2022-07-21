
def dfsRec(g, visited, v, cont):
    visited[v] = True
    cont = 0
    for adj in g[v]:
        if not visited[adj]:
            dfsRec(g, visited, adj, cont)
        else:
            cont += 1
    return cont

def dfs(g):
    n = len(g)
    visited = [False] * n
    cont = 0
    for v in range(0,n):
        if not visited[v]:
            ciclos = dfsRec(g, visited, v, cont)
            if ciclos  > 0:
                cont += ciclos
    if cont > 0:
        print("CORRUPTOS")
    else:
        print("INOCENTES")


n,m = map(int, input().strip().split()) #Número de personas y conexiones
g = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().strip().split())
    g[a].append(b)
    g[b].append(a)

dfs(g)