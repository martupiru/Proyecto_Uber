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
    for i in range (len(k)):
        sum = ord(k[i])*(10**i)
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
    hash_dupla=hash_terna(esquinas,len(hash_distancias))
    index = hash_dupla
    #elemento=[hash_key,(e1,e8,distancia)]
    for elemento in hash_distancias[index]:
        if elemento[1][0]==esquinas[0]:
            if elemento[1][1]==esquinas[1]:
                return elemento[1][2] #distancia del camino mas corto entre las dos esquinas

def cargar_new_element_hash(D,key,elemento):
    if D[key]==None:
        list=[]
        tupla=(key,elemento)
        list.append(tupla)
        D[key]=list
    else:
        tupla=(key,elemento)
        D[key].append(tupla)

def search_exist_nombre(D,elemento): #elemento=(lugar,direccion)
    hash_new_name=hash_subcadena(elemento,len(D))
    if search(D,hash_new_name)!= None:
        #Ya existe un elemento con ese nombre"
        return None
    else:
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