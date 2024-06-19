# 1) Faça um programa para ler as dimensões de um terreno em inteiros (comprimento e largura),
# bem como o preço do metro quadrado da região em ponto flutuante. ]
#Calcule o valor do terreno e imprima o resultado com a formatação apresentada a seguir.

#O terreno possui 250m2 e custa R$512,490.50

#Comente na linha acima de cada instrução uma breve descrição da instrução.


### Digite os valores de entrada: 25,10 e 2049.96 para testar a saída de exemplo

# Ler as dimensões do terreno
comprimento = int(input("Digite o comprimento do terreno em metros: "))
# Ler a largura do terreno
largura = int(input("Digite a largura do terreno em metros: "))
# Ler o preço do metro quadrado da região
preco_m2 = float(input("Digite o preço do metro quadrado em reais: "))

# Calcular a área do terreno
area_m2 = comprimento * largura
# Calcular o preço total do terreno
preco_total = preco_m2 * area_m2

# Imprimir o resultado formatado
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")


