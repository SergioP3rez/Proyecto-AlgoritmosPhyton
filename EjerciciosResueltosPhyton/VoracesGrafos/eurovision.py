

def update_components(components, old_id, new_id):
    for i in range(len(components)):
        if components[i] == old_id:
            components[i] = new_id

def kruskal(g, paises):
    components = list(range(len(g)))
    count = len(g)
    list_edges = []
    mst = 0
    red = []
    for adjacents in g.values():
        for start, end, weight in adjacents:
            if start < end:
                list_edges.append((weight,start,end))
    list_edges.sort()
    i = len(list_edges) - 1
    while len(list_edges) > 0 and count > 1:
        weight, start, end = list_edges[i]
        if components[paises.index(start)] != components[paises.index(end)]:
            count -= 1
            mst += weight
            update_components(components, components[paises.index(start)], components[paises.index(end)])
            red.append(start)
            red.append(end)
        i -= 1
    return mst, red

n,m = map(int, input().strip().split()) #Número de paises y de pactos
g = {}
paises = []

for i in range(m):
    c1, c2, p = input().strip().split()
    if c1 not in g:
        g[c1] = [(c1,c2,int(p))]
        paises.append(c1)
    else:
        g[c1].append((c1,c2,int(p)))
    if c2 not in g:
        g[c2] = [(c2,c1,int(p))]
        paises.append(c2)
    else:
        g[c2].append((c2,c1,int(p)))

maximo, red = kruskal(g,paises)
countMaxPactos = 0
countPeleles = 0
for i in paises:
    num = red.count(i)
    if num > countMaxPactos:
        countMaxPactos = num
    if num == 1:
        countPeleles += 1
print("El pais con mas pactos tiene", countMaxPactos)
print("La puntuacion total que se va a amaniar en la red es de", maximo)
print("Hay", countPeleles, "paises peleles")

