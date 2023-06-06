import heapq
from dictionary import *
import pickle

def cargar_grafo(vertices,aristas):
    graph = {node: [] for node in vertices}
    for source, target, weight in aristas:
        graph[source].append((target, weight))
    return graph


def check_direccion(mapa,direccion):
    flag = True
    esquina1 = direccion[0][0] 
    esquina2 = direccion[1][0]
    peso_a_buscar= int(direccion[0][1])+int(direccion[1][1])
    try:
        #verificar que la esquina 1 existe en el mapa
        adyacentes = mapa[esquina1]
    except:
        flag = False
    if flag == True:
        try:
            #verificar que la esquina 2 sea el otro vertice de esa arista
            for i in range (len(adyacentes)):
                if adyacentes[i][0] == esquina2:
                    if adyacentes[i][1]==peso_a_buscar:
                        flag = True    
                    else:
                        flag=False
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


"""
`def llenar_hash_distancias(mapa, hash_distancias):
    for vert in mapa:
        distances = dijkstra(mapa, vert)
        for node, distance in distances.items():
            cadena = (f"({vert},{node},{distance})")
            elementos = cadena.strip("()").split(",")
            if (elementos[2] != '0') and (elementos[2]!='inf'):
                terna = (elementos[0], elementos[1], int(elementos[2]))
                hashkeyterna = hash_terna(terna,len(hash_distancias))
                cargar_new_element_hash(hash_distancias,hashkeyterna,terna)
    printHashTable(hash_distancias)"""      