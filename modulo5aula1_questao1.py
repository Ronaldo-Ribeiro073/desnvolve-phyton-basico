''' 
1)Desenvolva um programa em Python que peça ao usuário para inserir dois números decimais e 
calcule a diferença absoluta entre esses dois números. Utilize a função nativa abs para garantir 
que o resultado seja sempre positivo e round para arredondar o resultado para duas casas decimais.

Exemplo de interação:'''

  # Solicita ao usuário que insira os dois números decimais
numero1 = float(input("Digite o primeiro número decimal: "))
numero2 = float(input("Digite o segundo número decimal: "))
    
    # Calcula a diferença do módulo ou diferença absoluta entre os dois números  
diferenca_absoluta = abs(numero1 - numero2)
    # Arredonda o resultado para duas casas decimais
arredondadodamento = round(diferenca_absoluta, 2)
    
    # Exibe o resultado
print(f"A diferença absoluta entre {numero1} e {numero2} é {arredondadodamento}")