# Proyecto Uber

Proyecto desarrollado por **Martina Laricchia** y **Aida Nahman** con el fin de simular el funcionamiento básico de una plataforma de transporte similar a Uber. El sistema permite gestionar un **mapa de calles representado mediante un grafo**, registrar **personas, autos y ubicaciones fijas**, y calcular viajes entre distintos puntos de la ciudad.

El proyecto implementa **estructuras de datos como tablas hash** para almacenar información de autos, personas y ubicaciones, y utiliza el **algoritmo de Dijkstra** para calcular las distancias mínimas entre esquinas del mapa. A partir de esta información, el sistema puede determinar los **autos más cercanos a un pasajero**, generar un **ranking de opciones disponibles** y calcular el **costo estimado del viaje**.

## Funcionalidades

El programa permite:
- Crear y serializar un **mapa de calles** desde un archivo
- Registrar **autos, personas y ubicaciones fijas** en el sistema
- Validar **direcciones dentro del mapa**
- Calcular el **camino más corto** entre distintos puntos
- Seleccionar un **auto disponible** para realizar un viaje
- Actualizar la **ubicación y el saldo de los usuarios** luego de completar el viaje

## Ejecución

El sistema se ejecuta mediante **línea de comandos**, permitiendo realizar operaciones como:
- Crear el mapa
- Cargar autos, personas o ubicaciones
- Solicitar y gestionar viajes
