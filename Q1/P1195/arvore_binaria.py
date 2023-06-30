

class Node:

	def __init__(self, key):
		self.key =  key
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


def printInorder(node):
    if node:

        printInorder(node.left)
        
        print(node.key, end = " ")
        
        printInorder(node.right)

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
    
    
    
# node = None
valores = []
arvores = []

case = int(input("coloque o número de caso: "))

for i in range(case):
    valores.append(i+1)

for i in enumerate(valores):
    arvore = f"arvore_{i}"  # Nome da variável usando o índice do loop
    arvores.append(exec(f"{arvore} = {None}"))  # Criação da variável dinamicamente usando 'exec'



for arvore in arvores:
    arvore = None
    insert(arvore, 2)
print(arvores)


"""tree1 = None
tree1 = insert(tree1,3)
tree1 =insert(tree1,5)
tree1 =insert(tree1,4)
tree1 =insert(tree1,2)"""





"""tree2 = Node(None)
tree2 = None

tree2 = insert(tree2,2)
tree2 = insert(tree2,1)
tree2 = insert(tree2,7)
tree2 = insert(tree2,5)
tree2 = insert(tree2,3)
"""

"""trees = []

case = int(input("coloque o número de casos: "))

for _ in range(case):
    tree = input("coloque a arvore: ")
    trees.append(tree)


for tree in trees:
    for node in tree:
        if node.isnumeric() == True:
            node = insert(node, node)"""

print(f"Em ordem: \n{printInorder(tree1)} ")


"""

print(f"PreOdem: ")
printPreOrder(tree1)

print(f"pos Ordem:")

printPostOrder(tree1)

print(f"Em ordem: ")
printInorder(tree2)

print(f"PreOdem: ")
printPreOrder(tree2)

print(f"pos Ordem:")

printPostOrder(tree2)"""

	

	
