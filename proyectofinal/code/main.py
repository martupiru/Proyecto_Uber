from dictionary import *
from uber import *
lugar=("H3",(('e1',5),('e2',10)))
#lugar2=("2", "diree")
load_fix_element(lugar) 
#load_fix_element(lugar2)
print("UBICACIONEES")
#printHashTable(H_Ubi_Fija)
ubimovil=("P2",(('e4',5),('e5',10)))
#ubimovil2=("c1", "direcccion",268)
#ubimovil3=("m2","direee", 365)
#load_movil_element(ubimovil)
#printHashTable(ubimovil)
#load_movil_element(ubimovil2)
#load_movil_element(ubimovil3)


#print(hash_terna(ubimovil2,1000))
#serializar()
#create_trip('P2','H3')



with open("Hash_Personas.pk", "rb") as HashFilePersonas:
    a=pickle.load(HashFilePersonas)
printHashTable(a)