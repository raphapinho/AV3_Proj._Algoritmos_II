class BST:
    def __init__(self, val=None):
        self.esq = None
        self.dir = None
        self.val = val

    def inserir(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.esq:
                self.esq.inserir(val)
                return
            self.esq = BST(val)
            return

        if self.dir:
            self.dir.inserir(val)
            return
        self.dir = BST(val)

    def emOrdem(self, vals):
        if self.esq is not None:
            self.esq.emOrdem(vals)
        if self.val is not None:
            print(self.val, end= " ")
        if self.dir is not None:
            self.dir.emOrdem(vals)
        # return vals

    def preOrdem(self, vals):
        if self.val is not None:
            print(self.val, end= " ")
        if self.esq is not None:
            self.esq.preOrdem(vals)
        if self.dir is not None:
            self.dir.preOrdem(vals)
        # return vals

    def posOrdem(self, vals):
        if self.esq is not None:
            self.esq.posOrdem(vals)
        if self.dir is not None:
            self.dir.posOrdem(vals)
        if self.val is not None:
            print(self.val, end= " ")
        # return vals

arvores = []


case = int(input("coloque o número de casos: "))
    

#criando objetos e atribuindo valores
for _ in range(case):
    arvore = BST()
    # n = int(input("coloque o tamanho: "))

    av = input("coloque a arvore: ")
    for i in range(len(av)):
        if av[i].isnumeric():
            BST.inserir(arvore,av[i])
        
    
    arvores.append(arvore)

#imprimindo pre, em e posOrdem
for i in range(len(arvores)):
    print(f"Case: {i+1}")
    

    print("Pre.:", end= " ")
    arvores[i].preOrdem([])
    
    print("\nEm..:", end= " ")
    arvores[i].emOrdem([])
    
    print("\nPos.:", end= " ")
    arvores[i].posOrdem([])
    
    print("")
