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
   raiz_nueva.parent = raiz_vieja.parent

   raiz_vieja.rightnode = None
   raiz_vieja.parent = raiz_nueva

   if aux != None:
        raiz_vieja.rightnode = aux
        aux.parent = raiz_vieja
   return raiz_nueva


def rotateRight(Tree , avlnode):
   raiz_vieja = avlnode
   Tree.root = avlnode.leftnode
   raiz_nueva = Tree.root
   aux = Tree.root.rightnode 

   raiz_nueva.rightnode = raiz_vieja
   raiz_nueva.parent = raiz_vieja.parent

   raiz_vieja.leftnode = None
   raiz_vieja.parent = raiz_nueva

   if aux != None:
        raiz_vieja.leftnode = aux
        aux.parent = raiz_vieja

   return raiz_nueva


#Recibe la raiz de un arbol
def calculateBalance(ALVTree):
     node = ALVTree.root
     if ALVTree == None:
          return
     #Queremos actualizar el node.bf
     height_left = 0
     height_right = 0
     if node.leftnode != None:
          height_left = calculateBalance_balanceRecursive(node.leftnode)
     if node.rightnode != None:
          height_right = calculateBalance_balanceRecursive(node.rightnode)
     bf = height_left - height_right
     node.bf = bf

     return ALVTree


def calculateBalance_balanceRecursive(node):
     
     if node == None:
          return 0
     
     height_left = calculateBalance_balanceRecursive(node.leftnode)
     height_right = calculateBalance_balanceRecursive(node.rightnode)
     #print(f"Altura izquierda {height_left} , Altura derecha {height_right}")

     bf = height_left - height_right
     node.bf = bf

     altura = max(height_left , height_right )

     return 1 + altura 

def reBalance(AVLTree):
     calculateBalance(AVLTree)
     reBalance_recursive(AVLTree , AVLTree.root)
     return AVLTree


def reBalance_recursive(AVLTree , node):
     

     if node.leftnode != None:
          reBalance_recursive(AVLTree, node.leftnode)

     if node.bf < -1:
          if node.rightnode.bf > 0:
               AVLTree.root.rightnode = rotateRight(AVLTree.root.rightnode, node.rightnode)
               rotateLeft(AVLTree,node)
               calculateBalance(AVLTree)
          else:
               rotateLeft(AVLTree,node)
               calculateBalance(AVLTree)

     elif node.bf > 1:
          if node.leftnode.bf < 0:
               AVLTree.root.leftnode = rotateLeft(AVLTree.root.leftnode,node.leftnode)
               rotateRight(AVLTree,node)
               calculateBalance(AVLTree)
          else:
               rotateRight(AVLTree,node)
               calculateBalance(AVLTree)


     if node.rightnode != None:
          reBalance_recursive(AVLTree , node.rightnode)



def insert(AVLTree , key):
     new_node = AVLNode()
     new_node.key = key
     current = AVLTree.root

     if current != None:
          return insertR(current,new_node)
     else:
          AVLTree.root = new_node
     
     return reBalance(AVLTree)
     

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
