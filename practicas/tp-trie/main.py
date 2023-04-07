import trie as t

T = t.Trie()
#-------------- INSERT --------------
#Inserto 3 palabras normales
t.insert(T, "HOLA")
t.insert(T, "CASA")
t.insert(T, "ADIOS")
#Inserto una palabra que tiene la misma rama que "HOLA"
t.insert(T, "HOLANDA")
t.insert(T, "HOLAN")
#Inserto una palabra que provoca una bifurcacion
t.insert(T,"CAOS")

#-------------- SEARCH --------------
#Pruebo si las palabras se encuentran en el arbol
print(t.search(T,"HOLANDA"))
print(t.search(T,"HOLA"))
print(t.search(T,"HOLAN"))
print(t.search(T,"CASA"))
print(t.search(T,"ADIOS"))
print(t.search(T,"CAOS"))

#Pruebo si las palabras no se encuentran en el arbol
print(t.search(T,"NINGUNO"))
print(t.search(T,"CASAMIENTO"))

#-------------- DELETE --------------
t.delete(T , "HOLA")
print("X")