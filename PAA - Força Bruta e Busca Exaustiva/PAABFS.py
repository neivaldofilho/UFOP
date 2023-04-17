#BFS - Algoritmo para Busca em Largura
#importa a biblioteca para poder criar uma lista
from collections import defaultdict 

class Graph:# Classe grafo, criação da lista adjacente
    def __init__(self):# funcao cria lista
        self.graph = defaultdict(list)# fornece uma funcao para criar valores
    def addEdge(self,u,v):# funcao adiciona vertices do grafo
        self.graph[u].append(v) 
    def BFS(self, s):# funcao de busca em largura, recebe o nó do grafo para ser vizitado
        visited = [False] * (len(self.graph)) # marca todos os vertices como não visitados
        queue = [] # cria uma fila vazia para a funcao BFS
        queue.append(s)# pega o nó de origem
        visited[s] = True # marca o nó como visitado e insere na fila
        while queue: # funcao basica, enquanto a fila não for vazia
            s = queue.pop(0) # retira o ultimo vertice inserido
            print (s, " ") # imprime o vertice
            # Obtenha todos os vértices adjacentes dos vértices desenfileirados. 
            # Se um adjacente não foi visitado, marque-o como visitado e coloque-o na fila
            for i in self.graph[s]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True
                    
# Criação do grafo
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
 
print ("Segue a execução do BFS, começando pelo vértice 2")
g.BFS(2) 