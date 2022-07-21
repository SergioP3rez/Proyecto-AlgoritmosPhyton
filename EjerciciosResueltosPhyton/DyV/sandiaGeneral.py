def sumar(matriz):
    sum = 0
    for row in matriz:
        for p in row:
            sum += p
    return sum


def dividir_matriz(matriz):
    sol = [[], [], [], []]
    m = len(matriz) // 2
    cont = 0
    for row in matriz: #Recorremos las filas de la amtriz
        if cont < m:
          sol[0].append(row[:m])
          sol[1].append(row[m:])
          cont += 1
        else: #En estas dos posiciones se guarda la segunda mitad de la matriz
          sol[2].append(row[:m])
          sol[3].append(row[m:])
    return sol

def calcular_subMatriz_Dyv(matriz, c, div):
    minimo = float('inf')
    maximo = 0
    if div == c: #Si las divisiones son igual a los cortes entramos
        sol = sumar(matriz)
        return sol, sol
    else:
        subTrozos = dividir_matriz(matriz)
        div += 1
        for k in subTrozos:
            minimo2, maximo2 = calcular_subMatriz_Dyv(k, c, div)
            minimo = min(minimo, minimo2)
            maximo = max(maximo, maximo2)

    return minimo, maximo


n, c = map(int, input().strip().split()) #longitud y cortes
matriz = [list(map(int, input().split())) for _ in range(n)]

min_p, maximo_p = calcular_subMatriz_Dyv(matriz,c, 0)
print(min_p)