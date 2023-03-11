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

    
    
