import dictionary as d

def is_permutation(element1 , element2):

    """
    La complejidad temporal de insert y search en un hash_table es O(1) , sin embargo
    la complejidad del algoritmo viene dada por la longitud de los elementos ya que
    se itera en un bucle .Por lo tanto la complejidad es O(n)
    """
    is_permutation = True
    if len(element1) != len(element2):
        return False
    
    m = 25  #Longitud del universo (los caracteres de a-z)
    hash_function = lambda x: ord(x) % m   #ord(x) es el codigo ASCII del caracter que ponga 
    dict = d.Dictionary(hash_function , m)

    #Agregamos al diccionario todos los caracteres de el primer elemento
    for i in element1:
        dict.insert(dict.D , i , str(i))

    for j in element2:
        pos = dict.search(dict.D , j)
        if pos == None:
            is_permutation = False
    
    return is_permutation

def is_permutation_opcion2(element1 , element2):

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