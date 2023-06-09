#PROYECTO LARICCHIA Y NAHMAN
from dictionary import *
from graph import *
import pickle
import re
from loud_elements import *
#-----------serializar_fichero--------------
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
#----------------------------------------------------------------
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

#---------------------------------------------------------------
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
        #------personas------
        elif ubimovil[0][0] == "P" or ubimovil[0][0] == "p":
            H_Personas=load_hash_table_Personas()
            modify_hash_table_Personas(H_Personas,ubimovil)
            
        else:
            print("El nombre ingresado no es válido")
#-----------------------------------------------------------------------------------
#---------------Create_trip-------------------------
def create_trip(persona,elemento): #elemento=direccion o nombre direccion fija
    direccion_persona=validar_entradas_create_trip(persona,elemento)[0]
    direccion_destino=validar_entradas_create_trip(persona,elemento)[1]
    if direccion_destino !=None:
        hash_autos=load_hash_table_Autos()
        list_autos=load_lista_Autos()
        tupla_sentido_persona=verificar_sentido(direccion_persona)
        search_auto_lista (hash_autos,list_autos,tupla_sentido_persona)
        


def verificar_sentido(direccion):
    cont=0
    mapa=load_map()
    esquina1=direccion[0][0]
    esquina2=direccion[1][0]
    if esquina1 in mapa:
        for i in range(len(mapa[esquina1])):
            if esquina2 in mapa[esquina1][i]:
                #print(f"La arista entre {esquina1} y {esquina2} es dirigida de {esquina1} a {esquina2}")
                cont+=1
                arista=(esquina1,esquina2)
    if esquina2 in mapa :
        for i in range(len(mapa[esquina2])):
            if esquina1 in mapa[esquina2][i]:
                #print(f"La arista entre {esquina1} y {esquina2} es dirigida de {esquina2} a {esquina1}")
                cont+=1
                arista=(esquina2,esquina1)
    if cont==1:
        return((1,arista))
    elif cont==2:
        #print('doble sentido')
        return((2,arista))


def search_auto_lista (hash_autos,list_autos,tupla_sentido_persona): 
    for i in range (len(list_autos)):
        auto = list_autos [i]
        #calculamos hash_key al auto
        hash_key_auto = hash_subcadena(auto,len(hash_autos))
        #obtenemos los datos del auto mediante el search
        datos_Auto = search_hash_autos(hash_autos,auto,hash_key_auto) #devuelve una tupla con:(direccion,monto)
        direccion_auto = datos_Auto[0]
        monto_auto = datos_Auto[1]
        
        tupla_sentido_auto=verificar_sentido(direccion_auto)
        
        #!!!!!LLAMAR FUNCION DONDE EVALUAREMOS LOS CASOS
        #RECIBIRA: (tupla_sentido_persona,tupla_sentido_auto)
        
        #retornara: camino mas corto con su monto
        #se agrega a la lista
def casos_recorridos(tupla_sentido_persona,tupla_sentido_auto):
    hash_distancias=load_hash_table_distancias()
    if tupla_sentido_auto[0]==1 and tupla_sentido_persona[0]==1:
        
        esquinas=(tupla_sentido_auto[1][1],tupla_sentido_persona[1][0])#esquina por la q pasa el auto,esquina anterior a la persona
        distancia=search_hash_distancias(hash_distancias,esquinas)
        return distancia
    elif tupla_sentido_auto[0]==1 and tupla_sentido_persona[0]==2:
        #caso1
        #return((2,arista))
        esquinas1=(tupla_sentido_auto[1][1],tupla_sentido_persona[1][0])
        esquinas2=(tupla_sentido_auto[1][1],tupla_sentido_persona[1][1])
        distancia1=search_hash_distancias(hash_distancias,esquinas1)
        distancia2=search_hash_distancias(hash_distancias,esquinas2)
        if distancia1>distancia2:
            return distancia2
        elif distancia1<distancia2: return distancia1
        else:
            ff=0
        #tener en cuenta q vamos a hacer cuando las distancias sean ==
    elif tupla_sentido_auto[0]==2 and tupla_sentido_persona[0]==1:
        esquinas1=(tupla_sentido_auto[1][0],tupla_sentido_persona[1][0])
        esquinas2=(tupla_sentido_auto[1][1],tupla_sentido_persona[1][0])
        distancia1=search_hash_distancias(hash_distancias,esquinas1)
        distancia2=search_hash_distancias(hash_distancias,esquinas2)
        if distancia1>distancia2:
            return distancia2
        elif distancia1<distancia2: return distancia1
        else:
            ff
    elif tupla_sentido_auto[0]==2 and tupla_sentido_persona[0]==2:  
        esquinas1=(tupla_sentido_auto[1][0],tupla_sentido_persona[1][0])
        esquinas2=(tupla_sentido_auto[1][1],tupla_sentido_persona[1][0])
        esquinas3=(tupla_sentido_auto[1][0],tupla_sentido_persona[1][1])
        esquinas4=(tupla_sentido_auto[1][1],tupla_sentido_persona[1][1])
        distancia1=search_hash_distancias(hash_distancias,esquinas1)
        distancia2=search_hash_distancias(hash_distancias,esquinas2)
        distancia3=search_hash_distancias(hash_distancias,esquinas3)
        distancia4=search_hash_distancias(hash_distancias,esquinas4)
        

    #salmios del for
    #recorremos y evaluamos el monto si no lo puede pagar se elimina de la lista
    #ordenamos la lista por camino mas corto
    #devolvemmos los tres primeros elementos de la lista
    #panel interactivo (si o no viaje)

#Dada una key buscamos los elementos
def search_hash_autos(hash_autos,auto,key):
    for elemento in hash_autos[key]: #slot de la hash:(hk,(nombre_auto,direccion,monto))
        if elemento[1][0] == auto: #si coinciden hago lo siguiente
            direc_auto = elemento[1][1]
            monto_auto = elemento[1][2]
            tuple = (direc_auto,monto_auto)
            return(tuple)


    
def validar_entradas_create_trip(persona,elemento):
    #chequeamos que la entrada elemento sea una direccion o un nombre de direcciones
    HashPersonas=load_hash_table_Personas()
    if (search_exist_nombre(HashPersonas,persona))==None: #si existe elemento devuelve none
        direc_persona=search_direccion(HashPersonas,persona)
        exist_person=True
        if isinstance(elemento, str): #verifica que el elemento sea str
            HashUbi=load_hash_table_ubicaciones()
            direccion_destino = search_direccion(HashUbi,elemento)
            exist_direccion=True
        elif isinstance(elemento, tuple): #verifica que el elemento sea tupla
            direccion_destino = elemento
            #validar que esa direccion exista
            with open("Mapa.pk", "rb") as MapaFile:
                Maph=pickle.load(MapaFile)
            exist_direccion = check_direccion(Maph,direccion_destino)
            if exist_direccion == False:
                print("Esa direccion no existe")
        else:
            print("El tipo de entrada no es válido")
    else:
        print('No existe la persona con la que desea cargar el viaje')
        exist_person=False
    if (exist_person==True) and (exist_direccion==True):
        return ((direc_persona,direccion_destino))
    else:
        return None


