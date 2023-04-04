class Trie:
    root = None


class TrieNode:
    parent = None
    children = None
    key = None
    isEndOfWord = False


def insert(T, element):

    
    if T.root == None:
        node = TrieNode()
        T.root = node

    current = T.root
    for i in range(len(element)):
        current.children = []
        children = current.children
        new_node = None

        if children != None: #Si la lista no esta vacia busco el elemento
            new_node = element[i] in children
        else:
            current.children = children #Sino dejo la lista vacia
        
        if new_node == False: #Si no se encontro el elemento en la lista children
            new_node = TrieNode()
            new_node.parent = current
            new_node.key = element[i]
            children.append(new_node)

        current = new_node

    return T




