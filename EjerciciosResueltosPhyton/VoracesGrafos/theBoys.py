def select_min(distances, visited):
    min_dit = float("inf")
    index = 0
    for i in range(len(distances)):
        if distances[i] < min_dit and not visited[i]:
            min_dit = distances[i]
            index = i
    return index


def dijkstra(g, origin):
    distances = [float("inf")] * len(g)
    visited = [False] * len(g)
    distances[origin] = 0
    visited[origin] = True
    for start, end, weight in g[origin]:
        distances[end] = weight
    for i in range(1, len(g)):
        next_node = select_min(distances, visited)
        visited[next_node] = True
        for start, end,weight in g[next_node]:
            distances[end] = min(distances[end], distances[start] + weight)
    return distances

n,m = map(int, input().strip().split()) #Número de localizaciones y conexiones
g  = [[] for i  in range(n)]
localizaciones = []
for i in range(m):
    u,v,d = map(int, input().strip().split())
    g[u].append((u,v,d))
    g[v].append((v,u,d))
b,s = map(int, input().strip().split())
for i in range(s):
    p = int(input())
    localizaciones.append(p)
ordenSalida = []
for i in localizaciones:
    distances = dijkstra(g, b)
    ordenSalida.append((distances[i],localizaciones[localizaciones.index(i)]))
ordenSalida.sort()
for i in ordenSalida:
    print(i[1], i[0])