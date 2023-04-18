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
lista2 = [1 , 5 , 12 , 2]
print(p2.isSet(lista))
print(p2.isSet(lista2))
print("--------FIN--------")
