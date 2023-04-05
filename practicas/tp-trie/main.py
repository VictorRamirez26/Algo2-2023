import trie as t

T = t.Trie()
#Inserto 3 palabras normales
t.insert(T, "HOLA")
t.insert(T, "CHAU")
t.insert(T, "ADIOS")
#Inserto una palabra que tiene la misma rama que "HOLA"
t.insert(T, "HOLANDA")
#Inserto una palabra que provoca una bifurcacion
t.insert(T,"CAOS")

