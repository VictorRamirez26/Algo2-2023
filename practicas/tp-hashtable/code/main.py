import dictionary as d
import parte2 as p2

dictionary = d.Dictionary(None , 8)
#--------Insert--------
#Si el diccionario esta vacio:
dictionary.insert(dictionary.D , 0 , "H0")
dictionary.insert(dictionary.D , 1 , "H1")
dictionary.insert(dictionary.D , 2 , "H2")
dictionary.insert(dictionary.D , 3 , "H3")
dictionary.insert(dictionary.D , 4 , "H4")
dictionary.insert(dictionary.D , 5 , "H5")
dictionary.insert(dictionary.D , 6 , "H6")
dictionary.insert(dictionary.D , 7 , "H7")
#Si no esta vacio:
dictionary.insert(dictionary.D , 10 , "H10")
dictionary.insert(dictionary.D , 9 , "H9")
#Si en la key ya hay un valor que ya estaba entonces:
dictionary.insert(dictionary.D , 8 , "H0")


print("--------Search--------")
#--------Search--------
print(dictionary.search(dictionary.D , 0))
print(dictionary.search(dictionary.D , 3))
print(dictionary.search(dictionary.D , 5))
print(dictionary.search(dictionary.D , 10))
print(dictionary.search(dictionary.D , 100))

print("--------Delete--------")
#--------Delete--------
dictionary.delete(dictionary.D , 0)
dictionary.delete(dictionary.D , 100)
dictionary.delete(dictionary.D , 3) #Solo hay un elemento y lo elemino

#Ahora quiero agregar algo en ese lugar
dictionary.insert(dictionary.D , 3 , "H3")
dictionary.insert(dictionary.D , 0 , "H1")

#--------PARTE 2--------
print("--------Ejercicio 4--------")
print(p2.is_permutation("hola" , "olha"))
print(p2.is_permutation("hola" , "holas"))
print(p2.is_permutation("chau" , "hola"))
#print(p2.is_permutation_opcion2("HOLA" , "ALHO"))
#print(p2.is_permutation_opcion2("HOLA" , "ALHODA"))

print("--------Ejercicio 5--------")
lista = [1 , 5 , 12 , 1 , 2]
lista2 = [2, 2, 2, 2]
lista3 = [1 , 5 , 12 , 2]
print(p2.isSet(lista))
print(p2.isSet(lista2))
print(p2.isSet(lista3))

print("--------Ejercicio 6--------")
dict = d.Dictionary(p2.hash_postal, 100003)
p2.codigo_postal(dict , "A9341ZJK")
p2.codigo_postal(dict ,"A9371ZJZ")
p2.codigo_postal(dict ,"Z9281KLZ")
p2.codigo_postal(dict ,"K9913LPQ")
p2.codigo_postal(dict ,"L0012ZLP")
p2.codigo_postal(dict ,"U0912KKK")

print("--------Ejercicio 7--------")
print(p2.compress("aabcccccaaa"))
print(p2.compress("abc"))

print("--------Ejercicio 8--------")
#Casos donde deberia devolver True
print(p2.inText("abc","aabttkabbabc"))
print(p2.inText("abb","aabttkabbabc"))
print(p2.inText("ttk","aabttkabbabc"))
#Casos donde deberia devolver False
print(p2.inText("zks","aabttkabbabc"))
print(p2.inText("cba","aabttkabbabc"))

print("--------Ejercicio 9--------")

conjunto = [1,2,3,4,5]
subConjunto = [1,2,3]
subConjunto2 = [3,2,1]
subConjunto3 = [1,2,67]
subConjunto4 = [1,2,3,8]
print(p2.isSubset( subConjunto , conjunto))
print(p2.isSubset( subConjunto2 , conjunto))
print(p2.isSubset( subConjunto3 , conjunto))
print(p2.isSubset( subConjunto4 , conjunto))

print("--------Ejercicio 1--------")
numbers = [5, 28, 19, 15, 20, 33, 12, 17, 10]
dict = d.Dictionary(None , len(numbers)) #Longitud 9, va a aplicar key % 9 en la hash_function
for key in numbers:
    dict.insert(dict.D , key , str(key))

print("--------Ejercicio 3--------")
numbers = [61,62,63,64,65]
dict = p2.ejercicio3(numbers)
print("--------FIN--------")
