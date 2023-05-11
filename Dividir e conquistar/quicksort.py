def quicksort(arr):
    if len(arr) <= 1:
        return arr  # Caso base, retorna o array se ele tiver tamanho <= 1
    pivot = arr[0]  # Seleciona o primeiro elemento como pivô
    left = []
    right = []
    for x in arr[1:]:
        if x < pivot:
            left.append(x)  # Adiciona elementos menores que o pivô à lista da esquerda
        else:
            right.append(x)  # Adiciona elementos maiores ou iguais ao pivô à lista da direita
    return quicksort(left) + [pivot] + quicksort(right)  # Chama recursivamente o quicksort para as duas sublistas e concatena com o pivô


'''
Caso médio O (n log n)
Pior caso O(n^2)
Melhor caso T(n) = 2T(n/2)+n = O(n log n)

'''

















my_list = [3, 7, 1, 9, 2, 5, 8]
print("Lista original:", my_list)
sorted_list = quicksort(my_list)
print("Lista ordenada:", sorted_list)