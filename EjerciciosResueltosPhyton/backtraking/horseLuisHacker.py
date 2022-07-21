#Direcciones a las que se podrá mover dentro del laberinto
dirsX = [1, 0, -1, 0] #1 derecha, 0 nada, -1 izquierda
dirsY = [0, 1, 0, -1] #1 arriba, o nada, -1 abajo

def bt(mat, cell, p, lastObject, actMin, actSteps, visited):
    if lastObject == p : # Si el ultimo objeto es igual al número de piezas se selecciona el minimo
        actMin = min(actMin, actSteps)
    else:
        for a in range(len(dirsX)): #Bucle que iterará 4 veces
            updatedObject = False # Ponemos updateObject a false
            if isFeasible(cell, dirsX[a], dirsY[a], mat, lastObject, visited): #Llamamos a isFeasible
                nextX = cell[0] + dirsX[a] #Sumamos desplazamiento de x
                nextY = cell[1] + dirsY[a] #Sumamos desplazamiento de y
                visited.add((nextX, nextY)) #Añadimos la tupla a visited
                if mat[nextX][nextY] == lastObject + 1:
                    lastObject += 1
                    updatedObject = True
                actMin = min(bt(mat, (nextX, nextY), p, lastObject, actMin, actSteps + 1, visited), actMin)
                if updatedObject:
                    lastObject -= 1
                visited.remove((nextX, nextY))
    return actMin


def isFeasible(cell, dirX, dirY, mat, lastObject, visited):
    nextX = cell[0] + dirX #En nextX guardamos la primera posición de cell más el valor correspondiente a dirX
    nextY = cell[1] + dirY #En nextY guardamos la segunda posición de cell más el valor correspondiente a dirY
    return 0 <= nextX < len(mat) and 0 <= nextY < len(mat[0]) and (mat[nextX][nextY] == lastObject + 1 or mat[nextX][nextY] == 0) and (nextX, nextY) not in visited
     #Si 0 es menor o igual que el valor de nextX y nextX es menor que la longitud de la matriz
     # Y o es menor o igual que nextY y nextY es menor que la longitud de la matriz
     # Y si el valor mat[nextX][nextY] es igual que lastObject + 1 o mat[nextX][nextY] es igual a 0
     # Y (nextX, nextY) no están en visitados
     # Si se cumple todo devolvemos true

if __name__ == '__main__':
    n, m, p = map(int, input().strip().split()) #Número de filas, columnas y piezas
    mat = []
    for _ in range(n):
        row = list(map(int, input().strip().split())) #Contienen m enteros que indican lo que hay en cada celda de la planta
        mat.append(row) #Añade la fila a la matriz
    init_cell = (0, 0) #Posición de salida que te da el enunciado
    visited = set() #Estructura de datos sin orden
    visited.add(init_cell) #Añadimos la posición de salida a visited

    print(bt(mat, init_cell, p, 0, 0x3f3f3f, 1, visited)) # A bt le pasamos la matriz, la celda inicial, el número de piezas, 0, un número
                                                          # muy alto sin llegar a infinito y visited