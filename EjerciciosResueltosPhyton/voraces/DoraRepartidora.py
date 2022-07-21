def select_min(candidates, visited):
    minimo = float("inf")
    index = 0
    for i in range(len(candidates)):
        if candidates[i] < minimo and not visited[i]:
            minimo = candidates[i]
            index = i
    return minimo, index


def greedy(g):
    tiempoTotal = 0
    sumaAnterior = 0
    visited = [False] * n
    candidates = []
    for i in g:
        candidates.append(i[1])
    for i in range(len(visited)):
        minimo, indice = select_min(candidates, visited)
        visited[indice] = True
        sumaAnterior += minimo
        tiempoTotal += sumaAnterior

    return tiempoTotal




n = input()#Número de clientes que han hecho pedidos
n = int(n)
g = []
for i in range(n):
    c,t = map(int, input().strip().split())
    g.append((c,t))

print(greedy(g))