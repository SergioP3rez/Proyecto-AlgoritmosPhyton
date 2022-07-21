def select_min(row, visitedColumns):
    min_dist = 0
    column = 0
    for i in range(0, len(row)):
        if row[i] != 0 and row[i] > min_dist and not visitedColumns[i]:
            min_dist = row[i]
            column = i

    return min_dist, column

def greedy(mat):
    visitedColumns= [False] * len(mat)
    beneficio = 0
    columna = 0
    visitedColumns[columna] = True
    for i in range(len(mat)):
        distancia, columna = select_min(mat[columna], visitedColumns)
        beneficio += distancia
        visitedColumns[columna] = True
        if i == len(mat) - 2:
            visitedColumns[0] = False
    print(beneficio)

n = int(input()) #Número de puntos de venta
mat = []
for i in range(n):
    row = list(map(int, input().strip().split()))
    mat.append(row)

greedy(mat)