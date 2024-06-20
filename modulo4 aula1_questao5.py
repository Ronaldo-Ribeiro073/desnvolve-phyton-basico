'''Um instituto realizou uma pesquisa de público e precisa calcular a média de idade dos respondentes. 
Escreva um programa que leia um inteiro N com a quantidade de respondentes e em seguida leia as N idades de cada respondente. 
Ao final, imprima a média das idades.
(idade1 + idade2 + idade3 + … + idade_n)/N
'''


# Passo 1: Ler a quantidade de respondentes
N = int(input("Digite a quantidade de respondentes: "))

# Inicializar a variável para armazenar a soma das idades
soma_idades = 0

# Inicializar contador para controlar a quantidade de idades lidas
contador = 0  

# Passo 2: Ler as idades dos respondentes e calcular a soma das idades
while contador < N:
    idade = int(input(f"Digite a idade do respondente {contador + 1}: "))
    soma_idades += idade
    contador += 1

# Passo 3: Calcular a média das idades
if N > 0:
    media_idades = soma_idades / N
    print(f"A média das idades dos respondentes é: {media_idades:.2f}")