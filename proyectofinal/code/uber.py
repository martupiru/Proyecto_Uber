#PROYECTO LARICCHIA Y NAHMAN
from dictionary import *
from graph import *
import pickle
import re


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

#Hash Ubi Fijas
H_Ubi_Fija= CreateHashTable(65)
with open("Hash_Ubicaciones.pk", "wb") as HashFileUbicaciones:
    pickle.dump(H_Ubi_Fija,HashFileUbicaciones)

#Hash Personas
H_Personas= CreateHashTable(65)
with open("Hash_Personas.pk", "wb") as HashFilePersonas:
    pickle.dump(H_Personas,HashFilePersonas)

#Hash Autos
H_Autos= CreateHashTable(65)
with open("Hash_Autos.pk", "wb") as HashFileAutos:
    pickle.dump(H_Autos,HashFileAutos)


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
    print("AAAAAAAAAAAAAA")
    printHashTable(Hash_Distancias)


def load_fix_element(lugar): #lugar:<nombre,direccion>
    #verificar que exista la direccion (grafo)
    with open("Mapa.pk", "rb") as MapaFile:
        Maph=pickle.load(MapaFile)
    exist = check_direccion(Maph,lugar[1])
    if exist == False:
        print("Esa direccion no existe")
    else:
        #si la direccion existe hacemos lo siguiente:
        if lugar[0][0] not in ["H", "h", "A", "a", "T", "t", "S", "s", "E", "e", "K", "k", "I", "i"]:
            print("El nombre ingresado no es válido")
        else:
            with open("Hash_Ubicaciones.pk", "rb") as HashFileUbicaciones:
                HashUbi=pickle.load(HashFileUbicaciones)
            #si no se encuentra el nombre repetido se agrega a la hash
            new_name = search_nombre(HashUbi,lugar)
            if new_name != None:
                cargar_new_element_hash(HashUbi,new_name,lugar)
                with open("Hash_Ubicaciones.pk", "wb") as HashFileUbicaciones:
                    pickle.dump(HashUbi,HashFileUbicaciones)
        

def load_movil_element(ubimovil): #ubomovil: <nombre, dirección, monto>
    #verificar que exista la direccion (grafo)
    with open("Mapa.pk", "rb") as MapaFile:
        Maph=pickle.load(MapaFile)
    exist = check_direccion(Maph,ubimovil[1])
    if exist == False:
        print("Esa direccion no existe")
    else:
        if ubimovil[0][0] == "C" or ubimovil[0][0] == "c":
            with open("Hash_Autos.pk", "rb") as HashFileAutos:
                HashAutos=pickle.load(HashFileAutos)
            #si no se encuentra el nombre repetido se agrega a la hash
            new_name = search_nombre(H_Autos,ubimovil) 
            if new_name != None:
                cargar_new_element_hash(HashAutos,new_name,ubimovil)
                with open("Hash_Autos.pk", "wb") as HashFileAutos:
                    pickle.dump(HashAutos,HashFileAutos)
            
        elif ubimovil[0][0] == "P" or ubimovil[0][0] == "p":
            with open("Hash_Personas.pk", "rb") as HashFilePersonas:
                HashPersonas=pickle.load(HashFilePersonas)
            #si no se encuentra el nombre repetido se agrega a la hash
            new_name = search_nombre(H_Personas,ubimovil) 
            if new_name != None:
                cargar_new_element_hash(HashPersonas,new_name,ubimovil)
                with open("Hash_Personas.pk", "wb") as HashFilePersonas:
                    pickle.dump(HashPersonas,HashFilePersonas)
        else:
            print("El nombre ingresado no es válido")

def create_trip(persona,elemento):
    #chequeamos que la entrada elemento sea una direccion o un nombre de direcciones
    if isinstance(elemento, str):
        direccion = search_direccion(H_Ubi_Fija,elemento)
    elif isinstance(elemento, tuple):
        direccion = elemento
        #validar que esa direccion exista
    else:
        print("El tipo de entrada no es válido")
    
    #if direccion != None:

