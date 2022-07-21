def sumar(pepitas):
    sum = 0
    for row in pepitas:
        for p in row:
            sum += p
    return sum


def dividir_Sandía(pepitas):
    sol = [[], [], [], []]
    m = len(pepitas) // 2
    cont = 0
    for row in pepitas: #Recorremos las filas de la amtriz
        if cont < m:
          sol[0].append(row[:m])
          sol[1].append(row[m:])
          cont += 1
        else: #En estas dos posiciones se guarda la segunda mitad de la matriz
          sol[2].append(row[:m])
          sol[3].append(row[m:])
    return sol


def calcular_pepitas_Dyv(pepitas, c, div):
    minimo = float('inf') #Inicializamos minimo a infinito
    maximo = 0
    if div == c: #Si las divisiones son igual a los cortes entramos
        sol = sumar(pepitas)
        return sol, sol
    else:
        subTrozos = dividir_Sandía(pepitas)
        div += 1
        for k in subTrozos: #Recorremos cada subtrozo
            minimo2, maximo2 = calcular_pepitas_Dyv(k, c, div) #Llamamos recursivamente a la función
            minimo = min(minimo, minimo2)
            maximo = max(maximo, maximo2)

    return minimo, maximo


n, c = map(int, input().strip().split())
pepitas = [list(map(int, input().split())) for _ in range(n)]

min_p, maximo_p = calcular_pepitas_Dyv(pepitas,c, 0)
print(min_p)