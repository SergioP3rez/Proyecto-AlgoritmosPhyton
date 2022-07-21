
def bynarySearch(e, elements):
    return rec_bynarySearch(e, 0, len(elements) - 1, elements)

def rec_bynarySearch(e, low, high, elements):
    if low > high:
        return - low - 1
    mid = (low + high) // 2
    if e == elements[mid]:
        return mid
    elif e < elements[mid]:
        return rec_bynarySearch(e, low, mid - 1, elements)
    else:
        return rec_bynarySearch(e, mid + 1, high, elements)


universos = list(input().strip().split())
universos.sort()
n = int(input()) #Número de universos en los que hay que buscar
for i in range(n):
    universo = input()
    index = bynarySearch(universo, universos)
    if index == 0:
        print("VACIO", universos[index + 1])
    elif index == len(universos) - 1:
        print(universos[index - 1], "VACIO")
    else:
        print(universos[index - 1], universos[index + 1])