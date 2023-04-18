class DictionaryNode:
    def __init__(self, key= None, value = None):
        self.key = key
        self.value = value

class Dictionary:

    def __init__(self , hash_function = None , longitud = 10):
        self.D = [None] * longitud

        if hash_function != None:
            self.hash_function = hash_function
        else:
            self.hash_function = lambda x: x % longitud

    def insert(self , D , key , value):

        new_key = self.hash_function(key)

        if D[new_key] == None:
            new_node = DictionaryNode(key , value)
            D[new_key] = []
            D[new_key].append(new_node)
        else:
            new_node = DictionaryNode(key , value)
            if search_list(value , D[new_key]) == False:
                D[new_key].append(new_node)
        return D

    def search(self , D , key):

        new_key = self.hash_function(key)
        if D[new_key] == None:
            return None
        else:
            list = D[new_key]
            pos = search_key(key , list)
            if pos == None:
                return None
            else:
                return list[pos].value

    def delete(self , D , key):

        new_key = self.hash_function(key)

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