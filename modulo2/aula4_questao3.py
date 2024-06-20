'''
3) Você está desenvolvendo um programa para calcular o preço total de uma compra em uma loja online.
O preço dos produtos é calculado multiplicando a quantidade pelo preço unitário.
Escreva um programa em Python que solicite do usuário o nome, o preço unitário e a quantidade de 3 produtos comprados
e imprima ao final o preço total da compra.
Note no exemplo a seguir que:
Cada entrada de dados tem uma mensagem indicando o dado solicitado (mensagens em itálico, dado de entrada em negrito).
A saída deve estar formatada exatamente como indicado (a string "Total: R$" e o preço com um separador de milhar e duas casas decimais).
'''

# Função para formatar texto em negrito
def negrito(texto):
    return f"\033[1m{texto}\033[0m"

# Função para formatar texto em itálico (alguns terminais podem não suportar)
def italico(texto):
    return f"\033[3m{texto}\033[0m"

# Ler dados do produto 1
nome_produto1 = input(italico("Digite o nome do produto 1: ") + negrito(""))
preco_unitario1 = float(input(italico("Digite o preço unitário do produto 1: ") + negrito("")))
quantidade1 = int(input(italico("Digite a quantidade do produto 1: ") + negrito("")))

# Ler dados do produto 2
nome_produto2 = input(italico("Digite o nome do produto 2: ") + negrito(""))
preco_unitario2 = float(input(italico("Digite o preço unitário do produto 2: ") + negrito("")))
quantidade2 = int(input(italico("Digite a quantidade do produto 2: ") + negrito("")))

# Ler dados do produto 3
nome_produto3 = input(italico("Digite o nome do produto 3: ") + negrito(""))
preco_unitario3 = float(input(italico("Digite o preço unitário do produto 3: ") + negrito("")))
quantidade3 = int(input(italico("Digite a quantidade do produto 3: ") + negrito("")))

# Calcular o preço total de cada produto
preco_total1 = preco_unitario1 * quantidade1
preco_total2 = preco_unitario2 * quantidade2
preco_total3 = preco_unitario3 * quantidade3

# Calcular o preço total da compra
preco_total_compra = preco_total1 + preco_total2 + preco_total3

# Imprimir o resultado formatado
print(italico(f"Total:") + negrito(f" R${preco_total_compra:,.2f}"))
