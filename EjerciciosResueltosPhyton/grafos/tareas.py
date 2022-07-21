def topSort(g):
    aristas_entrantes = [0] * n #inicializamos todas las aristas entrantes a cero
    nodos_iniciales = []
    recorrido = []
    for v in range(len(g)):
        for a in g[v]: #Vamos recorriendo todos los elementos de cada indice del grafo y al número de tarea que encontremos le sumamos 1 arista entrante
            aristas_entrantes[a] = aristas_entrantes[a] + 1
    for v in range(len(g)): #Recorremos todas las posiciones de aristas entrantes y si alguna es 0 como sabemos que no le precede nadie lo añadimos a nodos iniciales
        if aristas_entrantes[v] == 0:
            nodos_iniciales.append(v)
            nodos_iniciales.sort()  #Ordenamos la lista de menor a mayor por si hay varios nodos con 0 aristas entrantes
    while nodos_iniciales: #Mientras nodos iniciales tenga elementos
        origen = nodos_iniciales.pop(0) #Como la lista de nodos iniciales ya esta ordenada vamos sacando el valor del indice 0 y lo guardamos en origen
        recorrido.append(origen) #Añadimos ese valor a la lista recorrido
        for a in g[origen]: #Vamos recorriendo todos los elementos de la posición del grafo origen
            aristas_entrantes[a] = aristas_entrantes[a] - 1 #A cada elemento le restamos 1 arista
            if aristas_entrantes[a] == 0: #Cuando las aristas entrantes del nodo a lleguen a cero
                nodos_iniciales.append(a) #Lo añadimos a la lista de nodos iniciales
                nodos_iniciales.sort() #Ordenamos la lista de menor a mayor

    for i in range(len(recorrido)):
        print(recorrido[i], end =" ")

n, m = map(int, input().strip().split()) #Número de tareas a realizar y el tamaño de la lista de tareas que deben precederse
g = []

for i in range (n): #Rellenamos el array de arrays vacíos
    g.append([])

for i in range(m):
    origenList, destinoList =  map(int, input().strip().split())  #pedimos m veces la lista de tareas con el orden de precedencia
    g[origenList].append(destinoList) #El indice de la lista se tiene que hacer antes que el valor que encontramos en dicho indice

topSort(g)