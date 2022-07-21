def select_max(g, visited):
    ratio = 0
    index = 0
    for i in range(len(g)):
        if g[i][1] > ratio and not visited[i]:
            ratio = g[i][1]
            index = i
    return index


def greedy(g, maximoCajas):
    visited = [False] * n
    unidades = 0
    for i in range(len(g)):
        index = select_max(g,visited)
        visited[index] = True
        if g[index][0] <= maximoCajas:
            maximoCajas -= g[index][0]
            unidades += g[index][0] * g[index][1]
        else:
            unidades += maximoCajas * g[index][1]
            maximoCajas -= maximoCajas

    print(unidades)






n = int(input())
g = []
for i in range(n):
    c,u = map(int, input().strip().split())
    g.append((c,u))
t = int(input())

greedy(g,t)

