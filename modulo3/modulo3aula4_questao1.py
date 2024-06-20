'''1) Escreva um programa que lê dois números e informa se a sua soma é par ou ímpar. 
Critério: se o resto da divisão do número por 2 for 0, o número é par, caso contrário é ímpar. 
Lembre-se do operador do python % que retorna o resto de uma divisão.'''


n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
soma = n1 + n2
if soma%2 == 0:
 print("O resultado da soma é par!!")
else:
 print("A soma resultou em um número Impar !!! ")