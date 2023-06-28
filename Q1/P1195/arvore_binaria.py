

class Node:

	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None


def insert(node, key):
    if node is None:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)

    elif key > node.key:
        node.right = insert(node.right, key)

    return node


def printInorder(root):
    if root:
        printInorder(root.left)
         
        print(root.key,end=" ")
         
        printInorder(root.right)

def printPreOrder(node):
    if node is None:
        return
    print(node.key, end = " ")
 
    printPreOrder(node.left)
 
    printPreOrder(node.right)

def printPostOrder(node):
    if node is None:
        return
 
    printPostOrder(node.left)
 
    printPostOrder(node.right)
     
    print(node.key, end = " ")
 
    
    
root = None

trees = []

case = int(input("coloque o número de casos: "))

for _ in range(case):
    tree = input("coloque a arvore: ")
    trees.append(tree)


for tree in trees:
    for node in tree:
        if node.isnumeric() == True:
            root = insert(root, node)


print(f"Em ordem: ")
printInorder(root)

print(f"PreOdem: ")
printPreOrder(root)

print(f"pos Ordem:")

printPostOrder(root)

	

	
