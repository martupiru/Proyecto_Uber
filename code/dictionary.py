#TP HASH TABLE NAHMAN MARTINA L:13685

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
        
#haski
#def hash_mode(k,m):
#    return (k%m)

def hash_subcadena(k,m):
    for i in range (len(k)):
        sum = ord(k[i])*(10**i)
    return(sum%m)


"""def insert(D,key,value):
    if len(D)==0 or D==None:
        print("crear tabla hash con la funcion CreateHashTable")
        return None
    else:
        index=hash_mode(key,len(D))
        if D[index]==None:
            list=[]
            tupla=(key,value)
            list.append(tupla)
            D[index]=list
        else:
            tupla=(key,value)
            D[index].append(tupla)"""
            
def search(D,key):
    index=key
    for elemento in D[index]:
        if elemento[0]==key:
            return (elemento[1])

"""def delete (D,key):
    if search(D,key)!=None:
        index=hash_mode(key,len(D))
        for i in range (len(D[index])):
            if D[index][i][0]==key:
                #pop elimina el elemento
                D[index].pop(i)
                return D"""
                
#######FUNCIONES ESPECIALES UBER#############
def cargar_new_element_hash(D,key,elemento):
    if D[key]==None:
        list=[]
        tupla=(key,elemento)
        list.append(tupla)
        D[key]=list
    else:
        tupla=(key,elemento)
        D[key].append(tupla)

def search_nombre(D,elemento):
    hash_new_name=hash_subcadena(elemento[0],len(D))
    if search(D,hash_new_name)!= None:
        print("Ya existe un elemento con ese nombre")
    else:
        cargar_new_element_hash(D,hash_new_name,elemento)

def search_direccion(D,nombre): #Conocer, dado un lugar, persona o auto la dirección del mismo
    hash_new_name=hash_subcadena(nombre,len(D))
    index = hash_new_name
    for elemento in D[index]:
        if elemento[1][0]==nombre:
            return (elemento[1][1])
