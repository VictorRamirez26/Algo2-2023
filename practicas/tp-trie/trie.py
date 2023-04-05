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
            new_node = element[i] in children #Corregir esta parte para q devuelva la pos de un elemento
        else:
            current.children = children #Sino, dejo la lista vacia
        
        if new_node == False: #Si no se encontro el elemento en la lista children
            new_node = TrieNode()
            new_node.parent = current
            new_node.key = element[i]
            if children != None:
                children.append(new_node)
            else:
                children = []
                current.children = children
                children.append(new_node)

        current = new_node

    return T




