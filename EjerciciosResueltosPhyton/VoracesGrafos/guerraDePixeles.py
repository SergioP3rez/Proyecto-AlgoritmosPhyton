def updated_components(components, old_id, new_id):
    for i in range(len(components)):
        if components[i] == old_id:
            components[i] = new_id


def kruskal(g):
    components = list(range(len(g)))
    count = len(g)
    mst = 0
    list_edges = []
    conexiones = []
    for adjacents in g:
        for start, end, weight in adjacents:
            if start < end:
                list_edges.append((weight,start,end))
    list_edges.sort()
    i = 0
    while len(list_edges) > i and count > 1:
        weight, start, end = list_edges[i]
        if components[start] != components[end]:
            mst += weight
            count -= 1
            updated_components(components, components[start], components[end])
            conexiones.append((start, end))
        i += 1
    return mst, conexiones

n,m = map(int, input().strip().split()) #Número de pixeles y conexiones entre píxeles
g = []
conexionesVerificar = []
for i in range(n):
    g.append([])

for i in range(m):
    u, v, e = map(int, input().strip().split())
    g[u].append((u,v,e))
    g[v].append((v,u,e))

c = int(input()) #Número de conexiones que queremos verificar
for i in range(c):
    o, d = map(int, input().strip().split())
    conexionesVerificar.append((o,d))

mst, conexiones = kruskal(g)
print(mst)
for i in conexionesVerificar:
    if i in conexiones:
        print("SI")
    else:
        print("NO")