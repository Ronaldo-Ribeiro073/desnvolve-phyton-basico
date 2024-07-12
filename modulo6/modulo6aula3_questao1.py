


# Inicializar a lista de números
numeros = []

# Solicitar ao usuário o tamanho da lista (pelo menos 4)
while True:
    tamanho_lista = int(input('Digite a quantidade de números inteiros na lista (pelo menos 4): '))
    if tamanho_lista < 4:
        print("Você deve inserir pelo menos 4 números.")
    else:
        break

# Solicitar ao usuário os números inteiros
print(f'Digite os {tamanho_lista} números inteiros:')
for _ in range(tamanho_lista):
    numero = int(input())
    numeros.append(numero)

# Imprimir a lista completa
print("Lista completa:", numeros)

# Imprimir os três primeiros elementos
print("Os três primeiros elementos:", numeros[:3])

# Imprimir os três últimos elementos
print("Os três últimos elementos:", numeros[-3:])

# Imprimir a lista invertida
print("Lista invertida:", numeros[::-1])

# Imprimir a lista pulando de dois em dois elementos, posição par
print("Elementos na posição par (pulos de 2 em 2):", numeros[::2])

# Imprimir a lista pulando de dois em dois elementos, posição ímpar
print("Elementos na posição ímpar (pulos de 2 em 2):", numeros[1::2])

