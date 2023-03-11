from algo1 import * 
from linkedlist import LinkedList,add,print_list,invertir_lista
from myqueue import enqueue,dequeue

class BinaryTree:
  root = None

class BinaryTreeNode:
  key = None
  value = None
  leftnode = None
  rightnode = None
  parent = None


#En el peor de los casos es O(n) pero en los otros casos es O(log n)
def search(B,element):
  current = searchR(B.root,element)
  if current == None:
    return None
  else:
    return current.key

def searchR(current,element):

  if current == None:
    return None
  if current.value == element:
    return current

  leftNode = searchR(current.leftnode,element)
  if leftNode != None:
    return leftNode

  rightNode = searchR(current.rightnode,element)
  if rightNode != None:
    return rightNode

def searchR_key(current,key):

  if current == None:
    return None
  if current.key == key:
    return current

  leftNode = searchR_key(current.leftnode,key)
  if leftNode != None:
    return leftNode

  rightNode = searchR_key(current.rightnode,key)
  if rightNode != None:
    return rightNode


def insert(B, element, key):
  newNode = BinaryTreeNode()
  newNode.value = element
  newNode.key = key
  current = B.root

  if current != None:
    return insertR(current,newNode)
  else:
    B.root = newNode
    return newNode.key
  
def insertR(current,newNode):
  
  
  if newNode.key < current.key:
    if current.leftnode == None:
      current.leftnode = newNode
      newNode.parent = current
      return newNode.key
    else:
      return insertR(current.leftnode,newNode)
  elif newNode.key > current.key:
    if current.rightnode == None:
      current.rightnode = newNode
      newNode.parent = current
      return newNode.key
    else:
      return insertR(current.rightnode,newNode)
  else:
    return None

def delete(B,element):
  node = searchR(B.root,element)

  if node == None:
    return None
  else:
    return deleteR(B,node)

def deleteR(B,node):

  #Caso 1: elimino una hoja
  if node.leftnode == None and node.rightnode == None:
    if node.parent.leftnode == node:
      node.parent.leftnode = None
      return node.key
    elif node.parent.rightnode == node:
      node.parent.rightnode = None
      return node.key

  #Caso 2: elimino un nodo con un hijo del lado izquierdo
  if node.leftnode != None and node.rightnode == None:
    if node.parent.leftnode != None and node.parent.leftnode == node:
      node.parent.leftnode = node.leftnode
      return node.key
    elif node.parent.rightnode != None and node.parent.rightnode == node:
      node.parent.rightnode = node.leftnode
      return node.key
  
  #Caso 3: elimino un nodo con un hijo del lado derecho
  if node.rightnode != None and node.leftnode == None:
    if node.parent.rightnode != None and node.parent.rightnode == node:
      node.parent.rightnode = node.rightnode
      return node.key
    elif node.parent.leftnode != None and node.parent.leftnode == node:
      node.parent.leftnode = node.rightnode
      return node.key

  #Caso 4: Elimino un nodo que tiene 2 hijos
  mayor = mayor_menores(node.leftnode)
  aux = node.key
  node.value = mayor.value
  node.key = mayor.key
  
  mayor.parent.rightnode = mayor.leftnode
  return aux
    

def mayor_menores(node):

  if node.rightnode != None:
    currentNode = mayor_menores(node.rightnode)
    if currentNode != None:
      return currentNode
  else:
    return node

def deleteKey(B,key):
  node = searchR_key(B.root,key)

  if node == None:
    return None
  else:
    return deleteR(B,node)


def access(B,key):
  node = searchR_key(B.root,key)

  if node == None:
    return
  else:
    return node.value

def update(B,element,key):
  node = searchR_key(B.root,key)

  if node == None:
    return None
  else:
    node.value = element
    return node.key

#IN - ORDER
def traverseInOrder(B):
	L=LinkedList()
	traverseInOrderR(B.root, L)
	return invertir_lista(L)

# Función recursiva de traverseInOrder
def traverseInOrderR(node, L):
  if node != None:
    traverseInOrderR(node.leftnode,L)
    add(L,node.value)
    traverseInOrderR(node.rightnode,L)

#POST - ORDER
def traverseInPostOrder(B):
  L = LinkedList()
  traverseInPostOrderR(B.root,L)
  return invertir_lista(L)

#Funcion recursiva de traverseInPostOrder
def traverseInPostOrderR(node,L):
  if node != None:
    traverseInPostOrderR(node.leftnode,L)
    traverseInPostOrderR(node.rightnode,L)
    add(L,node.value)

    
#PRE - ORDER
def traverseInPreOrder(B):
  L = LinkedList()
  traverseInPreOrderR(B.root,L)
  return invertir_lista(L)


#Funcion recursiva de  traverseInPreOrder
def traverseInPreOrderR(node,L):
  if node != None:
    add(L,node.value)
    traverseInPreOrderR(node.leftnode,L)
    traverseInPreOrderR(node.rightnode,L)



def traverseBreadFirst(B):

  L = LinkedList()
  Q = LinkedList()
  enqueue(L, B.root)
  while L.head != None:
    node = dequeue(L)
    enqueue(Q, node.value)
    if node.leftnode != None:
      enqueue(L, node.leftnode)
    if node.rightnode != None:
      enqueue(L, node.rightnode)
  return invertir_lista(Q)