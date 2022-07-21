def select_min(distances, visited):
    min_dist = float("inf")
    vertex = 0
    for i in range(0, len(distances)):
        if distances[i] < min_dist and not visited[i]:
            min_dist = distances[i]
            vertex = i
    return vertex


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
        for start, end, weight in g[next_node]:
            distances[end] = min(distances[end], distances[start] + weight)

    return distances


n ,m = map(int, input().strip().split()) #Número de chimeneas y número de conexiones entre chimeneas
g = [[] for i in range(n)]
gFinal = [[] for i in range(n)]

for i in range(m):
    o,d,f = map(int, input().strip().split())
    g[o].append([o,d,f])
    g[d].append([d,o,f])
a = int(input()) #Número de chimeneas apagadas
identApagadas = list(map(int, input().strip().split()))
x, y = map(int,input().strip().split()) #Origen y destino

for i in g:
    for k in i:
       if k[0]not in identApagadas and k[1] not in identApagadas:
          gFinal[k[0]].append((k[0], k[1], k[2]))
          gFinal[k[1]].append((k[1],k[0],k[2]))


if y not in identApagadas and x not in identApagadas and x != y:
       distancias = dijkstra(gFinal, x)
       if distancias[y] == float("inf"):
           print("IMPOSIBLE")
       else:
           print(distancias[y])
elif x == y:
    print(0)
else:
    print("IMPOSIBLE")