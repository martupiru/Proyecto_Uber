from dictionary import *
from graph import *
import pickle

#----Funciones para Cargar/modificar/guardar tabla de ubicacione fijas----
def create_hash_table_Ubi_Fij(size):
    # Crea una nueva hash con el tamaño especificado
    H_Ubi_Fija= CreateHashTable(size)
    save_hash_table_ubicaciones(H_Ubi_Fija)
    return H_Ubi_Fija

def save_hash_table_ubicaciones(H_Ubi_Fija):
     # Guarda la hash en el archivo "Hash_Ubicaciones.pk"
    with open("Hash_Ubicaciones.pk", "wb") as HashFileUbicaciones:
        pickle.dump(H_Ubi_Fija,HashFileUbicaciones)
   
def load_hash_table_ubicaciones():
    # Carga la hash desde el archivo "Hash_Ubicaciones.pk"
    with open("Hash_Ubicaciones.pk", "rb") as fichero:
        HashUbi = pickle.load(fichero)
    return HashUbi

#----Funciones para Cargar/modificar/guardar tabla Autos----
def create_hash_table_Autos(size):
    # Crea una nueva hash con el tamaño especificado
    H_Autos= CreateHashTable(size)
    save_hash_table_Autos(H_Autos)
    return H_Autos

def save_hash_table_Autos(H_Autos):
     # Guarda la hash en el archivo "Hash_Ubicaciones.pk"
    with open("Hash_Autos.pk", "wb") as HashFileUbicaciones:
        pickle.dump(H_Autos,HashFileUbicaciones)
   
def load_hash_table_Autos():
    # Carga la hash desde el archivo "Hash_Ubicaciones.pk"
    with open("Hash_Autos.pk", "rb") as fichero:
        H_Autos = pickle.load(fichero)
    return H_Autos

def modify_hash_table_Autos(H_Autos,ubimovil):
    # Realiza las modificaciones, cargar autos 
        # Devuelve la hash modificada
        new_name = search_nombre(H_Autos,ubimovil)
        if new_name != None:
            cargar_new_element_hash(H_Autos,new_name,ubimovil)
            save_hash_table_Autos(H_Autos)
        else:
            print("Ya existe un elemento con ese nombre")
#----Funciones para Cargar/modificar/guardar tabla Personas----
def create_hash_table_Personas(size):
    # Crea una nueva hash con el tamaño especificado
    H_Personas= CreateHashTable(size)
    save_hash_table_Personas(H_Personas)
    return H_Personas

def save_hash_table_Personas(H_Personas):
     # Guarda la hash en el archivo "Hash_Ubicaciones.pk"
    with open("Hash_Personas.pk", "wb") as HashFileUbicaciones:
        pickle.dump(H_Personas,HashFileUbicaciones)
   
def load_hash_table_Personas():
    # Carga la hash desde el archivo "Hash_Ubicaciones.pk"
    with open("Hash_Personas.pk", "rb") as fichero:
        H_Personas = pickle.load(fichero)
    return H_Personas

def modify_hash_table_Personas(H_Personas,ubimovil):
    # Realiza las modificaciones, cargar autos 
        # Devuelve la hash modificada
        new_name = search_nombre(H_Personas,ubimovil)
        if new_name != None:
            cargar_new_element_hash(H_Personas,new_name,ubimovil)
            save_hash_table_Personas(H_Personas)
        else:
            print("Ya existe un elemento con ese nombre")
#--------------------------------------------------------------------------------