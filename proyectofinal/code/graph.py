
#vertices = ['A', 'B', 'C', 'D', 'E']
#aristas = [('A', 'B', 5), ('A', 'C', 2), ('B', 'C', 1), ('B', 'D', 3), ('C', 'D', 2), ('D', 'E', 4)]

def cargar_grafo(vertices, aristas):
    graph = {}
    # Agregar vértices al grafo
    for v in vertices:
        graph[v] = {}
    # Agregar aristas al grafo
    for arista in aristas:
        origen, destino, peso = arista
        if origen in graph and destino in graph:
            graph[origen][destino] = peso
    return graph

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()
    while len(visited) < len(graph):
        min_distance = float('inf')
        min_node = None
        for node in graph:
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                min_node = node
        visited.add(min_node)
        if min_node is not None:
            for neighbor, weight in graph[min_node].items():
                distance = distances[min_node] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance

    return distances



#graph=cargar_grafo(vertices, aristas)
#start_node = 'B'
#distances = dijkstra(graph, start_node)
# Imprimir las distancias más cortas desde el nodo de inicio
#for node, distance in distances.items():
 #   print(f"Distancia desde {start_node} hasta {node}: {distance}")