class Node:#Classe representa o nó na árvore binária
    def __init__(self, value):
        self.value = value # Cada nó tem um valor e duas referências para seus filhos left e right
        self.left = None
        self.right = None

def tree_size(node):
    if node is None: # Se o nó for 'NULO' árvore vazia
        return 0
    else:
        return 1 + tree_size(node.left) + tree_size(node.right)
    
