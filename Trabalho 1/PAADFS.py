
from collections import deque

class Graph:# Uma classe para representar um objeto gráfico
    def __init__(self, edges, n):# Construtor
        self.adjList = [[] for _ in range(n)]# Uma lista de listas para representar uma lista de adjacências
        for (src, dest) in edges:# adiciona arestas ao gráfico não direcionado
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
def iterativeDFS(graph, v, discovered):# Executa DFS iterativo no gráfico a partir do vértice `v`   
    stack = deque()# cria uma Stack(Pilha) usada para fazer DFS iterativo
    stack.append(v)# empurra o nó de origem para a Stack(Pilha)
    while stack:# loop até que a Stack esteja vazia
        v = stack.pop()# Retire um vértice da Stack(Pilha)
        if discovered[v]:# se o vértice já foi descoberto, ignore-o
            continue
        discovered[v] = True# chegaremos aqui se o vértice que apareceu `v` ainda não foi descoberto;
        print(v, end=' ')# imprime `v` e processa seus nós adjacentes não descobertos na Stack(Pilha)
        adjList = graph.adjList[v]# faz para cada aresta (v, u)
        for i in reversed(range(len(adjList))):
            u = adjList[i]
            if not discovered[u]:
                stack.append(u)