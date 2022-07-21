def select_min(distances, visited):
    index = 0
    min_dist = float("inf")
    for i in range(0, len(distances)):
        if distances[i] < min_dist and not visited[i]:
            min_dist = distances[i]
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
        for start, end, weight in g[next_node]:
            distances[end] = min(distances[start] + weight, distances[end])

    return distances



n,m = map(int, input().strip().split()) #Número de componentes y número de conexiones entre ellos
g = []
salida = []
for i in range(n):
    g.append([])
components = list(map(int, input().strip().split()))
dict = {}
for i in range(m):
    c,d,l = map(int, input().strip().split())
    g[c].append((c,d,l))
    g[d].append((d,c,l))

for i in components:
    if i not in dict:
        dict[i] = float("inf")

for i in range(len(g)):
  distancias = dijkstra(g,i)
  for k in distancias:
      if k != 0:
        indice = distancias.index(k)
        if components[indice] == components[i] and dict[components[i]] > k:
            dict[components[i]] = k

for i in dict.items():
    salida.append(i)

salida.sort()
for i in salida:
    print(i[1], end=" ")






