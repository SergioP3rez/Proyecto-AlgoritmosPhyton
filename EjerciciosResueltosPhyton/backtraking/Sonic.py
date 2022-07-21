def esFactible(matriz,X,Y,inicio,intentos):
    nextX = inicio[0] + X[intentos]
    nextY = inicio[1] + Y[intentos]
    return 0 <= nextX < len(matriz) and 0 <= nextY < len(matriz[0]) and 0 <= matriz[nextX][nextY] <= 2

def bt(matriz,inicio,fin,anillos,pasos,pasosMin,anillosRecogidos,X,Y,elemAnterior):
    if anillosRecogidos == anillos and inicio == fin:
        pasosMin = min(pasosMin,pasos)
    else:
        camino = []
        camino.append(elemAnterior)
        visited = []
        visited.append((inicio[0], inicio[1]))
        for intentos in range(len(movX)):
            if esFactible(matriz,X,Y,inicio,intentos):
                while esFactible(matriz,X,Y,inicio,intentos):
                    inicio[0] = inicio[0] + X[intentos]
                    inicio[1] = inicio[1] + Y[intentos]
                    camino.append(matriz[inicio[0]][inicio[1]])
                    visited.append((inicio[0],inicio[1]))
                    elemAnterior = matriz[inicio[0]][inicio[1]]
                    if matriz[inicio[0]][inicio[1]] == 1:
                        anillosRecogidos += 1
                    matriz[inicio[0]][inicio[1]] = 3
                    pasos += 1
                minimo = bt(matriz, inicio, fin, anillos, pasos, pasosMin, anillosRecogidos, X, Y,elemAnterior)
                pasosMin = min(pasosMin, minimo)
                while len(camino) > 1:
                    elem = camino.pop()
                    posicion = visited.pop()
                    pasos -= 1
                    if elem == 1:
                        anillosRecogidos -= 1
                        matriz[posicion[0]][posicion[1]] = 1
                    else:
                        matriz[posicion[0]][posicion[1]] = elem
                inicio[0] = visited[0][0]
                inicio[1] = visited[0][1]
    return pasosMin

n = int(input())
matriz = []
for i in range(n):
    fila = list(map(int,input().strip().split()))
    matriz.append(fila)
xp,yp,xf,yf = map(int, input().strip().split())
anillos = 0
for i in matriz:
    for j in i:
        if j == 1:
            anillos += 1
movX = [1,0,-1,0]
moxY = [0,1,0,-1]
sol = bt(matriz,[xp,yp],[xf,yf],anillos,1,0x3f3f3f,0,movX,moxY,matriz[xp][yp])
print(sol)