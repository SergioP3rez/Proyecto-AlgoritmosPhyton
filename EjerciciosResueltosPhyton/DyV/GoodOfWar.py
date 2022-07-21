
def bynary_Search(e, elements):
    return rec_bynarySearch(e, 0, len(elements) - 1, elements)

def rec_bynarySearch(e, low, high, elements):
    if low > high:
        return - low - 1
    mid = (low + high) // 2
    if elements[mid] == e:
        return mid
    elif e < elements[mid]:
        return rec_bynarySearch(e, low, mid - 1, elements)
    else:
        return rec_bynarySearch(e, mid + 1, high, elements)

n = int(input()) #Numero de niveles diferentes disponibles
niveles = list(map(int, input().strip().split())) #diferentes y ordenados de menor a mayor
q = int(input())
nivelesJugadores = list(map(int, input().strip().split()))

for i in nivelesJugadores:
    index = bynary_Search(i, niveles)
    if index >= 0:
        if index == 0:
            print("X", niveles[index + 1])
        elif index == len(niveles) - 1:
            print(niveles[index - 1], "X")
        else:
            print(niveles[index - 1], niveles[index + 1])
    else:
        index = - index - 1
        if index == 0:
            print("x", niveles[index])
        elif index == len(niveles):
            print(niveles[index - 1], "X")
        else:
            print(niveles[index - 1], niveles[index])