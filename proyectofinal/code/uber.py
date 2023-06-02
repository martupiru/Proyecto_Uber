#PROYECTO LARICCHIA Y NAHMAN
from dictionary import *
import pickle

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


def load_fix_element(lugar): #lugar:<nombre,direccion>
    #verificar que exista la direccion (grafo)
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

