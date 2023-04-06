class Trie:
    root = None


class TrieNode:
    parent = None
    children = None
    key = None
    isEndOfWord = False


def insert(T, element):
    aux = 0
    
    if T.root == None:
        node = TrieNode()
        T.root = node
        aux = 1

    current = T.root
    for i in range(len(element)):
        if aux == 1: 
            current.children = []
        children = current.children
        new_node = False

        if children != [] and children != None: #Si la lista no esta vacia busco el elemento
            new_node = search_list(element[i] , children)  #Devuelve true o false
        else:
            current.children = children #Sino, dejo la lista vacia
        
        if new_node == False: #Si no se encontro el elemento en la lista children entonces:
            new_node = TrieNode()
            new_node.parent = current
            new_node.key = element[i]
            if children != None:
                children.append(new_node)
            else:
                children = []
                current.children = children
                children.append(new_node)
        else:                       #Si el elemento ya esta en la lista entonces:
            index = search_pos(element[i] , children)
            new_node = children[index]

        if len(element)-1 == i:
            new_node.isEndOfWord = True

        current = new_node

    return T


def search_list(element , lista):

    for i in range(len(lista)):
        if element == lista[i].key:
            return True
        
    return False

def search_pos(element , lista):

    for i in range(len(lista)):
        if element == lista[i].key:
            return i
        
    return None


def search(T, element):
    node = T.root
    return searchR(node,element)


def searchR(node,element):
    children = node.children 

    aux = search_list(element[0],children)
    pos = search_pos(element[0],children)
    if pos != None:
        aux2 = children[pos]
    
    if aux == False:
        return False
    
    if len(element) == 1 and aux2.isEndOfWord == True:
        return True
    
    element = element[1:]
    return searchR(aux2 , element)

def delete(T , element):

    if search(T,element) == False:
        return False
    
    node = T.root
    deleteR(node, element)


def deleteR(node,element):

    #Sirve para llegar al final de la palabra (desp separar por casos para eleminarlo bien)
    children = node.children
    pos = search_pos(element[0],children)
    aux = children[pos]
    element = element[1:]
    if children != None and element != "":
        return deleteR(aux , element)
    
    if len(children) == 1 and children[0].children == None: #Si la lista final tiene 1 elemento y no tiene hijos
        node.children = None

    
    if len(children) > 1 and children[pos].children == None: #Si la lista final tiene 1 elemento y no tiene hijos
        aux2 = children[0].parent
        aux2.children = None

    #Modificar el codigo para que la primera parte sea una funcion 
