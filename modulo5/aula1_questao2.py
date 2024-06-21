import math
import random

n = int(input("Digite o valor de n (quantidade de números inteiros aleatórios a serem gerados): "))
    
    # Passo 3: Gerar n valores inteiros aleatórios entre 0 e 100
valores = [random.randint(0, 100) for _ in range(n)]
    
    # Passo 4: Calcular a soma dos valores
soma = sum(valores)
    
    # Passo 5: Calcular a raiz quadrada da soma
raiz_quadrada = math.sqrt(soma)
    
    # Passo 6: Imprimir o resultado com duas casas decimais
print(f"A raiz quadrada da soma dos {n} valores inteiros aleatórios gerados é: {raiz_quadrada:.2f}")
