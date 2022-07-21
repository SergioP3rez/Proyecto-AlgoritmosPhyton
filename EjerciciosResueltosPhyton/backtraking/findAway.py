dirsX = [1, 0, -1, 0]
dirsY = [0, 1, 0, -1]

def bt(mat, cell, cont, lastObject, visited, salida):
    if cell == final_cell and cont == lastObject:
        salida = "SI"
    else:
        for a in range(len(dirsX)):
            if isFeasible(cell, dirsX[a], dirsY[a], mat, visited):
                nextX = cell[0] + dirsX[a]
                nextY = cell[1] + dirsY[a]
                visited.add((nextX, nextY))
                if mat[nextX][nextY] == 0:
                    lastObject += 1
                salida = bt(mat, (nextX, nextY), cont, lastObject, visited, salida)
                lastObject -= 1
                visited.remove((nextX, nextY))

    return salida

def isFeasible(cell, dirX, dirY, mat, visited):
    nextX = cell[0] + dirX
    nextY = cell[1] + dirY
    return 0 <= nextX < len(mat) and 0 <= nextY < len(mat[0]) and (mat[nextX][nextY] == 0) and (nextX, nextY) not in visited

n = int(input()) #Tamaño del laberinto
mat = []
for i in range(n):
    row = list(map(int, input().strip().split()))
    mat.append(row)
init_cell = (0,0)
final_cell = (n -1, n -1)
visited = set()
visited.add(init_cell)
cont = 0
for i in mat:
    for k in i:
        if k == 0:
            cont += 1

salida = bt(mat, init_cell, cont, 1, visited, "NO")
print(salida)
