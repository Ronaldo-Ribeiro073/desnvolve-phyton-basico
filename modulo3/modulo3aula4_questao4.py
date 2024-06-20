'''''
4) Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete com base na distância 
e no peso do pacote. Escreva um código que solicita a distância da entrega em quilômetros e o peso do pacote em quilogramas. 
O programa deve calcular e imprimir o valor do frete de acordo com as seguintes regras:
Distância até 100 km: R$1 por kg.
Distância entre 101 e 300 km: R$1.50 por kg.
Distância acima de 300 km: R$2 por kg.
Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg  '''

# Solicita a distância da entrega em quilômetros
distancia = float(input("Digite a distância da entrega em quilômetros: "))

# Solicita o peso do pacote em quilos
peso = float(input("Digite o peso do pacote em quilogramas: "))

# Calcula o valor do frete considerando a distância
if distancia <= 100:
    valor_frete = 1 * peso
elif 101 <= distancia <= 300:
    valor_frete = 1.50 * peso
else:  # distancia > 300
    valor_frete = 2 * peso

# Acrescenta  R$10 para pacotes com peso superior a 10 kg
if peso > 10:
    valor_frete += 10

# Imprime o valor do frete
print("O valor do frete é: R$", valor_frete)
