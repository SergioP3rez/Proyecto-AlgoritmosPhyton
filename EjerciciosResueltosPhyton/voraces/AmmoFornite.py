def select_posicion(n, i):
    suma = 0
    index = 0
    municionesSuma = []
    for k in range(len(n)):
        suma = suma + n[k]
        municionesSuma.append(suma)
        if suma >= i:
            index = k
            return index, municionesSuma[index]


def greedy(n, intentos, divisiones):
    for i in intentos:
       indice, suma = select_posicion(n,i)
       suma2 = suma
       divisiones2 = []
       for i in divisiones:
           if suma2 // i > 0:
               divisiones2.append(suma2 // i)
               suma2 = suma2 - (suma2 // i) * i
           else:
               divisiones2.append(0)

       print(indice, suma, "->" ,end=" ")
       for i in divisiones2:
           print(i, end=" ")
       print(end = "\n")

n = list(map(int, input().strip().split())) #Municiones disponibles en cada localizacion
intentos = []
m = int(input()) #Número de intentos
for i in range(m):
    a = int(input())
    intentos.append(a)
divisiones = [100, 50, 25, 10, 5]
greedy(n, intentos, divisiones)