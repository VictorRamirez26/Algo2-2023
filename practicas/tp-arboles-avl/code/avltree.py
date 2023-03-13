class AVLTree:
	root = None

class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    bf = None
	

def rotateLeft(Tree , avlnode):
   raiz_vieja = avlnode
   Tree.root = avlnode.rightnode
   raiz_nueva = Tree.root    
   aux = raiz_nueva.leftnode 
   raiz_nueva.leftnode = raiz_vieja

   if aux != None:
        raiz_vieja.rightnode = aux
   return raiz_nueva


def rotateRight(Tree , avlnode):
   raiz_vieja = avlnode
   Tree.root = avlnode.leftnode
   raiz_nueva = Tree.root
   aux = Tree.root.rightnode 
   raiz_nueva.rightnode = raiz_vieja

   if aux != None:
        raiz_vieja.leftnode = aux

   return raiz_nueva


def calculateBalance(ALVTree):
     node = ALVTree
     #Queremos actualizar el node.bf
     height_left = balanceRecursive(node.leftnode)
     height_right = balanceRecursive(node.rightnode)
     bf = height_left - height_right
     node.bf = bf

     return node
     

def balanceRecursive(node):
     
     if node == None:
          return 0
     
     height_left = balanceRecursive(node.leftnode)
     height_right = balanceRecursive(node.rightnode)
     #print(f"Altura izquierda {height_left} , Altura derecha {height_right}")

     bf = height_left - height_right
     node.bf = bf

     altura = max(height_left , height_right )

     return 1 + altura 


def reBalance(AVLTree): 
     #Primero calculo el Balance Factor de cada nodo
     new_arbol = calculateBalance(AVLTree)
     node = new_arbol
     reBalance_recursive(node)
     #print(node.value)
     #print(node.leftnode.value)
     #print(node.rightnode.value)
     return node


def reBalance_recursive(node):

     if node == None or node.bf == 0 :
          return 
     
     if node.bf > 0 : 
          if node.leftnode.bf < 0:
               node.leftnode = rotateLeft(node , node.leftnode)
               node = rotateRight(node , node)
          else:
               node = rotateRight(node , node)
     
     elif node.bf < 0 :
          if node.rightnode.bf > 0:
               node.rightnode = rotateRight(node , node.rightnode )
               print(f"Primera rotacion / hijo derecho : {node.rightnode.value}")
               node = rotateLeft(node , node)
               print(f"Segunda rotacion / Raiz : {node.value} , hijo izquierdo : {node.leftnode.value} , hijo derecho : {node.rightnode.value}")

          else:
               node = rotateLeft(node , node)


     #Falta calcular el nuevo balance factor de cada nodo pq sino no termina la recursividad nunca
     reBalance_recursive(node.leftnode)
     reBalance_recursive(node.rightnode)

     return node
