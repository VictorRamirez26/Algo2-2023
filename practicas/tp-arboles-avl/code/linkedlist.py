from algo1 import*
class LinkedList:
  head=None
class Node:
  value=None
  nextNode=None


def print_list(L):
	node = L.head
	pos = 0

	while node != None:
		if pos != 0: print(end=" | ")
		print(node.value, end="")
		node = node.nextNode
		pos += 1
	print()
	return pos
  
def add(L,element):
  node = L.head
  newNode = Node()
  newNode.value = element

  if node == None:
    L.head = newNode
  else:
    newNode.nextNode = node
    L.head = newNode
    
def search(L,element):
  node = L.head
  pos = 0
  while node != None:
    if node.value == element:
      return pos
    node = node.nextNode
    pos += 1
    
  return 

def insert(L,element,position):
  node = L.head
  pos = 0
  
  if position == 0:
    add(L,element)
    return pos
    
  elif position > 0:
    newNode = Node()
    newNode.value = element
    if node == None:
      return 
    while node.nextNode != None:
      if pos+1 != position:
        node = node.nextNode 
        pos += 1
      else:
        newNode.nextNode = node.nextNode
        node.nextNode = newNode
        return position
    node.nextNode = newNode
    return pos+1
  return 

def delete(L,element):
  node = L.head
  pos = 0

  if node == None:
    return
  elif node.value == element:
    L.head = node.nextNode
    return pos

  while node.nextNode != None:
    if node.nextNode.value == element:
      node.nextNode =   node.nextNode.nextNode 
      return pos+1
    else:
      node = node.nextNode
      pos += 1
  return 

def length(L):
  node = L.head
  pos = 0
  if node == None:
    return pos
  
  while node.nextNode != None:
    node = node.nextNode
    pos += 1
  return pos+1

def access(L,position):
  node = L.head
  pos = 0
  if node == None:
    return
  while node.nextNode != None:
    if pos == position:
      return node.value
    node = node.nextNode
    pos += 1

  if pos == position:
    return node.value
    
  return 

def update(L,element,position):
  node = L.head
  pos = 0

  while node.nextNode != None:
    if pos == position:
      node.value = element
      return pos
    node = node.nextNode
    pos += 1
    
  if pos == position:
      node.value = element
      return pos

def move(l, position_origin, position_dest):
    val_origin = access(l, position_origin)
    val_dest = access(l, position_dest)
    update(l, val_dest, position_origin)
    update(l, val_origin, position_dest)

def invertir_lista(L):
  node = L.head
  newList = LinkedList()
  j=0
  for i in range(length(L)-1,-1,-1):
    valor = access(L,i)
    insert(newList,valor,j)
    j += 1  
  return newList