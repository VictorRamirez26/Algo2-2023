class Dictionaty:
    value = None


def func_hash(D , key):
    return key % len(D)

def insert(D , key , value):
    
    new_key = func_hash(D , key)

    if D[new_key] == None:
        new_node = Dictionaty()
        new_node.value = value
        D[new_key] = []
        D[new_key].append(new_node)
    else:
        new_node = Dictionaty()
        new_node.value = value
        if search_list(value , D[new_key]) == False:
            D[new_key].append(new_node)


def search_list(element , lista):

    for i in range(len(lista)):
        if lista[i] != None:
            if element == lista[i].value:
                return True       
        
    return False
