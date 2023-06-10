import heapq
from loud_elements import *
from dictionary import *
from trip import *
import pickle

def cargar_grafo(vertices,aristas):
    graph = {node: [] for node in vertices}
    for source, target, weight in aristas:
        graph[source].append((target, weight))
    return graph


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


# Imprimir las distancias más cortas desde el nodo de inicio
#ITEMS ES LOS ELEMENTOS DEL DICCIONARIO QUE CORRESPONDEN A ESE NODO
def llenar_hash_distancias(mapa,hash_distancias):
    for vert in mapa:
        distances = dijkstra(mapa, vert)
        for node, distance in distances.items():
            cadena = (f"({vert},{node},{distance})")
            elementos = cadena.strip("()").split(",")
            if (elementos[2] != "inf") and (elementos[2] != "0"):
                terna = (elementos[0], elementos[1], int(elementos[2]))
                hashkeyterna = hash_terna(terna,len(hash_distancias))
                cargar_new_element_hash(hash_distancias,hashkeyterna,terna)
    return hash_distancias


    