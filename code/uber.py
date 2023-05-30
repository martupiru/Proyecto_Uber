#PROYECTO LARICCHIA Y NAHMAN
from dictionary import *
import pickle

#Hash Ubi Fijas
H_Ubi_Fija= CreateHashTable(65)
#Hash Personas
H_Personas= CreateHashTable(65)
#Hash Autos
H_Autos= CreateHashTable(65)

def load_fix_element(lugar): #lugar:<nombre,direccion>
    #verificar que exista la direccion (grafo)
    #si la direccion existe hacemos lo siguiente:
    if lugar[0][0] not in ["H", "h", "A", "a", "T", "t", "S", "s", "E", "e", "K", "k", "I", "i"]:
        print("El nombre ingresado no es válido")
    else:
        #si no se encuentra el nombre repetido se agrega a la hash
        search_nombre(H_Ubi_Fija,lugar)

def load_movil_element(ubimovil): #ubomovil: <nombre, dirección, monto>
    #verificar que exista la direccion (grafo)
    if ubimovil[0][0] == "C" or ubimovil[0][0] == "c":
        #si no se encuentra el nombre repetido se agrega a la hash
        search_nombre(H_Autos,ubimovil) 
    elif ubimovil[0][0] == "P" or ubimovil[0][0] == "p":
        #si no se encuentra el nombre repetido se agrega a la hash
        search_nombre(H_Personas,ubimovil) 
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

