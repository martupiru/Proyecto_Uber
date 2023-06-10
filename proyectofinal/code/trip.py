from dictionary import *
from loud_elements import *
from graph import *

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
            #print('doble sentido')
            return((2,arista))
    except: 
        print('Esa direccion no es valida')

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
        print('Direccion incorrecta')
        
def search_auto_lista(monto_persona,hash_autos,list_autos,tupla_sentido_persona,direccion_persona): 
    lista_ranking=[]
    for i in range (len(list_autos)):
        auto = list_autos [i]
        #calculamos hash_key al auto
        hash_key_auto = hash_subcadena(auto,len(hash_autos))
        #obtenemos los datos del auto mediante el search
        datos_Auto = search_hash_autos(hash_autos,auto,hash_key_auto) #devuelve una tupla con:(direccion,monto)
        direccion_auto = datos_Auto[0]
        monto_auto = datos_Auto[1]
        
        tupla_sentido_auto = verificar_sentido(direccion_auto)
        #!!!!!LLAMAR FUNCION DONDE EVALUAREMOS LOS CASOS
        #RECIBIRA: (tupla_sentido_persona,tupla_sentido_auto)
        distancia=casos_recorridos(tupla_sentido_persona,tupla_sentido_auto,direccion_persona,direccion_auto)
        monto_total_viaje=distancia+(monto_auto/4)
        #si la persona no puede pagar el viaje no se agrega a la lista
        if monto_total_viaje<=monto_persona:
            terna_ranking=(auto,distancia,monto_total_viaje)
            lista_ranking.append(terna_ranking)
    list_ranking_ordenada=sorted(lista_ranking,key=lambda terna: terna[1])
    ranking=list_ranking_ordenada[:3] #cortara la lista a los primero 3
    return ranking

        #se agrega a la lista
def distancia_total_recorrido(hash_distancias,tupla_sentido_persona,tupla_sentido_auto,direccion_persona,direccion_auto):
    esquinas=(tupla_sentido_auto[1][1],tupla_sentido_persona[1][0])#esquina por la q pasa el auto,esquina anterior a la persona
    distancia_n=search_hash_distancias(hash_distancias,esquinas)
    if tupla_sentido_auto[1][1]==direccion_auto[0][0]:
        na=direccion_auto[0][1]
    elif tupla_sentido_auto[1][1]==direccion_auto[1][0]:
        na=direccion_auto[1][1]
    if tupla_sentido_persona[1][0]==direccion_persona[0][0]:
        np=direccion_persona[0][1]
    elif tupla_sentido_persona[1][0]==direccion_persona[1][0]:
        np=direccion_persona[1][1]
    distancia_total=distancia_n+na+np       
    return(distancia_total)

def casos_recorridos(tupla_sentido_persona,tupla_sentido_auto,direccion_persona,direccion_auto):
    hash_distancias=load_hash_table_distancias()
    #ambas calles son de un solo sentido
    if tupla_sentido_auto[0]==1 and tupla_sentido_persona[0]==1:
        distancia=distancia_total_recorrido(hash_distancias,tupla_sentido_persona,tupla_sentido_auto,direccion_persona,direccion_auto)
        return distancia
    #calle del auto un solo sentido y calle de la persona doble sentido
    elif tupla_sentido_auto[0]==1 and tupla_sentido_persona[0]==2:
        distancia1=distancia_total_recorrido(hash_distancias,tupla_sentido_persona,tupla_sentido_auto,direccion_persona,direccion_auto)
        tupla_sentido_persona2=reversed(tupla_sentido_persona)
        distancia2=distancia_total_recorrido(hash_distancias,tupla_sentido_persona2,tupla_sentido_auto,direccion_persona,direccion_auto)
        if distancia1>distancia2:
            return distancia2
        else : return distancia1
    #calle del auto doble sentido y calle de la persona un sentido
    elif tupla_sentido_auto[0]==2 and tupla_sentido_persona[0]==1:
        distancia1=distancia_total_recorrido(hash_distancias,tupla_sentido_persona,tupla_sentido_auto,direccion_persona,direccion_auto)
        tupla_sentido_auto2=reversed(tupla_sentido_auto)
        distancia2=distancia_total_recorrido(hash_distancias,tupla_sentido_persona,tupla_sentido_auto2,direccion_persona,direccion_auto)
        if distancia1>distancia2:
            return distancia2
        else: return distancia1
    #ambas calles doble sentido
    elif tupla_sentido_auto[0]==2 and tupla_sentido_persona[0]==2:  
        distancia1=distancia_total_recorrido(hash_distancias,tupla_sentido_persona,tupla_sentido_auto,direccion_persona,direccion_auto)
        tupla_sentido_persona2=reversed(tupla_sentido_persona)
        distancia2=distancia_total_recorrido(hash_distancias,tupla_sentido_persona2,tupla_sentido_auto,direccion_persona,direccion_auto)
        tupla_sentido_auto2=reversed(tupla_sentido_auto)
        distancia3=distancia_total_recorrido(hash_distancias,tupla_sentido_persona,tupla_sentido_auto2,direccion_persona,direccion_auto)
        distancia4=distancia_total_recorrido(hash_distancias,tupla_sentido_persona2,tupla_sentido_auto2,direccion_persona,direccion_auto)  
        list_distancia=[distancia1,distancia2,distancia3,distancia4]
        list_distancia.sort
        return(list_distancia[0])

    #recorremos y evaluamos el monto si no lo puede pagar se elimina de la lista
    #ordenamos la lista por camino mas corto
    #devolvemmos los tres primeros elementos de la lista
    #panel interactivo (si o no viaje)
    
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
