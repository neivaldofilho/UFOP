def selectsort(array):
    for i in range(0, len(array)):# faz a busca no array começando da posição 0 até o final, em busca no menor valor 
        min_i = i # atribui a variavel o menor valor
        for j in range(i + 1, len(array)):# nova busca comecando do proximo elemento(j) e faz a comparação até o ultimo elemento.
            if array[j] < array[min_i]: #comparacao  e depois faz a atribuicao
                min_i = j      
        array[i], array[min_i] = array[min_i], array[i]#troca de posições no array 
        
array = [9 ,4, 6, 3, 7, 5, 1, 11, 8, 8, 2]
selectsort(array)
print(array)