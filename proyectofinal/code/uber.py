#PROYECTO LARICCHIA Y NAHMAN
from dictionary import *
from graph import *
import pickle
import re
from loud_elements import *


def load_fix_element(lugar):
    HashUbi=load_hash_table_ubicaciones()
    # Realiza las modificaciones, cargar lugares 
    with open("Mapa.pk", "rb") as MapaFile:
        Maph=pickle.load(MapaFile)
    exist = check_direccion(Maph,lugar[1])
    if exist == False:
        print("Esa direccion no existe")
    else:
        #si la direccion existe hacemos lo siguiente:
        if lugar[0][0].lower() not in ["h", "a", "t", "s", "e", "k", "i"]:
            print("El nombre ingresado no es válido")
        else:
            # Devuelve la hash modificada
            new_name = search_nombre(HashUbi,lugar)
            if new_name != None:
                cargar_new_element_hash(HashUbi,new_name,lugar)
                save_hash_table_ubicaciones(HashUbi)
#--------------------------------------------------------------------------------
def load_movil_element(ubimovil): #ubomovil: <nombre, dirección, monto>
    #verificar que exista la direccion (grafo)
    with open("Mapa.pk", "rb") as MapaFile:
        Maph=pickle.load(MapaFile)
    exist = check_direccion(Maph,ubimovil[1])
    if exist == False:
        print("Esa direccion no existe")
    else:
        #------autos------
        if ubimovil[0][0] == "C" or ubimovil[0][0] == "c":
            H_Autos=load_hash_table_Autos()
            modify_hash_table_Autos(H_Autos,ubimovil)
        #------personas------
        elif ubimovil[0][0] == "P" or ubimovil[0][0] == "p":
            H_Personas=load_hash_table_Personas()
            modify_hash_table_Personas(H_Personas,ubimovil)
            
        else:
            print("El nombre ingresado no es válido")

#-----------------------------------------------------------------------------------






def serializar():
    #preguntar argumentos de la funcion con path
    with open('MAPITAPRUEBA.txt', 'r') as archivo:
        lineas = archivo.readlines()
    #vertices
    lista = [elem[0:] for elem in lineas[0][1:-1].split('{' ) if elem.startswith('e')]
    lista[0] = [elem.replace('}', '') for elem in lista]   
    vertices = lista[0][0].strip("[]'").split(',')
    #ver bien como funciona!!!!!
    ternas = re.findall(r'<(.*?),(.*?),(.*?)>', lineas[1])
    aristas = [(elem[0], elem[1], int(elem[2])) for elem in ternas]
    graph = cargar_grafo(vertices, aristas)
    with open("Mapa.pk", "wb") as MapaFile:
        pickle.dump(graph,MapaFile)


def cargar_mapa_hashD():
    #CUANDO LLAMEMOS A LA FUNCION LLENAR HASH DE DISTANCIAS:
    with open("Mapa.pk", "rb") as MapaFile:
        Maph=pickle.load(MapaFile)
    #Creamos Hash
    H_Distancias = CreateHashTable(389)
    #Llenamos Hash
    Hash_Distancias = llenar_hash_distancias(Maph,H_Distancias)
    #Serializamos la Hash Anterior
    with open("Hash_Distancias.pk", "wb") as HashFileDistancias:
        pickle.dump(Hash_Distancias,HashFileDistancias)


def create_trip(persona,elemento): #elemento=direccion o nombre direccion fija
    #chequeamos que la entrada elemento sea una direccion o un nombre de direcciones
    with open("Hash_Personas.pk", "rb") as HashFilePersonas:
        HashPersonas=pickle.load(HashFilePersonas)
    if (search_nombre(HashPersonas,persona))==None:
        if isinstance(elemento, str):
            with open("Hash_Ubicaciones.pk", "rb") as HashFileUbicaciones:
                HashUbi=pickle.load(HashFileUbicaciones)
            direccion = search_direccion(HashUbi,elemento)
        elif isinstance(elemento, tuple):
            direccion = elemento
            #validar que esa direccion exista
            with open("Mapa.pk", "rb") as MapaFile:
                Maph=pickle.load(MapaFile)
            exist = check_direccion(Maph,direccion)
            if exist == False:
                print("Esa direccion no existe")
        else:
            print("El tipo de entrada no es válido")
    else:
        print('No existe la persona con la que desea cargar el viaje')
    
  

