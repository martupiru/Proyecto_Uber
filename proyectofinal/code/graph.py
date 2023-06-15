import heapq
from dictionary import *

def cargar_grafo(vertices,aristas):
    graph = {node: [] for node in vertices}
    for source, target, weight in aristas:
        graph[source].append((target, weight))
    return graph

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    previous = {node: None for node in graph}  # Diccionario para guardar los nodos anteriores
    visited = {node: [] for node in graph}  # Diccionario para guardar la lista de nodos visitados para cada nodo
    while queue:
        curr_distance, curr_node = heapq.heappop(queue)
        if curr_distance > distances[curr_node]:
            continue
        for neighbor, weight in graph[curr_node]:
            distance = curr_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = curr_node  # Guardar el nodo anterior
                visited[neighbor] = visited[curr_node] + [curr_node]  # Actualizar la lista de nodos visitados para el vecino
                heapq.heappush(queue, (distance, neighbor))
 # Convertir el diccionario previous en una lista
    return distances,  visited  # Retornar distancias y lista de visitados para cada nodo en formato de lista

def llenar_hash_distancias(mapa,hash_distancias):
    for vert in mapa:
        distances, visitados = dijkstra(mapa, vert)
        for node, distance in distances.items():
            cadena = (f"({vert},{node},{distance})")
            elementos = cadena.strip("()").split(",")
            if (elementos[2] != "inf") and (elementos[2] != "0"):
                terna = (elementos[0], elementos[1], int(elementos[2]))
                dupla=(terna,visitados[node])
                hashkeyterna = hash_terna(terna,len(hash_distancias))
                cargar_new_element_hash(hash_distancias,hashkeyterna,dupla)
    return hash_distancias


    