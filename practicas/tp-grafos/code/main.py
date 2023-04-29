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
print("Es un arbol?: " , grafo.isTree(new_graph))

print("-"*5 , "Grafo 2" ,"-"*5)
#Grafo 2: No existe un camino entre el V3 y el V2
vertices = [1 , 2 , 3 , 4]
arista = [(1 , 2), (4,2), (1,4)]
grafo2 = graph.Graph(vertices)
new_graph2 = grafo2.createGraph(vertices , arista)
grafo2.print_graph(new_graph2)
print("Existe camino?: " , grafo2.existPath(new_graph2 , 3 , 2)) 
print("Grafo conexo?: ", grafo2.isConnected(new_graph2))
print("Es un arbol?: " , grafo2.isTree(new_graph2))


print("-"*5 , "Grafo 3" ,"-"*5)
#Grafo 3: Existe un camino entre V1 y el mismo
vertices = [1 , 2 , 3 , 4]
arista = [(1 , 1)]
grafo3 = graph.Graph(vertices)
new_graph3 = grafo3.createGraph(vertices , arista)
grafo3.print_graph(new_graph3)
print("Existe camino?: " , grafo3.existPath(new_graph3 , 1 , 1)) 
print("Grafo conexo?: ", grafo3.isConnected(new_graph3))
print("Es un arbol?: " , grafo3.isTree(new_graph3))


print("-"*5 , "Grafo 4" ,"-"*5)
#Grafo 4 : Son 2 subgrafos conexos, pero el grafo en si es NO conexo
vertices = [1 , 2 , 3 , 4 , 5]
arista = [(1 , 2) , (1 , 3) , (2 , 3)  , (4 , 5)]
grafo4 = graph.Graph(vertices)
new_graph4 = grafo.createGraph(vertices , arista)
grafo4.print_graph(new_graph4)
print("Existe camino?: " , grafo4.existPath(new_graph4 , 1 , 5)) 
print("Existe camino?: " , grafo4.existPath(new_graph4 , 1 , 4)) 
print("Grafo conexo?: ", grafo4.isConnected(new_graph4))
print("Es un arbol?: " , grafo4.isTree(new_graph4))

print("-"*5 , "Grafo 5" ,"-"*5)
#Grafo conexo y aciclico (arbol)
vertices = [1 , 2 , 3 , 4]
arista = [(1 , 2) , (2 , 3) , (3 , 4)]
grafo5 = graph.Graph(vertices)
new_graph5 = grafo5.createGraph(vertices , arista)
grafo4.print_graph(new_graph5)
print(grafo5.isTree(new_graph5))

print("-"*5 , "Grafo 6" ,"-"*5)
#Grafo camino con un ciclo
vertices = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8]
arista = [(1, 2) , (2 , 3) , (3 , 4) , (4 , 5) , (5 , 6) , (6 , 7) , (7 , 8) , (1,8)]
grafo6 = graph.Graph(vertices)
new_graph6 = grafo6.createGraph(vertices , arista)
grafo4.print_graph(new_graph6)
print(grafo5.isTree(new_graph6))