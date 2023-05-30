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
    if lugar[0][0] != ("H" or "h" or "A" or "a" or "T" or "t" or "S" or "s" or "E" or"e" or "K" or "k" or "I" or "i"):
        print("El nombre ingresado no es válido")
    else:
        #si no se encuentra el nombre repertido se agrega a la hash
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









