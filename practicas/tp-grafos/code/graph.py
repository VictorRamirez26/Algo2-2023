class GraphNode:
    def __init__(self , key = None):
        self.key = key
        self.list = []


class Graph:
    def __init__(self , vertices = None):
        self.vertices = len(vertices)

    def createGraph(self , vertices, aristas):
        dict = {}
        for key in range(len(vertices)):
            pos = vertices[key]
            dict[pos] = GraphNode(pos)

        dict = self.connections(dict , aristas)
        return dict

    def connections(self , dict , aristas):

        for (v1 , v2) in aristas:
            dict[v1].list.append(v2)
            dict[v2].list.append(v1)
        return dict
    
    def print_graph(self , graph):
        for key in graph:
            print(f"{key}: {graph[key].list}")

    def existPath(self , graph , v1 , v2):

        #Me fijo si los vertices existen en el grafo
        if (v1 in graph and v2 in graph) == False:
            return False
        
        #Itero sobre la lista de adyacencia de V1
        for i in graph[v1].list:
            #Si V2 existe en la lista de adyacencia de v1 entonces:
            if v2 in graph[v1].list:
                return True
            else:    
                #Sino , el nuevo v1 va a ser un vertice de su lista de adyacencia
                return self.existPath(graph , i , v2)
            
        return False