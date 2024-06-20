'''''
Maria precisa de sua ajuda para organizar os experimentos de seu laboratório. 
Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada. 
Este laboratório utiliza três tipos de cobaias: sapos, ratos e coelhos. 
Entrada: A primeira linha de entrada é um inteiro N com a quantidade de experimentos registrados. 
As N linhas seguintes contém um inteiro Quantia que representa a quantidade de cobaias utilizadas e 
um caractere Tipo ('S', 'R' ou 'C') 
com o tipo de cobaia (S:Sapo, R:Rato ou C:Coelho).
Saída: Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia e 
o percentual de cada uma em relação ao total de cobaias utilizadas'''

# Passo 1: Ler a quantidade de experimentos
n = int(input("Digite a quantidade de experimentos registrados: "))

# Inicializar contadores
total_cobaias = 0
total_sapos = 0
total_ratos = 0
total_coelhos = 0

# Inicializar variável de controle
contador = 0

# Passo 2 e 3: Processar cada experimento usando um while
while contador < n:
    tipo = input("Digite o tipo dessa cobaia, sendo R - Rato, S-Sapo e C-Coelho ")
    quantia = int(input("Digite a quantidade de experimentos com essa cobaia "))
    
    
    # Atualizar o total geral de cobaias
    total_cobaias += quantia
    
    # Atualizar os totais por tipo de cobaia
    if tipo == 'S':
        total_sapos += quantia
    elif tipo == 'R':
        total_ratos += quantia
    elif tipo == 'C':
        total_coelhos += quantia
    
    # Atualizar o contador
    contador += 1

# Calcular os percentuais
percentual_sapos = (total_sapos / total_cobaias) * 100 if total_cobaias > 0 else 0
percentual_ratos = (total_ratos / total_cobaias) * 100 if total_cobaias > 0 else 0
percentual_coelhos = (total_coelhos / total_cobaias) * 100 if total_cobaias > 0 else 0

# Passo 4: Imprimir os resultados
print(f"Total: {total_cobaias} cobaias")
print(f"Total de sapos: {total_sapos}")
print(f"Total de ratos: {total_ratos}")
print(f"Total de coelhos: {total_coelhos}")
print(f"Percentual de sapos: {percentual_sapos:.2f}%")
print(f"Percentual de ratos: {percentual_ratos:.2f}%")
print(f"Percentual de coelhos: {percentual_coelhos:.2f}%")
