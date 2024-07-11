'''4) Crie um programa em Python que receba duas listas de números do usuário, podendo cada lista ter uma quantidade diferente de valores. 
Em seguida, combine essas duas listas de forma alternada para formar uma terceira lista. Intercale os elementos até o final da primeira lista, 
adicionando ao final os elementos remanescentes da maior lista.

Exemplo de interação via terminal (entradas em negrito):

Digite a quantidade de elementos da lista 1: 4'''


'''Digite a quantidade de elementos da lista 1: 4
Digite os 4 elementos da lista 1:
1
2
3
4Digite a quantidade de elementos da lista 2: 6
Digite os 6 elementos da lista 2:
5
6
7
8
9
10Lista intercalada: 1 5 2 6 3 7 4 8 9 10'''

# Obter a quantidade de elementos da lista 1
quantidade1 = int(input('Digite a quantidade de elementos da lista 1: '))

# Obter os elementos da lista 1
lista1 = []
print(f'Digite os {quantidade1} elementos da lista 1:')
for _ in range(quantidade1):
    elemento = int(input())
    lista1.append(elemento)

# Obter a quantidade de elementos da lista 2
quantidade2 = int(input('Digite a quantidade de elementos da lista 2: '))

# Obter os elementos da lista 2
lista2 = []
print(f'Digite os {quantidade2} elementos da lista 2:')
for _ in range(quantidade2):
    elemento = int(input())
    lista2.append(elemento)

# Criar a lista intercalada
lista_intercalada = []
min_len = min(quantidade1, quantidade2)

# Intercalar os elementos das duas listas
for i in range(min_len):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])

# Adicionar os elementos remanescentes da lista maior
if quantidade1 > quantidade2:
    lista_intercalada.extend(lista1[min_len:])
else:
    lista_intercalada.extend(lista2[min_len:])

# Exibir a lista intercalada
print('Lista intercalada:', ' '.join(map(str, lista_intercalada)))

