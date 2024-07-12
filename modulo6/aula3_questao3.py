'''3) Crie uma lista com 20 elementos, entre -10 e 10, gerados aleatoriamente. 
Em seguida encontre o intervalo que possui a maior quantidade de números negativos e delete ele da lista com o operador del. 
Você deve imprimir a lista antes e depois da deleção.

Original: [9, 2, -1, 4, -2, -3, 5, 6, -7, -4, -1, 6, 8, -3, -6]
Editada:  [9, 2, -1, 4, -2, -3, 5, 6, 6, 8, -3, -6]'''


import random

# Gerar uma lista com 20 elementos entre -10 e 10
lista = [random.randint(-10, 10) for _ in range(20)]

# Imprimir a lista original
print("Original:", lista)

# Encontrar o intervalo com a maior quantidade de números negativos
max_negativos = 0
start_index = 0

for i in range(len(lista)):
    for j in range(i+1, len(lista)+1):
        sublista = lista[i:j]
        num_negativos = sum(1 for x in sublista if x < 0)
        if num_negativos > max_negativos:
            max_negativos = num_negativos
            start_index = i
            end_index = j

# Deletar o intervalo da lista
del lista[start_index:end_index]

# Imprimir a lista editada
print("Editada:", lista)
