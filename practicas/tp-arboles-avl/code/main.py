from algo1 import *
import binarytree
import avltree as avl

#Rotaciones
"""

B = binarytree.BinaryTree()
binarytree.insert(B , "E" , 10)
binarytree.insert(B , "C" , 5)
binarytree.insert(B , "D" , 6) 
binarytree.insert(B , "B" , 4) 
binarytree.insert(B , "A" , 3) 
binarytree.insert(B , "F" , 11) 


print(B.root.value)
print(B.root.rightnode.value)
print(B.root.leftnode.value)
print(B.root.leftnode.rightnode.value)
print(B.root.leftnode.leftnode.value)
print(B.root.leftnode.leftnode.leftnode.value)
print("--"*5)

B = avl.rotateRight(B , B.root )
print(B.value)
print(B.leftnode.value)
print(B.leftnode.leftnode.value)
print(B.rightnode.value)
print(B.rightnode.leftnode.value)
print(B.rightnode.rightnode.value)



B = binarytree.BinaryTree()
binarytree.insert(B , "A" , 10)
binarytree.insert(B , "B" , 12)
binarytree.insert(B , "D" , 11) 
binarytree.insert(B , "C" , 15) 


print(B.root.value)
print(B.root.rightnode.value)
print(B.root.rightnode.leftnode.value)
print(B.root.rightnode.rightnode.value)
print("--"*5)

B = avl.rotateLeft(B , B.root )
print(B.value)
print(B.leftnode.value)
print(B.rightnode.value)
print(B.leftnode.rightnode.value)

"""


#Test de Balance Factor
"""
#Llenamos un arbol avl
B = avl.AVLTree()
#Nodo A
nodeA = avl.AVLNode()
nodeA.value = "A"
nodeA.key = 10
#Nodo B
nodeB = avl.AVLNode()
nodeB.value = "B"
nodeB.key = 5
#Nodo C
nodeC = avl.AVLNode()
nodeC.value = "C"
nodeC.key = 15

#Nodo D
nodeD = avl.AVLNode()
nodeD.value = "D"
nodeD.key = 3

#Hacemos que el B.root sea el nodoA y asignamos los hijos de A
nodeA.leftnode = nodeB
nodeA.rightnode = nodeC
nodeA.leftnode.leftnode = nodeD
B.root = nodeA


new_arbol = avl.calculateBalance(B.root)

print(new_arbol.bf)
print(new_arbol.leftnode.bf)
print(new_arbol.rightnode.bf)
print(new_arbol.leftnode.leftnode.bf)
"""
#Caso 1 (Desbalanceado por derecha)
"""

#Llenamos un arbol avl
B = avl.AVLTree()
#Nodo A
nodeA = avl.AVLNode()
nodeA.value = "A"
nodeA.key = 10
#Nodo B
nodeB = avl.AVLNode()
nodeB.value = "C"
nodeB.key = 15
#Nodo C
nodeC = avl.AVLNode()
nodeC.value = "B"
nodeC.key = 13


#Hacemos que el B.root sea el nodoA y asignamos los hijos de A
nodeA.rightnode = nodeB
nodeA.rightnode.leftnode = nodeC
B.root = nodeA

print("CASO 1:")
balanced_tree = avl.reBalance(B.root)
print(balanced_tree.value)
print(balanced_tree.leftnode.value)
print(balanced_tree.rightnode.value)
print("__"*10)
"""

#Caso 2 (Desbalanceado por izquierda)

B = avl.AVLTree()
nodeA = avl.AVLNode()
nodeA.value = "A"
nodeA.key = 10
#Nodo B
nodeB = avl.AVLNode()
nodeB.value = "B"
nodeB.key = 5
#Nodo C
nodeC = avl.AVLNode()
nodeC.value = "C"
nodeC.key = 7

#Hacemos que el B.root sea el nodoA y asignamos los hijos de A
print("CASO 2:")
nodeA.leftnode = nodeB
nodeA.leftnode.rightnode = nodeC
B.root = nodeA
balanced_tree = avl.reBalance(B.root)
print(balanced_tree.value)
print(balanced_tree.leftnode.value)
print(balanced_tree.rightnode.value)
