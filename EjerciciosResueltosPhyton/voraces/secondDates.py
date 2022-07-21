def select_max(candidates, k):
    sumaJovenes1 = 0
    sumaMayores1 = 0
    sumaJovenes2 = 0
    sumaMayores2 = 0
    for i in range(k):
        sumaJovenes1 += candidates[i]
    for i in range(k, len(g)):
        sumaMayores1 += candidates[i]
    diferencia1 = sumaMayores1 - sumaJovenes1
    n = len(g) - k
    for i in range(n, len(g)):
        sumaMayores2 += candidates[i]
    for i in range(n):
        sumaJovenes2 += candidates[i]
    diferencia2 = sumaMayores2 - sumaJovenes2
    if diferencia1 > diferencia2:
        return "Jovenes"
    else:
        return "Mayores"

def greedy(g, k):
    g.sort()
    candidates = []
    for i in g:
        candidates.append(i[0])
    grupok = select_max(candidates, k)
    if grupok == "Jovenes":
        for i in range(0, k):
            if i != k - 1:
              print(g[i][1], end=" ")
            else:
                print(g[i][1])
        for i in range(k, len(g)):
              print(g[i][1], end=" ")

    else:
        for i in range(0, k - 1):
            if i != k - 2:
                print(g[i][1], end=" ")
            else:
                print(g[i][1])
        for i in range(k - 1, len(g)):
                print(g[i][1], end=" ")



n,k = map(int, input().strip().split()) #Número de participantes y tamaño de uno de los grupos
g = []
for i in range(n):
    c,a = input().strip().split()
    g.append((int(a), c))


greedy(g, k)