def update_components(components, old_id, new_id):
    for i in range(len(components)):
        if components[i] == old_id:
            components[i] = new_id


def kruskal(g):
    components = list(range(len(g)))
    count = len(g)
    list_edges = []
    mst = 0
    for adjacents in g:
        for start, end, weight in adjacents:
            if start < end:
                list_edges.append((weight, start, end))
    list_edges.sort()
    i = 0
    while len(list_edges) > i and count > 1:
        weight, start, end = list_edges[i]
        if components[start] != components[end]:
            count -= 1
            mst += weight
            update_components(components, components[start], components[end])
        i += 1
    return mst


n, m = map(int, input().strip().split()) #Número de supermercados y caminos que los unen
g = []
for i in range(n):
    g.append([])
for i in range(m):
    o,d,p = map(int, input().strip().split())
    g[o].append((o,d,p))
    g[d].append((d,o,p))

print(kruskal(g))
