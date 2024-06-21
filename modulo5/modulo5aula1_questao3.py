'''Escreva um programa em Python que utiliza a biblioteca random para gerar um número aleatório entre 1 e 10 e 
peça ao usuário para adivinhar o número. Forneça feedback se o palpite é muito alto, muito baixo ou correto. 
Interrompa a execução somente quando o usuário acertar o palpite.

Exemplo de interação:
Adivinhe o número entre 1 e 10: 5
Muito alto, tente novamente!
Adivinhe o número entre 1 e 10: 3
Correto! O número é 3. '''

import random

# Gera um número aleatório entre 1 e 10
numero_aleatorio = random.randint(1, 10)

while True:
    # Pede ao usuário para adivinhar o número
    valor_chute = int(input("Chute o valor do número gerado aleatoriamente: "))
    
    # Verifica se o palpite está correto
    if valor_chute == numero_aleatorio:
        print(f"Acertou, o valor gerado foi {numero_aleatorio}.")
        break
    # Verifica se o palpite é muito alto
    elif valor_chute > numero_aleatorio:
        print("Chutou alto, tente de novo")
    # Verifica se o palpite é muito baixo
    elif valor_chute < numero_aleatorio:
        print("Chutou demais, tente de novo")
    # Condição extra: diferença de 1
    if abs(valor_chute - numero_aleatorio) == 1:
        print("Passou raspando, mas não foi dessa vez")

