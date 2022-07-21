def select_max(candidates, visited):
    ratioRiesgoBeneficio = 0
    index = 0
    for i in range(len(candidates)):
        if (candidates[i][1] / candidates[i][0]) > ratioRiesgoBeneficio and not visited[i]:
            ratioRiesgoBeneficio = (candidates[i][1] /candidates[i][0])
            index = i
    return index

def isFeasible(riesgoMaximo, riesgo):
    return riesgoMaximo - riesgo >= 0

def greedy(g, m):
    candidates = []
    visited = [False] * n
    riesgoMaximo = m
    for i in g:
        candidates.append([i[1], i[2]])
    while riesgoMaximo > 0:
        index = select_max(candidates, visited)
        visited[index] = True
        if isFeasible(riesgoMaximo, g[index][1]):
            riesgoMaximo -= g[index][1]
            print(g[index][0], end= " ")
        else:
            porcentaje = (riesgoMaximo * 100) /g[index][1]
            porcentaje = porcentaje / 100
            riesgo = porcentaje * g[index][1]
            riesgoMaximo -= riesgo
            print(g[index][0], end=" ")





n, m = map(int, input().strip().split()) #Número de cartas disponibles y riesgo máximo que quiere correr perry
g = []
for i in range(n):
    c,r,b = input().strip().split() #Nombre de la carta, riesgo, beneficio
    g.append((c,int(r),int(b)))



greedy(g,m)