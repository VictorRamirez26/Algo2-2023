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
print("-------------- SEARCH --------------")

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
print("-------------- DELETE --------------")
print(t.delete(T, "PILA")) #Elento q no existe 
print(t.delete(T ,"HOLA")) #Caso 0: Borro una palabra que este dentro de otra mas grande (Hola , Holanda)
print(t.delete(T ,"CAOS")) #CASO 1 Y 2 borro el ultimo elemento si no tiene hijos o borro el ultimo elemento si tiene hijos
t.insert(T,"CAOS")
t.insert(T,"CAOTA")
print(t.delete(T ,"CAOS")) #CASO 3 Borro un elemento que se encuentre entre medio de 2 palabras (CASA, CAOS ,CAOTA)
t.buscar_patron(T , "HO" , 4)