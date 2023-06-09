class GraphNode:
    def __init__(self , key = None , aristas = None):
        self.key = key
        self.list = []
        self.connections = aristas
class Graph:
    def __init__(self , vertices = None , aristas = None):
        self.vertices = vertices
        self.aristas = aristas
        
    def createGraph(self , vertices, aristas):
        dict = {}
        for key in range(len(vertices)):
            pos = vertices[key]
            dict[pos] = GraphNode(pos)

        dict = self.connections(dict , aristas)
        dict["connections"] = GraphNode(None , aristas)
        return dict

    def connections(self , dict , aristas):

        for (v1 , v2) in aristas:
            if v1 != v2:
                dict[v1].list.append(v2)
                dict[v2].list.append(v1)
            else:
                dict[v1].list.append(v1)
        return dict
    
    def print_graph(self , graph):
        for key in graph:
            if key != "connections":
                print(f"{key}: {graph[key].list}")

    def existPath(self, graph, v1, v2):

        if (v1 in graph and v2 in graph) is not True:
            return False
        
        if v1 == v2:
            return True

        visited = set()
        queue = [v1]

        # Busco mientras haya elementos en la cola
        while queue:
            aux = queue.pop(0)
            # Si el vertice no ha sido visitado, lo agrego al conjunto visited
            if aux not in visited:
                visited.add(aux)
                #Recorro los vertices adyacentes del vertice actual
                for adyacente in graph[aux].list:
                    #Si encuentro el vertice entonces:
                    if adyacente == v2: 
                        return True
                    # Si no ,lo agrego a la cola.
                    queue.append(adyacente)
        return False

    def isConnected(self , grafo):

        for key in range(1, len(grafo)):
            if grafo[key] != "connections":
                if grafo[key].list == []:
                    return False

        for key in range(2, len(grafo)):
            if self.existPath(grafo , grafo[1].key , grafo[key].key) == False:
                return False
        return True

    def isTree(self , grafo):
        if self.isConnected(grafo) == False:
            return False
        
        for key in range(1, len(grafo)-1):

            if self.isCiclycal(grafo , 1 , key+1) is True:
                return False
        return True
    

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
                    if adyacente not in visited:
                        queue.append(adyacente)

    def isComplete(self , graph):
        
        longitud = len(self.vertices)
        for key in range (1,len(graph)-1):
            if len(graph[key].list) != longitud-1:
                return False
        return True
    
    def convertTree(self , graph):

        visited = set()
        queue = [(graph[1].key, None)]  
        aristas = []  # Aristas del arbol
        
        while queue:
            aux, parent = queue.pop(0)
            # Si el vértice no ha sido visitado, lo agrego al conjunto visited
            if aux not in visited:
                visited.add(aux)

                if parent is not None:
                    aristas.append((parent, aux))
                # Recorro los vértices adyacentes del vértice actual
                for adyacente in graph[aux].list:
                    #Los agrego a la cola con el vértice actual como padre
                    if adyacente not in visited:
                        queue.append((adyacente, aux))
        return aristas
    
    def countConnections(self , graph):

        if self.isConnected(graph) is True:
            return 1   
        
        visited = set()
        count = 0
        for key in range(1, len(graph)):

            if graph[key].key not in visited:
                if graph[key].list == []:
                    count += 1
                    visited.add(graph[key].key)
                else:
                    count += 1
                    visited.add(key)
                    for i in graph[key].list:
                        visited.add(i)
        return count
    
    def convertToBFSTree(self , graph , v):
        visited = set()
        queue = [(v, None)]  
        aristas = []  # Aristas del arbol
        
        while queue:
            aux, parent = queue.pop(0)
            # Si el vértice no ha sido visitado, lo agrego al conjunto visited
            if aux not in visited:
                visited.add(aux)

                if parent is not None:
                    aristas.append((parent, aux))
                # Recorro los vértices adyacentes del vértice actual
                for adyacente in graph[aux].list:
                    #Los agrego a la cola con el vértice actual como padre
                    queue.append((adyacente, aux))
        
        return self.createGraph(self.vertices , aristas)
    
    def convertToDSFTree(self , graph , v):

        visited = set()
        aristas = []
        self.DSF_recursive(graph , v , visited , aristas)
        return self.createGraph(self.vertices , aristas)

    def DSF_recursive(self , graph , v , visited , aristas):
        
        visited.add(v) #Agrego el primer vertice  de todos al conjunto
        for adyacente in graph[v].list:

            if adyacente not in visited:
                aristas.append((v , adyacente)) #Agrego su adyacente
                self.DSF_recursive(graph , adyacente , visited , aristas) #Recorro desde el primer adyacente

    def bestRoad(self , graph ,  v1 , v2):

        bfs_tree = self.convertToBFSTree(graph, v1)
        visited = set()
        queue = [(v1, None)]

        while queue:
            node, prev = queue.pop(0)

            if node == v2:
                #Construyo la ruta desde v1 a v2
                path = []
                while prev is not None:
                    path.append((prev, node))
                    node, prev = prev, bfs_tree[prev].parent
                path.reverse()
                return path

            if node not in visited:
                visited.add(node)
                #El nodo anterior es el padre del nodo actual
                bfs_tree[node].parent = prev 
                #Recorro los nodos adyacentes
                for adyacente in bfs_tree[node].list:
                    #Si el adyacente no ha sido visitado lo agrego a la cola
                    if adyacente not in visited:
                        queue.append((adyacente, node))

        return None
