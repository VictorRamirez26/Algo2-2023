import heapq
class GraphNode_ponderado:
    def __init__(self , key = None , aristas = None , value = None):
        self.key = key
        self.list = []    #Esta lista sirve para poner sus nodos adyacentes
        self.connections = aristas
        self.value = value

class Node:
    def __init__(self , key = None, value = None):
        self.key = key
        self.value = value

class Graph_Ponderado:
    def __init__(self , vertices = None , aristas = None):
        self.vertices = vertices
        self.aristas = aristas
        
    def createGraph_ponderado(self , vertices, aristas):
        dict = {}
        for key in range(len(vertices)):
            pos = vertices[key]
            dict[pos] = GraphNode_ponderado(pos)

        dict = self.connections(dict , aristas)
        return dict

    def connections(self , dict , aristas):

        for (v1 , v2 , c) in aristas:
            if v1 != v2:
                node = Node(v2, c)
                dict[v1].list.append(node)
                node2 = Node(v1 , c)
                dict[v2].list.append(node2)
            else: 
                node = Node(v1, c)
                dict[v1].list.append(node)
        return dict
    
    def prim(self , graph):

        visited = set()
        queue = [(0, graph[1].key)]
        new_arbol = []

        while queue:
            (peso, aux) = heapq.heappop(queue) #Saco la tupla con menor peso
            if aux not in visited:
                visited.add(aux)
                if peso > 0 :
                    for i in graph[aux].list: #Busco la arista de menor peso
                        if i.value == peso:
                            new_arbol.append((i.key, aux , peso))    
                for adyacente in graph[aux].list:
                    if adyacente.key not in visited:
                        heapq.heappush(queue, (adyacente.value, adyacente.key)) #Agrego los adyacentes con sus pesos
        return new_arbol