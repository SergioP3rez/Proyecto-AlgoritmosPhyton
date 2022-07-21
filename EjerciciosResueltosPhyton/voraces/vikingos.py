def select_max(g, visited):
    ratio = 0
    index = 0
    for i in range(len(g)):
        if g[i][1] / g[i][2] > ratio and not visited[i]:
            ratio = g[i][1] / g[i][2]
            index = i
    return index


def isFeasible(tiempoMaximo, duracion):
    return tiempoMaximo - duracion >= 0


def greedy(g, t):
    visited = [False] * n
    tiempoMaximo = t
    puntuacionTotal = 0
    seleccionadas =  []
    while tiempoMaximo > 0:
        index = select_max(g, visited)
        visited[index] = True
        if isFeasible(tiempoMaximo, g[index][2]):
            tiempoMaximo -= g[index][2]
            puntuacionTotal += g[index][1]
            seleccionadas.append(g[index][0])
        else:
            proporcion = (tiempoMaximo * 100) / g[index][2]
            proporcion = proporcion / 100
            tiempoMaximo = tiempoMaximo - (g[index][2] * proporcion)
            puntuacionTotal += g[index][1] * proporcion
            seleccionadas.append(g[index][0])

    for i in g:
        if i[0] in seleccionadas:
            print(i[0])
    print(int(puntuacionTotal))




n,t = map(int, input().strip().split()) #Número de series disponibles y tiempo máximo que el usuario puede dedicar
g = []
for i in range(n):
    c,s,l= input().strip().split() #Nombre de la serie, puntuacion, duración
    g.append((c, int(s), int(l)))

greedy(g, t)