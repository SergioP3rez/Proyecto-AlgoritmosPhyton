def select_min(distances, visited):
    min_dist = float("inf")
    vertex = 0
    for i in range(len(distances)):
        if distances[i] < min_dist and not visited[i]:
            min_dist = distances[i]
            vertex = i
    return vertex


def dijkstraCamino(g, origin, destino):
    distances = [float("inf")] * len(g)
    visited = [False] * len(g)
    distances[origin] = 0
    visited[origin] = True
    camino = [[] for i in range(len(g))]
    for start, end, weight in g[origin]:
        distances[end] = weight
        camino[end].append(start)
    while not visited[destino]:
        for i in range(1, len(g)):
            next_node = select_min(distances, visited)
            visited[next_node] = True
            camino[next_node].append(next_node)
            for start, end, weight in g[next_node]:
                if distances[start] + weight < distances[end]:
                    camino[end].clear()
                    distances[end] = distances[start] + weight
                    for i in range(len(camino[start]) - 1):
                        camino[end].append(camino[start][i])
                    camino[end].append(start)
    print(distances[destino])
    for i in camino[destino]:
        print(i, end = " ")


n,m = map(int, input().strip().split()) #Número de cervezas que hay y conexiones entre ellas
g = []
for i in range(n):
    g.append([])

for i in range(m):
    c1, c2, d = map(int, input().strip().split())
    g[c1].append((c1,c2,d))
    g[c2].append((c2,c1,d))

origin, destino = map(int, input().strip().split())

dijkstraCamino(g, origin, destino)