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
    
    def kruskal(self, graph):
        
        #Primero busco todas las conexiones
        visited = set()
        aristas = []
        
        for i in range(1 , len(graph)+1):
            for j in graph[i].list:
                if j.key not in visited:
                    aristas.append((i , j.key , j.value))
            visited.add(i)
        #Ordeno las aristas de menor a mayor segun su peso
        vertices = list(visited)
        aristas = sorted(aristas , key = lambda x: x[2])
        new_aristas = []
        new_dictionary = Graph_Ponderado(vertices , aristas)

        for tuple in aristas :

            new_aristas.append(tuple)
            #Creo un nuevo grafo y me fijo si tiene agregando la tupla genera ciclo
            aux_dict = new_dictionary.createGraph_ponderado(vertices , new_aristas)
            #Si genera ciclo entonces lo saco
            if self.isCiclycal(aux_dict , aristas[0][0] , tuple[1]) == True:
                new_aristas.remove(tuple)
        return new_aristas



    def isCiclycal(self , graph , v1 , v2):

        if (v1 in graph and v2 in graph) is not True:
            return False
        
        if v1 == v2:
            return True

        visited = set()
        queue = [v1]

        # Busco mientras haya elementos en la cola
        while queue:
            
            if queue.count(queue[0]) > 1:
                return True
            
            aux = queue.pop(0)
            # Si el vertice no ha sido visitado, lo agrego al conjunto visited
            if aux not in visited:
                visited.add(aux)
                #Recorro los vertices adyacentes del vertice actual
                for adyacente in graph[aux].list:
                    # Si no ,lo agrego a la cola.
                    if adyacente.key not in visited:
                        queue.append(adyacente.key)
        
        
        

