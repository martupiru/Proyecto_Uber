
import pickle
from loud_elements import *

def verificar_sentido(direccion):
    cont=0
    mapa=load_map()
    try:
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
            #doble sentido
            return((2,arista))
    except: 
        return None

def check_direccion(mapa,direccion):#Hay que cambiarlo para la entrada pueda ser como dijo el profe xd
    #chequear el sentido
    tupla_sentido=verificar_sentido(direccion) #(1/2,arista con esquinas en sentido de la calle)
    if tupla_sentido !=None:
        esquina1 = tupla_sentido[1][0]
        esquina2 = tupla_sentido[1][1]
        flag = True

        peso_a_buscar= int(direccion[0][1])+int(direccion[1][1])
        try:
            #verificar que la esquina 1 existe en el mapa
            adyacentes = mapa[esquina1]
        except:
            flag = False
        if flag == True:
            try:
                #verificar que la esquina 2 sea el otro vertice de esa arista
                for i in range (len(adyacentes)):
                    if adyacentes[i][0] == esquina2:
                        if adyacentes[i][1]==peso_a_buscar:
                            flag = True 
                            return flag #que corte ahi  
                        else:
                            flag=False
                    else:
                        flag = False
            except: 
                flag = False
        return flag
    else: 
        print("Esa direccion no es válida")

        
def search_auto_lista(monto_persona,hash_autos,list_autos,tupla_sentido_persona,direccion_persona): 
    lista_ranking=[]
    for i in range (len(list_autos)):
        auto = list_autos [i]
        #calculamos hash_key al auto

        hash_key_auto = hash_subcadena(auto,(len(hash_autos)))
        #obtenemos los datos del auto mediante el search
        datos_Auto = search_hash_autos(hash_autos,auto,hash_key_auto) #devuelve una tupla con:(direccion,monto)
        direccion_auto = datos_Auto[0]
        monto_auto = datos_Auto[1]
        #si la persona no puede pagar el costo del auto, el auto no rankea
        if monto_persona>monto_auto:
            tupla_sentido_auto = verificar_sentido(direccion_auto)
            distancia,camino=casos_recorridos(tupla_sentido_persona,tupla_sentido_auto,direccion_persona,direccion_auto)
            monto_total_viaje=(distancia+monto_auto)/4
            #si la persona no puede pagar el viaje no se agrega a la lista
            if monto_total_viaje<=monto_persona:
                terna_ranking=(auto,distancia,monto_total_viaje)
                lista_ranking.append(terna_ranking)
    list_ranking_ordenada=sorted(lista_ranking,key=lambda terna: terna[1])
    ranking=list_ranking_ordenada[:3] #cortara la lista a los primero 3
    return ranking


# #solo tenemos que acceder si es posible el recorrido
def distancia_total_recorrido(esquinas,hash_distancias,tupla_persona,tupla_auto,direccion_persona,direccion_auto):
#esquina por la q pasa el auto,esquina anterior a la persona
    distancia_n,visitados=search_hash_distancias(hash_distancias,esquinas) #cambio en el search
    if esquinas[0]==direccion_auto[0][0]: #esquina auto
        na=direccion_auto[0][1]
    elif esquinas[0]==direccion_auto[1][0]:
        na=direccion_auto[1][1]
    if esquinas[1]==direccion_persona[0][0]:
        np=direccion_persona[0][1]
    elif esquinas[1]==direccion_persona[1][0]:
        np=direccion_persona[1][1]
    if distancia_n==None:
        distancia_n=0
    #print(distancia_n)
    distancia_total=distancia_n+na+np   
    #print(distancia_total)
    return(distancia_total)  

def casos_recorridos(tupla_sentido_persona,tupla_sentido_auto,direccion_persona,direccion_auto):
    hash_distancias=load_hash_table_distancias()
    #ambas calles son de un solo sentido
    tupla_persona=tupla_sentido_persona[1]
    tupla_auto=tupla_sentido_auto[1]

    #-------------CASO1-----------------------------
    if tupla_sentido_auto[0]==1 and tupla_sentido_persona[0]==1:
        esquina_auto=tupla_auto[1]
        esquina_persona=tupla_persona[0]
        esquinas=(esquina_auto,esquina_persona)
        #TENER EN CUENTA ENTODO
        distancia,camino=search_hash_distancias(hash_distancias,(esquina_auto,esquina_persona))
        distancia=distancia_total_recorrido(esquinas,hash_distancias,tupla_persona,tupla_auto,direccion_persona,direccion_auto)
        return distancia,camino
    #-----------funciona--------------------------------
        
    #-------------CASO2-----------------------------
    #calle del auto un solo sentido y calle de la persona doble sentido
    elif tupla_sentido_auto[0]==1 and tupla_sentido_persona[0]==2:
        #nodos
        esquina_auto=tupla_sentido_auto[1][1]
        esquina_persona1=tupla_sentido_persona[1][0]
        esquina_persona2=tupla_sentido_persona[1][1]

        #si las esquinas son las misma ya son el camino mas corto
        #verificar que que los recorridos no contengan al otro nodo
        distancia1,camino1=search_hash_distancias(hash_distancias,(esquina_auto,esquina_persona1))
        distancia2,camino2=search_hash_distancias(hash_distancias,(esquina_auto,esquina_persona2))

        if esquina_persona2 in camino1:
            #solo hacemos el recorrido con esquina 1
            esquinas1=(esquina_auto,esquina_persona2)
            distancia1=distancia_total_recorrido(esquinas1,hash_distancias,tupla_persona,tupla_auto,direccion_persona,direccion_auto)            
            return distancia1, camino2
        elif esquina_persona1 in camino2:
            #solo hacemos el recorrido con esquina 2
            esquinas2=(esquina_auto,esquina_persona1)
            distancia2=distancia_total_recorrido(esquinas2,hash_distancias,tupla_persona,tupla_auto,direccion_persona,direccion_auto)            
            return distancia2,camino1
        else:
            esquinas1=(esquina_auto,esquina_persona1)
            distancia1=distancia_total_recorrido(esquinas1,hash_distancias,tupla_persona,tupla_auto,direccion_persona,direccion_auto)
            esquinas2=(esquina_auto,esquina_persona2)
            distancia2=distancia_total_recorrido(esquinas2,hash_distancias,tupla_persona,tupla_auto,direccion_persona,direccion_auto)
            if distancia1>distancia2:

                return distancia2,camino2
            else : return distancia1,camino1
    #-----------funciona--------------------------------
    #-------------CASO3-----------------------------
    elif tupla_sentido_auto[0]==2 and tupla_sentido_persona[0]==1:
        #nodos
        esquina_auto1=tupla_sentido_auto[1][0]
        esquina_auto2=tupla_sentido_auto[1][1]
        esquina_persona=tupla_sentido_persona[1][0]
       
        #verificar que que los recorridos no contengan al otro nodo
        distancia1,camino1=search_hash_distancias(hash_distancias,(esquina_auto1,esquina_persona))
        distancia2,camino2=search_hash_distancias(hash_distancias,(esquina_auto2,esquina_persona))
        if esquina_auto1 in camino2:
            #solo hacemos el recorrido con esquina 1
            esquinas1=(esquina_auto1,esquina_persona)
            distancia1=distancia_total_recorrido(esquinas1,hash_distancias,tupla_persona,tupla_auto,direccion_persona,direccion_auto)            
            return distancia1,camino1
        elif esquina_auto2 in camino1:
            #solo hacemos el recorrido con esquina 2
            esquinas2=(esquina_auto2,esquina_persona)
            distancia2=distancia_total_recorrido(esquinas2,hash_distancias,tupla_persona,tupla_auto,direccion_persona,direccion_auto)            
            return distancia2,camino2
        else:
            esquinas1=(esquina_auto1,esquina_persona)
            distancia1=distancia_total_recorrido(esquinas1,hash_distancias,tupla_persona,tupla_auto,direccion_persona,direccion_auto)
            esquinas2=(esquina_auto2,esquina_persona)
            distancia2=distancia_total_recorrido(esquinas2,hash_distancias,tupla_persona,tupla_auto,direccion_persona,direccion_auto)
            if distancia1>distancia2:
                return distancia2,camino2
            else : return distancia1,camino1
    #-----------funciona----------------------------
    #-------------CASO4-----------------------------
    else:
        #tupla_sentido_auto[0]==2 and tupla_sentido_persona[0]==2
        #dos posibles nodos para el auto
        esquina_auto1=tupla_sentido_auto[1][0]
        esquina_auto2=tupla_sentido_auto[1][1]
        #dos posibles nodos para la persona
        esquina_persona1=tupla_sentido_persona[1][0]
        esquina_persona2=tupla_sentido_persona[1][1]


        distancia1,camino1=search_hash_distancias(hash_distancias,(esquina_auto1,esquina_persona1))
        distancia2,camino2=search_hash_distancias(hash_distancias,(esquina_auto2,esquina_persona1))
        distancia3,camino3=search_hash_distancias(hash_distancias,(esquina_auto1,esquina_persona2))
        distancia4,camino4=search_hash_distancias(hash_distancias,(esquina_auto2,esquina_persona2))

        if esquina_auto1 in camino2:
            
            esquinas1=(esquina_auto1,esquina_persona1)
            distancia1=distancia_total_recorrido(esquinas1,hash_distancias,tupla_persona,tupla_auto,direccion_persona,direccion_auto)              
            distancia2=None
        elif esquina_auto2 in camino1:
            
            esquinas2=(esquina_auto2,esquina_persona1)
            distancia2=distancia_total_recorrido(esquinas2,hash_distancias,tupla_persona,tupla_auto,direccion_persona,direccion_auto) 
            distancia1=None
        else:
            esquinas2=(esquina_auto2,esquina_persona1)
            distancia2=distancia_total_recorrido(esquinas2,hash_distancias,tupla_persona,tupla_auto,direccion_persona,direccion_auto)
            esquinas1=(esquina_auto1,esquina_persona1)
            distancia1=distancia_total_recorrido(esquinas1,hash_distancias,tupla_persona,tupla_auto,direccion_persona,direccion_auto)
        
        if esquina_auto2 in camino3:
            esquinas4=(esquina_auto2,esquina_persona2)
            distancia4=distancia_total_recorrido(esquinas4,hash_distancias,tupla_persona,tupla_auto,direccion_persona,direccion_auto)              
            distancia3=None

        elif esquina_auto1 in camino4:
            esquinas3=(esquina_auto1,esquina_persona2)
            distancia3=distancia_total_recorrido(esquinas3,hash_distancias,tupla_persona,tupla_auto,direccion_persona,direccion_auto)              
            distancia4=None
        else:
            esquinas4=(esquina_auto2,esquina_persona2)
            distancia4=distancia_total_recorrido(esquinas4,hash_distancias,tupla_persona,tupla_auto,direccion_persona,direccion_auto)
            esquinas3=(esquina_auto1,esquina_persona2)
            distancia3=distancia_total_recorrido(esquinas3,hash_distancias,tupla_persona,tupla_auto,direccion_persona,direccion_auto)
        distacias=[distancia1,distancia2,distancia3,distancia4]
        distacias_validas = [elem for elem in distacias if elem is not None]
        distacias_validas.sort()
        if distancia1!=None and distacias_validas[0]==distancia1:
            return distancia1,camino1
        elif distancia2!=None and distacias_validas[0]==distancia2:
            return distancia2,camino2
        elif distancia3!=None and distacias_validas[0]==distancia3:
            return distancia3,camino3
        elif distancia4!=None and distacias_validas[0]==distancia4:
            return distancia4,camino4

    #---------------------------------------

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
