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
print("Es un grafo completo?: " , grafo.isComplete(new_graph))
print(grafo.convertTree(new_graph))
print("Componentes conexas: " , grafo.countConnections(new_graph))
bfs = grafo.convertToBFSTree(new_graph , 2)
grafo.print_graph(bfs)

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
print("Es un grafo completo?: " , grafo2.isComplete(new_graph2))
print(grafo2.convertTree(new_graph2))
print("Componentes conexas: " , grafo2.countConnections(new_graph2))
bfs = grafo2.convertToBFSTree(new_graph2 , 1)
grafo2.print_graph(bfs)

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
print("Es un grafo completo?: " , grafo3.isComplete(new_graph3))
print(grafo3.convertTree(new_graph3))
print("Componentes conexas: " , grafo3.countConnections(new_graph3))
bfs = grafo3.convertToBFSTree(new_graph3 , 1)
grafo3.print_graph(bfs)

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
print("Es un grafo completo?: " , grafo4.isComplete(new_graph4))
print(grafo4.convertTree(new_graph4))
print("Componentes conexas: " , grafo4.countConnections(new_graph4))
bfs = grafo4.convertToBFSTree(new_graph4 , 1)
grafo4.print_graph(bfs)

print("-"*5 , "Grafo 5" ,"-"*5)
#Grafo conexo y aciclico (arbol)
vertices = [1 , 2 , 3 , 4]
arista = [(1 , 2) , (2 , 3) , (3 , 4)]
grafo5 = graph.Graph(vertices)
new_graph5 = grafo5.createGraph(vertices , arista)
grafo4.print_graph(new_graph5)
print(grafo5.isTree(new_graph5))
print("Es un grafo completo?: " , grafo5.isComplete(new_graph5))
print(grafo5.convertTree(new_graph5))
print("Componentes conexas: " , grafo5.countConnections(new_graph5))
bfs = grafo5.convertToBFSTree(new_graph5 , 1)
grafo5.print_graph(bfs)


print("-"*5 , "Grafo 6" ,"-"*5)
#Grafo camino con un ciclo
vertices = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8]
arista = [(1, 2) , (2 , 3) , (3 , 4) , (4 , 5) , (5 , 6) , (6 , 7) , (7 , 8) , (1,8)]
grafo6 = graph.Graph(vertices)
new_graph6 = grafo6.createGraph(vertices , arista)
grafo6.print_graph(new_graph6)
print(grafo6.isTree(new_graph6))
print("Es un grafo completo?: " , grafo6.isComplete(new_graph6))
print(grafo6.convertTree(new_graph6))
print("Componentes conexas: " , grafo6.countConnections(new_graph6))
bfs = grafo6.convertToBFSTree(new_graph6 , 1)
grafo6.print_graph(bfs)


print("-"*5 , "Grafo 7" ,"-"*5)
#Grafo completo
vertices = [1 , 2 , 3 , 4 , 5]
arista = [(1 , 2) , (1 , 3) , (1 , 4) , (1 , 5)]
grafo7 = graph.Graph(vertices)
new_graph7 = grafo7.createGraph(vertices , arista)
grafo7.print_graph(new_graph7)
print("Es un arbol: " ,grafo7.isTree(new_graph7))
print("Es un grafo completo?: " , grafo7.isComplete(new_graph7))
print(grafo7.convertTree(new_graph7))
print("Componentes conexas: " , grafo7.countConnections(new_graph7))
bfs = grafo7.convertToBFSTree(new_graph7 , 1)
grafo7.print_graph(bfs)
