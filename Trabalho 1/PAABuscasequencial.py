import time
import random
#Busca sequencial de elementos

def sequencialBusca(vetor, k):
    i = 0
    while i < len(vetor):
        if vetor[i] == k:
            return i
        i += 1
        
    return -1

#vetor = list(range(0,11))
#random.shuffle(vetor)
#print(vetor)
#k = 1
#antes = time.time()
#posicao = sequencialBusca(vetor, k)
#depois = time.time()
#total = (depois-antes)*1000  
#if posicao >= 0:
#    print("O elemento %d foi encontrado na posição: %d" % (k, posicao))
#else:
#    print("O elemento NÃO foi encontrado.")
#print("O tempo total gasto: %0.2f ms" % total)