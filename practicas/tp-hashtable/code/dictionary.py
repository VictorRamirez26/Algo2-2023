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
        
def delete(D , key):

    new_key = func_hash(D , key)

    if D[new_key] == None:
        return D
    else:
        lista = D[new_key]
        pos = search_key(key , lista)
        if pos == None:
            return D
        else:
            lista.pop(pos)
            return D
        
def is_permutation(element1 , element2):

    #En este caso iteramos los elementos y nos quedamos con su valor ASCII,
    #luego hacemos la suma de sus valores ASCII. Por lo tanto nos queda O(n)
    sum1 = sum(ord(i) for i in element1)
    sum2 = sum(ord(i) for i in element2)

    if sum1 == sum2:
        return True
    else:
        return False

def isSet(element):
    return len(element) == len(set(element))
    #Hacer denuevo esta funcion ya que el set implementa hash table



