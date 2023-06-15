
import pickle
from dictionary import *
def load_map():
    # Carga la hash desde el archivo "Hash_Ubicaciones.pk"
    with open("Mapa.pk", "rb") as MapaFile:
        Maph=pickle.load(MapaFile)
    return Maph

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
    create_list_autos()
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
        new_name = search_exist_nombre(H_Autos,ubimovil[0])
        if new_name != None:
            cargar_new_element_hash(H_Autos,new_name,ubimovil)
            list_autos=load_lista_Autos()
            #cargar auto a la lista de autos!!!
            list_autos.append(ubimovil[0]) #guardamos solo el nombre del auto en la lista 
            #guardar en el listaautos.pk
            save_list_autos(list_autos)
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
        new_name = search_exist_nombre(H_Personas,ubimovil[0])
        if new_name != None:
            cargar_new_element_hash(H_Personas,new_name,ubimovil)
            save_hash_table_Personas(H_Personas)
        else:
            print("Ya existe un elemento con ese nombre")
#--------------------------------------------------------------------------------
def load_hash_table_distancias():
    # Carga la hash desde el archivo "Hash_Ubicaciones.pk"
    with open("Hash_Distancias.pk", "rb") as fichero:
        H_distancias = pickle.load(fichero)
    return H_distancias

#----Funciones para Cargar/modificar/guardar lista de nombres de autos----
def create_list_autos():
    # Crea una nueva lista
    list_autos= []
    save_list_autos(list_autos)
    return list_autos

def save_list_autos(list_autos):
     # Guarda la hash en el archivo "Hash_Ubicaciones.pk"
    with open("List_autos.pk", "wb") as HashFileUbicaciones:
        pickle.dump(list_autos,HashFileUbicaciones)
   
def load_lista_Autos():
    # Carga la hash desde el archivo "Lista_autos.pk"
    with open("List_autos.pk", "rb") as fichero:
        list_autos = pickle.load(fichero)
    return list_autos
#--------------------------------------------------------------