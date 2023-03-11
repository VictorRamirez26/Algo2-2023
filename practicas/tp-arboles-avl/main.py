from algo1 import *
import binarytree
import avltree as avl



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


"""
B = binarytree.BinaryTree()
binarytree.insert(B , "A" , 10)
binarytree.insert(B , "B" , 12)
binarytree.insert(B , "D" , 11) 
binarytree.insert(B , "C" , 15) 


print(B.root.value)
print(B.root.rightnode.value)
print(B.root.rightnode.rightnode.value)
print("--"*5)

B = avl.rotateLeft(B , B.root )
print(B.value)
print(B.leftnode.value)
print(B.rightnode.value)
print(B.leftnode.rightnode.value)

"""