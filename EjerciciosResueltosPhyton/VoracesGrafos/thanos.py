
def bynarySearch(e, elements):
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


n = int(input()) #Número de habitantes que existen
identHab = list(map(int, input().strip().split()))
m = int(input())
identHabAmochados = list(map(int, input().strip().split()))
identHabAmochados.sort()
p = int(input())
idenComprobar = list(map(int,input().strip().split()))

for i in idenComprobar:
    index = bynarySearch(i, identHabAmochados)
    if index >= 0:
        index2 = bynarySearch(i, identHab)
        if index2 >= 0:
            print(":_(")
        else:
            print(":)")
    else:
        print(":)")