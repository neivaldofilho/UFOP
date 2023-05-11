def find_max_position(arr):# Função que recebe arranjo como entrada
    n = len(arr) #define n
    if n == 1: # verifica o tamanho do arranjo
        return 0
    
    mid = n // 2 # dividi o arranjo n/2
    left_max_pos = find_max_position(arr[:mid]) #posição do maior elemento na primeira metade
    right_max_pos = find_max_position(arr[mid:]) #posição do maior elemento na segunda metade
    
    if arr[left_max_pos] > arr[right_max_pos]:# comparação 'Operação básica'
        return left_max_pos
    else:
        return right_max_pos + mid
    
    
    '''
    Para melhor balanceamento (n-1)^2
    Expressão matematica é uma somatorio: T(n) = 2T(n/2)+1 
    Recorrência 
    Classe de eficiência O(n)
    '''