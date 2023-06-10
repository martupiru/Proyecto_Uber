#PROYECTO LARICCHIA Y NAHMAN
from dictionary import *
from graph import *
from loud_elements import *
from trip import *
import pickle
import re

#---------------------------serializar fichero---------------------------------
def serializar(path):
    #preguntar argumentos de la funcion con path
    with open(path, 'r') as archivo:
        lineas = archivo.readlines()
    #vertices
    lista = [elem[0:] for elem in lineas[0][1:-1].split('{' ) if elem.startswith('e')]
    lista[0] = [elem.replace('}', '') for elem in lista]   
    vertices = lista[0][0].strip("[]'").split(',')
    #ver bien como funciona!!!!!
    #aristas
    ternas = re.findall(r'<(.*?),(.*?),(.*?)>', lineas[1])
    aristas = [(elem[0], elem[1], int(elem[2])) for elem in ternas]

    graph = cargar_grafo(vertices, aristas)
    with open("Mapa.pk", "wb") as MapaFile:
        pickle.dump(graph,MapaFile)

#--------------------------cargar hash distancias-----------------------------
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

#------------------------- cargar ubicaciones fijas---------------------------
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
            new_name = search_exist_nombre(HashUbi,lugar[0])
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
            save_hash_table_Autos(H_Autos)
        #------personas------
        elif ubimovil[0][0] == "P" or ubimovil[0][0] == "p":
            H_Personas=load_hash_table_Personas()
            modify_hash_table_Personas(H_Personas,ubimovil)
            save_hash_table_Personas(H_Personas)
        else:
            print("El nombre ingresado no es válido")

#-----------------------------------------------------------------------------------

def create_trip(persona,elemento): #elemento=direccion o nombre direccion fija
    direccion_persona=validar_entradas_create_trip(persona,elemento)[0]
    direccion_destino=validar_entradas_create_trip(persona,elemento)[1]
    hash_personas =load_hash_table_Personas()
    monto_persona=search_monto_personas(hash_personas,persona)
    if direccion_destino !=None:
        hash_autos=load_hash_table_Autos()
        list_autos=load_lista_Autos()
        tupla_sentido_persona=verificar_sentido(direccion_persona)
        ranking=search_auto_lista(monto_persona,hash_autos,list_autos,tupla_sentido_persona,direccion_persona)
        if len(ranking)!=0:
            print('Ranking autos: ',)
            for node in ranking:
                print('Auto: ', node[0], '\ndistancia: ', node[1], '\ncosto de viaje: ', node[2], '\n----------')
        
        #CAMINO MAS CORTO PARA LLEGAR A DESTINO
            tupla_sentido_destino=verificar_sentido(direccion_destino)
            distancia_destino=casos_recorridos(tupla_sentido_persona,tupla_sentido_destino,direccion_persona,direccion_destino)
            print('La distancia a su destino es: ',distancia_destino)
            realiza_viaje=input('Indique si va a relizar el viaje (Si/No)').lower()
            if realiza_viaje=='si':
                entrada_valida=False
                while entrada_valida==False:
                    auto_elegido= input('Elija un auto: ').lower()
                    for node in ranking:
                        if auto_elegido==node[0].lower():
                            entrada_valida=True
                            monto_total_viaje = node[2]
                        else:
                            print('Ingrese el auto correctamente')
                #TELETRANSPORTAR 
                #UPDATE_DIRECCION HASH PERSONA (persona,nueva_direccion,costo) 
                new_monto_persona = monto_persona - monto_total_viaje
                update_hash_personas(hash_personas,persona,direccion_destino,new_monto_persona)
                #UPDATE_DIRECCION HASH AUTO ()
                update_hash_autos(hash_autos,auto_elegido,direccion_destino)
            elif realiza_viaje==('no'):
                print('Viaje rechazado')
        else:
            print('No hay autos para su viaje')
