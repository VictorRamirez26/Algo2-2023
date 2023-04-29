import graph

print("-"*5 , "Grafo 1" ,"-"*5)
#Grafo 1 : Existe un camino entre el V3 y el V4
vertices = [1 , 2 , 3 , 4]
arista = [(1 , 2), (2 ,3), (4,2), (1,4)]
grafo = graph.Graph(vertices)
new_graph = grafo.createGraph(vertices , arista)
grafo.print_graph(new_graph)
print("Existe camino?: " , grafo.existPath(new_graph , 3 , 4)) 
print("Grafo conexo?: ", grafo.isConnected(new_graph))

print("-"*5 , "Grafo 2" ,"-"*5)
#Grafo 2: No existe un camino entre el V3 y el V2
vertices = [1 , 2 , 3 , 4]
arista = [(1 , 2), (4,2), (1,4)]
grafo2 = graph.Graph(vertices)
new_graph2 = grafo.createGraph(vertices , arista)
grafo.print_graph(new_graph2)
print("Existe camino?: " , grafo.existPath(new_graph2 , 3 , 2)) 
print("Grafo conexo?: ", grafo.isConnected(new_graph2))

print("-"*5 , "Grafo 3" ,"-"*5)
#Grafo 3: Existe un camino entre V1 y el mismo
vertices = [1 , 2 , 3 , 4]
arista = [(1 , 1)]
grafo3 = graph.Graph(vertices)
new_graph3 = grafo.createGraph(vertices , arista)
grafo.print_graph(new_graph3)
print("Existe camino?: " , grafo.existPath(new_graph3 , 1 , 1)) 
print("Grafo conexo?: ", grafo.isConnected(new_graph3))

print("-"*5 , "Grafo 4" ,"-"*5)
#Grafo 4 : Son 2 subgrafos conexos, pero el grafo en si es NO conexo
vertices = [1 , 2 , 3 , 4 , 5]
arista = [(1 , 2) , (1 , 3) , (2 , 3)  , (4 , 5)]
grafo4 = graph.Graph(vertices)
new_graph4 = grafo.createGraph(vertices , arista)
grafo.print_graph(new_graph4)
print("Existe camino?: " , grafo.existPath(new_graph4 , 1 , 5)) 
print("Existe camino?: " , grafo.existPath(new_graph4 , 1 , 4)) 
print("Grafo conexo?: ", grafo.isConnected(new_graph4))

