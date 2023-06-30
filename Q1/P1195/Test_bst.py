class BSTNode:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if not self.value:
            self.value = value
            return

        if self.value == value:
            return

        if value < self.value:
            if self.left:
                self.left.insert(value)
                return
            self.left = BSTNode(value)
            return

        if self.right:
            self.right.insert(value)
            return
        self.right = BSTNode(value)

    def inorder(self, values):
        if self.left is not None:
            self.left.inorder(values)
        if self.value is not None:
            values.append(self.value)
        if self.right is not None:
            self.right.inorder(values)
        return values

    def preorder(self, values):
        if self.value is not None:
            values.append(self.value)
        if self.left is not None:
            self.left.preorder(values)
        if self.right is not None:
            self.right.preorder(values)
        return values

    def postorder(self, values):
        if self.left is not None:
            self.left.postorder(values)
        if self.right is not None:
            self.right.postorder(values)
        if self.value is not None:
            values.append(self.value)
        return values

arvores = []
avs = []
case = int(input("coloque o número de casos: "))

for _ in range(case):
    arvore = BSTNode()
    arvores.append(arvore)

for _ in range(case):
    av = input("coloque a arvore: ")
    avs.append(av)

"""for i in range(len(avs)):
    for i range(len(arvores)):
    # if node.isnumeric() == True:"""
    



for i in range(len(arvores)):
    print(f"Case: {i}")
    pre = arvores[i].preorder([])
    print(f"Pre.:{pre}")

"""
nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18]
bst = BSTNode()
for num in nums:
    bst.insert(num)
print("preorder:")
print(bst.preorder([]))
print("#")

print("postorder:")
print(bst.postorder([]))
print("#")

print("inorder:")
print(bst.inorder([]))
print("#")"""