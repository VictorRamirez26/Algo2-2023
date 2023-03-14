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


def insert_key(AVLTree , key):
     new_node = AVLNode()
     new_node.key = key
     current = AVLTree.root

     if current != None:
         return insertR(current,new_node)
     else:
          AVLTree.root = new_node
          return new_node


def insertR(current,newNode):
  
  
  if newNode.key < current.key:
    if current.leftnode == None:
          current.leftnode = newNode
          newNode.parent = current
          return newNode
    else:
          return insertR(current.leftnode,newNode)
    
  elif newNode.key > current.key:
    if current.rightnode == None:
          current.rightnode = newNode
          newNode.parent = current
          return newNode
    else:
          return insertR(current.rightnode,newNode)
    
  else:
          return None


def insert(AVLTree , key):
     if AVLTree.root == None:
          return insert_key(AVLTree , key)
     new_node = AVLTree.root
     #Primero inserto el elemento
     new_node = insert_key(AVLTree , key)
     
     #Luego voy desde el nodo insertado hacia atras
     print("Ejecuto insert_recursive desde el nodo insertado") 
     insert_recursive(new_node)
     return 



def insert_recursive(node):

     if node == None:
          return 
     
     node = calculateBalance(node)
     print(node.bf)
     if node.bf < -1 or node.bf > 1:
          node = reBalance(node)
          print(f"El nodo rebalanceado es {node.key} , izq: {node.leftnode.key} , der: {node.rightnode.key}")
          return node
     else:
          return insert_recursive(node.parent)

     





