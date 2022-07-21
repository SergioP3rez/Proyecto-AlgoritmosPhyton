def sumaMaxDyV(v,ini,fin):
    if ini == fin:
        result = v[ini]
    else:
        mitad = (ini + fin) // 2
        sumaMaxIzq = sumaMaxDyV(v,ini,mitad)
        sumaMaxDer = sumaMaxDyV(v,mitad+1,fin)

        suma = 0
        sumaMaxI = 0
        for i in range(mitad,ini-1, -1):
            suma += v[i]
            if suma > sumaMaxI:
                sumaMaxI = suma

        suma = 0
        sumaMaxD = 0
        for i in range(mitad+1, fin +1):
            suma += v[i]
            if suma > sumaMaxD:
                sumaMaxD = suma
        sumaMaxCentral = sumaMaxI+sumaMaxD
        result = max(sumaMaxCentral,sumaMaxIzq,sumaMaxDer)

    return result


casos = list(map(int, input().strip().split()))
sumaMaxima = sumaMaxDyV(casos, 0, len(casos) - 1)
print(sumaMaxima)