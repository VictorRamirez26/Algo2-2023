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


#Recibe la raiz de un arbol
def calculateBalance(ALVTree):
     if ALVTree == None:
          return
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
     if AVLTree == None:
          return 
     
     #Balanceo el lado izquierdo y derecho recursivamente 
     AVLTree.leftnode = reBalance(AVLTree.leftnode)
     AVLTree.rightnode = reBalance(AVLTree.rightnode)

     #Calculo el balance factor de la raiz y sus hijos 
     AVLTree = calculateBalance(AVLTree)
     balance_f_der = calculateBalance(AVLTree.rightnode)
     balance_f_iz = calculateBalance(AVLTree.leftnode)


     #Si el arbol esta desbalanceado por derecha:
     if AVLTree.bf < -1:

          if balance_f_der.bf > 0:
               AVLTree.rightnode =  rotateRight(AVLTree , AVLTree.rightnode)

          return rotateLeft(AVLTree , AVLTree)

     #Si el arbol esta desbalanceado por izquierda:
     if AVLTree.bf > 1:

          if balance_f_iz.bf < 0:
               AVLTree.leftnode =  rotateLeft(AVLTree , AVLTree.leftnode)

          return rotateRight(AVLTree , AVLTree)

     #Devuelvo el arbol
     return AVLTree