def createGraph(LA,LV):
    l_ady=[]
    for vertices in LV:
        lis=[]
        lis.append(vertices)
        l_ady.append(lis)
    for vertice in l_ady:
    #recorremos los vertices
        for aristas in LA:
            vertice[0]
            if vertice[0]==aristas[0]:
                tuple=(aristas[1],aristas[2])
                vertice.append(tuple)
    return(l_ady)
