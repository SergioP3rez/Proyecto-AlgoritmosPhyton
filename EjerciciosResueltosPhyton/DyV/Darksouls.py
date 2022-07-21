def rec_BynarySearch(e, elements):
    return bynarySearch(e, 0, len(elements) - 1, elements)

def bynarySearch(e, low, high, elements):
    if low > high:
        return - low - 1
    mid = (low + high) // 2
    if elements[mid] == e:
        return mid
    elif e < elements[mid]:
        return bynarySearch(e, low, mid - 1, elements)
    else:
        return bynarySearch(e, mid + 1, high, elements)

n = int(input()) #Número de enemigos de la oleada
nivelesEnemigos = list(map(int, input().strip().split()))
sumaPuntos = []
for i in range(len(nivelesEnemigos)):
    if i == 0:
       sumaPuntos.append(nivelesEnemigos[i])
    else:
        sumaPuntos.append(nivelesEnemigos[i] + sumaPuntos[i - 1])
m = int(input()) #Número de casos de prueba
for i in range(m):
    nivelCaballero = int(input())
    index = rec_BynarySearch(nivelCaballero, nivelesEnemigos)
    if index >= 0:
        print(index + 1, sumaPuntos[index])
    else:
        index = - index - 1
        if index == 0:
            print(0, 0)
        elif index == len(nivelesEnemigos):
            print(len(nivelesEnemigos), sumaPuntos[len(nivelesEnemigos) - 1])
        else:
            print(index, sumaPuntos[index -1])


