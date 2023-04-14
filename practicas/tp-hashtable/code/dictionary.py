class Dictionaty:
    value = None
    key = None

def func_hash(D , key):
    return key % len(D)

def insert(D , key , value):
    
    new_key = func_hash(D , key)

    if D[new_key] == None:
        new_node = Dictionaty()
        new_node.value = value
        new_node.key = key
        D[new_key] = []
        D[new_key].append(new_node)
    else:
        new_node = Dictionaty()
        new_node.value = value
        new_node.key = key
        if search_list(value , D[new_key]) == False:
            D[new_key].append(new_node)

    return D


def search_list(element , lista):

    for i in range(len(lista)):
        if lista[i] != None:
            if element == lista[i].value:
                return True       
    return False

def search_key(key , lista):

    for i in range(len(lista)):
        if lista[i] != None:
            if key == lista[i].key:
                return i       
    return None

def search(D , key):
    
    new_key = func_hash(D , key)
    if D[new_key] == None:
        return None
    else:
        list = D[new_key]
        pos = search_key(key , list)
        if pos == None:
            return None
        else:
            return list[pos].value