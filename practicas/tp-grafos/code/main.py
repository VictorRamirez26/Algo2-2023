import graph


#Grafo 1
vertices = [1 , 2 , 3 , 4]
arista = [(1 , 2), (2 ,3), (4,2), (1,4)]
grafo = graph.Graph(vertices)
new_graph = grafo.createGraph(vertices , arista)
grafo.print_graph(new_graph)
print(grafo.existPath(new_graph , 3 , 4)) 

#Grafo 2
vertices = [1 , 2 , 3 , 4]
arista = [(1 , 2), (4,2), (1,4)]
grafo2 = graph.Graph(vertices)
new_graph2 = grafo.createGraph(vertices , arista)
grafo.print_graph(new_graph2)
print(grafo.existPath(new_graph2 , 3 , 2)) 