import dictionary as d
import math 
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

def isSet(lista):
    """
    El costo de iterar la lista para agregar los elementos al diccionario es  O(n), 
    las funciones insert,search,delete son O(1). Por lo tanto la complejidad del algoritmo
    viene dada por la longitud de la lista O(n).
    """
    m = len(lista)
    A = (math.sqrt(5)-1)/2
    hash_function = lambda k : int(m*((k*A) % 1))
    dict = d.Dictionary(hash_function , m)

    for key in lista:
        dict.insert(dict.D , key ,str(key))

    count = 0
    for key in lista:
        aux = dict.search(dict.D , key) 
        if aux != None:
            dict.delete(dict.D , key)
            count += 1

    #Si despues de buscar los elementos, el contador es igual a la longitud de la lista 
    #entonces significa que no hay elementos repetidos
    if count == m: 
        return True
    else:
        return False
    

def codigo_postal(dict , codigo):
    #dict = d.Dictionary(hash_postal, 100003)
    print(f"El codigo postal se va a insertar en la posicion {hash_postal(codigo)}")
    dict.insert(dict.D ,codigo , str(codigo))
    return dict.D

def hash_postal(codigo):
    #La cantidad total de combinaciones del codigo postal que se puede
    #obtener con cddddccc son: 4569760000
    #Entonces vamos a tener que elegir un numero primo muy grande para que se distribuyan
    #correctamente las keys sin que se colisionen tanto

    m = 100003 #Numero primo grande
    num = int(codigo[1:5])
    char_ascii = ord(codigo[0])*10^4+ord(codigo[5])*10^3+ord(codigo[6])*10^2+ord(codigo[7])*10
    value = num + char_ascii
    hash_function = value % m
    return hash_function

def compress(element):
    #No supe como implementar diccionarios de manera optima en este ejercicio. La complejidad de
    #este algoritmo es O(n) porque itero una lista de tamaño n.

    lista = ""
    lista2 = list(element)
    cont = 0

    for i in range(len(element)):
        if i == 0:
            lista += element[i]
            cont += 1
            continue
        if element[i] == lista[-1]:
            cont += 1
        else:
            lista += str(cont) + element[i]
            cont = 1
    lista += str(cont)
    count = lista.count("1")
    if count == len(lista2):
        return element
    else:
        return lista
    
def inText(subtext , text):
    
    aux = len(subtext)
    dict = d.Dictionary(hash_text , 97)
    for i in range(0, len(text)):
        if i+3 <= len(text):
            new_char = text[i:i+3]
            dict.insert(dict.D , new_char , new_char)
    found = dict.search(dict.D , subtext)
    if found != None:
        return True
    else:
        return False

def hash_text(text):

    char_ascii = 0
    for i in range(len(text)):
        char_ascii += ord(text[i])*10^i

    hash_function = char_ascii % 97
    return hash_function


def isSubset(subconjunto , conjunto):
    #La complejidad del algoritmo es O(n) y viene dada por la iteracion 
    #del conjunto al insertar, aunque el costo de insertar es O(1)

    m = 67 #Numero primo
    hash_function = lambda key : key % m
    dict = d.Dictionary(hash_function , m)

    #Agrego los elementos del conjunto a un diccionario
    for key in conjunto: 
        dict.insert(dict.D , key , str(key))

    #Itero el subconjunto y me fijo si sus elementos estan en el diccionario
    #Si algun elemento no esta, entonces no es subconjunto 
    #Recordemos que por ser conjunto no hay elementos repetidos en el diccionario
    for key in subconjunto:
        found = dict.search(dict.D , key)
        if found == None:
            return False
    return True