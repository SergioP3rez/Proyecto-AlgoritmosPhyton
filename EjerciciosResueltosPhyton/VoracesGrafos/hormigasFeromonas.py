def select_min(distances, visited):
    min_dist = float('inf')
    index = 0
    for i in range(0, len(distances)):
        if not visited[i] and distances[i] < min_dist:
            min_dist = distances[i]
            index = i
    return index

def dijkstra(g, origin, dest):
    distances = [float('inf')] * len(g)
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

    return distances[dest]

trad = {}
cont = 0
n, m = map(int, input().strip().split()) #Número de lugares y caminos posibles
feromonas = []
caminos = []

for i in range(n):
    ident, tipo = input().strip().split() #Identificador del lugar y tipo de feromona
    feromonas.append((ident, int(tipo)))
    trad[ident] = cont
    cont += 1
    caminos.append([])

for i in range(m):
    a, b, d = input().strip().split()
    if feromonas[trad[a]][1] != 0 and feromonas[trad[b]][1] != 0:
        caminos[trad[a]].append((trad[a], trad[b], int(d)))
        caminos[trad[b]].append((trad[b], trad[a], int(d)))

origen, destino = input().strip().split()

if feromonas[trad[origen]][1] == 0 or feromonas[trad[destino]][1] == 0:
    print('imposible')
else:
    sol = dijkstra(caminos, trad[origen], trad[destino])
    if sol == float('inf'):
        print('imposible')
    else:
        print(sol)