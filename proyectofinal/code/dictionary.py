

def CreateHashTable(Dim):
    Hash=[]
    #crea un Hash de M posciones
    for i in range (0,Dim):
        L=[]
        Hash.append(L)
    return Hash

def printHashTable(D):
    count=0
    for each in D:
        print("[",count,"]","--->",end="")
        print(each)
        print("----")
        count+=1
        

def search(D,key):
    index=key
    for elemento in D[index]:
        if elemento[0]==key:
            return (elemento[1])
        else: return None


                
#######FUNCIONES ESPECIALES UBER#############
#Hash Key 
def hash_subcadena(k,m):
    sum=0
    for i in range (len(k)):
        sum = sum+ord(k[i])*(10**i)
    return(sum%m)

def hash_terna(terna,m):
    sum1=0
    sum2=0
    for i in range (0,len(terna[0])):
        sum1=ord(terna[0][i])*(10**i+1)
    for i in range (0,len(terna[1])):
        sum2=ord(terna[1][i])*(10**i+1)
    #
    sum=sum1+sum2
    #sum=sum1+sum2+terna[2]
    return(sum%m)

def search_hash_distancias(hash_distancias,esquinas):#esquinas= dupla de esquinas ej. (e1,e8)
   #calcular el hash a la dupla
   if esquinas[0]==esquinas[1]:
        distancia=0
        lista_visitados=[esquinas[0]]
        return distancia, lista_visitados
   else:
        hash_dupla=hash_terna(esquinas,len(hash_distancias))
        index = hash_dupla
        #elemento=[hash_key,((e1,e8,distancia),(lista_visitados))]
        for elemento in hash_distancias[index]:
            dupla = elemento[1]
            if dupla[0][0]==esquinas[0]:
                if dupla[0][1]==esquinas[1]:
                    distancia = dupla[0][2] #distancia del camino mas corto entre las dos esquinas
                    lista_visitados = dupla[1] #lista de nodos por los que hay que pasar para llegar del nodo inicio al nodo fin
                    if esquinas[1] not in lista_visitados:
                        lista_visitados.append(esquinas[1])
                    return distancia, lista_visitados

def cargar_new_element_hash(D,key,elemento):
    if D[key]==None:
        list=[]
        tupla=(key,elemento)
        list.append(tupla)
        D[key]=list
    else:
        tupla=(key,elemento)
        D[key].append(tupla)

def search_exist_nombre(D,nombre): #nombre= persona/auto
    hash_new_name=hash_subcadena(nombre,len(D))
    for elemento in D[hash_new_name]:
        if elemento[1][0]==nombre:
            #el elemento ya existe, retornamos none
            hash_new_name = None
    return hash_new_name 
        
def search_direccion(D,nombre): #Conocer, dado un lugar, persona o auto la dirección del mismo
    hash_new_name=hash_subcadena(nombre,len(D))
    index = hash_new_name
    try:
        for elemento in D[index]:
            if elemento[1][0]==nombre:
                return (elemento[1][1])
    except:
        return None

#Dada una key buscamos los elementos
def search_hash_autos(hash_autos,auto,key):
    for elemento in hash_autos[key]: #slot de la hash:(hk,(nombre_auto,direccion,monto))
        if elemento[1][0] == auto: #si coinciden hago lo siguiente
            direc_auto = elemento[1][1]
            monto_auto = elemento[1][2]
            tuple = (direc_auto,monto_auto)
            return(tuple)

#dada una persona retornar su monto
def search_monto_personas(hash_personas,persona):
    hash_name=hash_subcadena(persona,len(hash_personas))
    for elemento in hash_personas[hash_name]:
        if elemento [1][0] == persona:
            return (elemento[1][2])
        
#dado un auto, actualizamos su la direccion en la que se encuentra
def update_hash_autos(hash_autos,auto,new_direccion):
    hash_key_auto = hash_subcadena(auto,len(hash_autos))
    for elemento in hash_autos[hash_key_auto]:
        if elemento[1][0] == auto:
            #actualizamos la direccion
            elemento[1][1] = new_direccion



def delete(D,key):
    index=key
    for i in range (len(D[index])):
        if D[index][i][0]==key:
                D[index].pop(i)
                




