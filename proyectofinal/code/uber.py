#PROYECTO LARICCHIA Y NAHMAN
import pickle
import re
import sys
from graph import *
from trip import *

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
    print("Map created successfully")

#--------------------------cargar hash distancias-----------------------------
def cargar_mapa_hashD():
    #CUANDO LLAMEMOS A LA FUNCION LLENAR HASH DE DISTANCIAS:
    with open("Mapa.pk", "rb") as MapaFile:
        Maph=pickle.load(MapaFile)
    #Creamos Hash
    H_Distancias = CreateHashTable(419)
    #Llenamos Hash
    Hash_Distancias = llenar_hash_distancias(Maph,H_Distancias)
    #Serializamos la Hash Anterior
    with open("Hash_Distancias.pk", "wb") as HashFileDistancias:
        pickle.dump(Hash_Distancias,HashFileDistancias)
#--------------------cargar hash de todo---------------------------------------
def cargar_todo():
    create_hash_table_Autos(71)
    create_hash_table_Personas(71)
    create_hash_table_Ubi_Fij(71)

def create_map(path):
    #serializamos mapa
    serializar(path)
    #serializamos hash de distancias
    cargar_mapa_hashD()
    #serializamos hash personas/autos/ubicaciones
    cargar_todo()

#------------------------- cargar ubicaciones fijas---------------------------
def load_fix_element(lugar):
    HashUbi=load_hash_table_ubicaciones()
    # Realiza las modificaciones, cargar lugares 
    Maph=load_map()
    exist = check_direccion(Maph,lugar[1])
    if exist == False:
        print("Esa direccion no existe")
    else:
        #si la direccion existe hacemos lo siguiente:
        if len(lugar[0]) > 1:
            letra = lugar[0][0]
            numeros = lugar[0][1:]
           
            if letra.isalpha() and numeros.isdigit():
                if letra.lower() not in ["h", "a", "t", "s", "e", "k", "i"]:
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
    Maph=load_map()
    exist = check_direccion(Maph,ubimovil[1])
    if exist == False:
        print("Esa direccion no existe")
    else:
        #------autos------
        if ubimovil[0][0] == "C" :
            
            H_Autos=load_hash_table_Autos()
            modify_hash_table_Autos(H_Autos,ubimovil)
            save_hash_table_Autos(H_Autos)
        #------personas------
        elif ubimovil[0][0] == "P" :
            
            H_Personas=load_hash_table_Personas()
            modify_hash_table_Personas(H_Personas,ubimovil)
            save_hash_table_Personas(H_Personas)
        else:
            print("El nombre ingresado no es válido")

    # new_name = search_exist_nombre(HashUbi,lugar[0])
    # if new_name != None:
    #     cargar_new_element_hash(HashUbi,new_name,lugar)
    #     save_hash_table_ubicaciones(HashUbi)
#-----------------------------------------------------------------------------------

def update_hash_personas(hash_personas,persona,new_direccion,new_monto):
    hash_key_persona = hash_subcadena(persona,len(hash_personas))
    delete(hash_personas,hash_key_persona)
    save_hash_table_Personas(hash_personas)
    #cargar
    load_movil_element((persona,new_direccion,new_monto)) #ubimovil: <nombre, dirección, monto>

def update_hash_auto(hash_auto,auto,new_direccion,new_monto):
    hash_key_persona = hash_subcadena(auto,len(hash_auto))
    delete(hash_auto,hash_key_persona)
    save_hash_table_Autos(hash_auto)
    lista_autos=load_lista_Autos()

    print(len(lista_autos))
    print(lista_autos)

    long=(len(lista_autos))
    for i in range (long):
        if lista_autos[i]==auto:
            lista_autos[i]=None
    lista_autos = [elemento for elemento in lista_autos if elemento is not None]
    save_list_autos(lista_autos)
    load_movil_element((auto,new_direccion,new_monto))
    

def create_trip(persona,elemento): #elemento= direccion o nombre direccion fija
    try:
        direccion_persona=validar_entradas_create_trip(persona,elemento)[0]
        direccion_destino=validar_entradas_create_trip(persona,elemento)[1]

        hash_personas =load_hash_table_Personas()
        monto_persona=search_monto_personas(hash_personas,persona)

        if (direccion_destino !=None) and (direccion_persona!=None):

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
                distancia_destino,camino_destino=casos_recorridos(tupla_sentido_destino,tupla_sentido_persona,direccion_destino,direccion_persona)
                #delvolver camino
                print('La distancia a su destino es: ',distancia_destino)
                print('El camino a su destino es: ',camino_destino)
                realiza_viaje=input('Indique si va a relizar el viaje (Si/No)').lower()
                if realiza_viaje=='si':
                    entrada_valida=False
                    while entrada_valida==False:
                        auto_elegido= input('Elija un auto: ')
                        for node in ranking:
                            if auto_elegido==(node[0]):
                                entrada_valida=True
                                monto_total_viaje = node[2]
                            # else:
                            #     print('Ingrese el auto correctamente')
                    #TELETRANSPORTAR 
                    #UPDATE_DIRECCION HASH PERSONAS ()
                    new_monto_persona = monto_persona - monto_total_viaje
                    update_hash_personas(hash_personas,persona,direccion_destino,new_monto_persona)
                    #UPDATE_DIRECCION HASH AUTO ()
                    monto_auto=search_monto_personas(hash_autos,auto_elegido)
                    update_hash_auto(hash_autos,auto_elegido,direccion_destino,monto_auto)
                    print("Viaje realizado exitosamete")
                elif realiza_viaje==('no'):
                    print('Viaje rechazado')
            else:
                print('No hay autos para su viaje')
        else:
            print('No es posible este viaje')
    except:
        print('No es posible realizar el viaje')

#CONSOLA


def convertir_a_tupla(cadena):
    tuplas = re.findall(r'<(.*?),(.*?)>', cadena)
    tupla = tuple((terna[0], int(terna[1])) for terna in tuplas)
    return tupla

#load_movil_element(('P1',(('e6',15),('e7',5)),2000)) 
#python uber.py -load_movil_element P1 "<e8,10> <e10,40>" 2000


if sys.argv[1] == "-load_movil_element":
    try:
        direccion=convertir_a_tupla(sys.argv[3])
        ubimovil=(sys.argv[2],direccion,int(sys.argv[4]))
        load_movil_element(ubimovil)
    except:
        print('No es posible cargar el elemento')


#python uber.py -load_fix_element H1 "<e8,20> <e10,30>"
if sys.argv[1] == "-load_fix_element":
    try:
        direccion=convertir_a_tupla(sys.argv[3])
        lugar=(sys.argv[2],direccion)
        load_fix_element(lugar)
    except:
        print('No es posible cargar el elemento')

if sys.argv[1] == "-create_trip":

    try:
        if sys.argv[3][0].lower() in ["h", "a", "t", "s", "e", "k", "i"]:
            create_trip(sys.argv[2],sys.argv[3])
        else:
            tupla=convertir_a_tupla(sys.argv[3])
            create_trip(sys.argv[2],tupla)
        #funcion q convierta argv[2] q es H1 y argv[3] q es "<e8,20> <e10,30>" a tupla
    except:
        print('paramento invalido')
