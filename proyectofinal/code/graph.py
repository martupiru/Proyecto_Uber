import heapq
vertices = ['A', 'B', 'C', 'D', 'E']
aristas = [('A', 'B', 5), ('A', 'C', 2), ('B', 'C', 1), ('B', 'D', 3), ('C', 'D', 2), ('D', 'E', 4)]

def cargar_grafo(vertices,aristas):
    graph = {node: [] for node in vertices}
    for source, target, weight in aristas:
        graph[source].append((target, weight))
    return graph


def check_direccion(mapa,direccion):
    #verificar que las esquinas existan en el mapa
    flag = True
    esquina1 = direccion[0][0] 
    esquina2 = direccion[1][0]
    peso_a_buscar= int(direccion[0][1])+int(direccion[1][1])
    try:
        adyacentes = mapa[esquina1]
    except:
        flag = False
    if flag == True:
        try:
            if adyacentes[esquina2] == peso_a_buscar:
                flag = True
            else:
                flag = False
        except: 
            flag = False
    return flag

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        curr_distance, curr_node = heapq.heappop(queue)
        if curr_distance > distances[curr_node]:
            continue
        for neighbor, weight in graph[curr_node]:
            distance = curr_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances

graph=cargar_grafo(vertices, aristas)
start_node = 'B'
distances = dijkstra(graph, start_node)
# Imprimir las distancias más cortas desde el nodo de inicio
#ITEMS ES LOS ELEMENTOS DEL DICCIONARIO QUE CORRESPONDEN A ESE NODO

for node, distance in distances.items():
    cadena=(f"({start_node},{node},{distance})")
    elementos = cadena.strip("()").split(",")
    terna = (elementos[0], elementos[1], int(elementos[2]))


start_node = 'e10'
graph=cargar_grafo(vertices,aristas)
distances = dijkstra(graph, start_node)
print(distances)