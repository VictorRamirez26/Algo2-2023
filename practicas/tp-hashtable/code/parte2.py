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