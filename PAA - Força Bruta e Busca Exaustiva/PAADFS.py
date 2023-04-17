
from collections import deque

class Graph:# classe do grafo
    def __init__(self, edges, n):# funcao cria lista
        self.adjList = [[] for _ in range(n)]# Uma lista de listas para representar uma lista de adjacências
        for (src, dest) in edges:# adiciona arestas ao gráfico não direcionado
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
def DFS(graph, v, discovered):# Executa DFS no gráfico a partir do vértice `v`   
    stack = deque()# cria uma Stack(Pilha) usada para fazer a busca em profundidade
    stack.append(v)# empurra o nó de origem para a Stack(Pilha)
    while stack:# enquanto(loop) até que a Stack(Pilha) esteja vazia
        v = stack.pop()# Retire um vértice da Stack(Pilha)
        if discovered[v]:# se o vértice já foi descoberto, ignore-o
            continue
        discovered[v] = True# aqui se o vértice que apareceu `v` ainda não foi descoberto;
        print(v, end=' ')# imprime `v` e processa seus nós adjacentes não descobertos na Stack(Pilha)
        adjList = graph.adjList[v]# faz para cada aresta (v, u)
        for i in reversed(range(len(adjList))):
            u = adjList[i]
            if not discovered[u]:
                stack.append(u)
                
if __name__ == '__main__':
 
    # Lista de arestas do gráfico conforme o diagrama acima
    edges = [
        # Observe que o nó 0 está desconectado
        (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (8, 9), (8, 12), (9, 10), (9, 11)
        #(6, 9) introduces a cycle
    ]
 
    # número total de nós no gráfico (rotulado de 0 a 12)
    n = 13
 
    # constrói um gráfico a partir das arestas dadas
    graph = Graph(edges, n)
 
    # para acompanhar se um vértice é descoberto ou não
    discovered = [False] * n
 
    # Faz a travessia iterativa do DFS de todos os nós não descobertos para
    # cobre todos os componentes conectados de um gráfico
    for i in range(n):
        if not discovered[i]:
            DFS(graph, i, discovered)