#BFS - Algoritmo para Busca em Largura
#importa a biblioteca para poder criar uma lista
from collections import defaultdict 
 
#1-classe para criação do grafo direcionado e que usa representação de lista de adjacência
#2-constroi a função, cria a lista 
#3-Quando você cria um defaultdict, fornece uma função usada para criar valores, nesse caso criou-se a lista
#4-função que adiciona os vértices no grafo
#5-função para imprimir a BFS do grafo, recebe o primeiro nó a ser visitado 
#6-marca todos os vértices como não visitados.
#7-cria uma fila vazia para o BFS
#8-pega o nó de origem, marca como visitado e insere ele na fila
#9-enquanto a fila não for vazia
#10-retira o último vértice inserido na fila e imprime
#11-Obtenha todos os vértices adjacentes dos vértices desenfileirados. Se um adjacente não foi visitado, marque-o como visitado e coloque-o na fila

class Graph:#1
    def __init__(self):#2
        self.graph = defaultdict(list)#3
    def addEdge(self,u,v):#4
        self.graph[u].append(v) 
    def BFS(self, s):#5
        visited = [False] * (len(self.graph)) #6
        queue = [] #7
        queue.append(s)#8 
        visited[s] = True #8
        while queue: #9
            s = queue.pop(0) #10
            for i in self.graph[s]: #11
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True