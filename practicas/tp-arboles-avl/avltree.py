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
   aux = avlnode
   Tree.root = avlnode.rightnode
   aux2 = Tree.root.leftnode 
   Tree.root.leftnode = aux

   if Tree.root.leftnode != None:
        aux.rightnode = aux2

   return Tree.root


def rotateRight(Tree , avlnode):
   aux = avlnode
   print("aux: " ,aux)
   Tree.root = avlnode.leftnode
   aux2 = Tree.root.rightnode 
   print("aux2: " ,aux2)
   Tree.root.rightnode = aux

   if Tree.root.rightnode != None:
        aux.leftnode = aux2

   return Tree.root

    
    
