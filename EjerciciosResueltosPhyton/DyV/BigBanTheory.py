def bynarySearch(e, elements, saltos):
    return rec_bynarySearch(e, 0, len(elements) - 1, elements, saltos)

def rec_bynarySearch(e, low, high, elements, saltos):
    if low > high:
        return (- low - 1, saltos)
    mid = (low + high) // 2
    if elements[mid] == e:
        saltos += 1
        return mid, saltos
    elif e < elements[mid]:
        return rec_bynarySearch(e, low, mid - 1, elements, saltos + 1)
    else:
        return rec_bynarySearch(e, mid + 1, high, elements, saltos + 1)


n,m,p = map(int, input().strip().split()) #Número habitaciones, intentos, habitacion penny
identHabitaciones = list(map(int, input().strip().split()))
saltos = 0
index, saltos = bynarySearch(p, identHabitaciones, saltos)
if saltos <= m and index >= 0:
    print("Penny esta en la habitacion", str(index) +",","se han requerido", saltos, "saltos")
else:
    print("¿Donde esta Penny?")