#4) Escreva um programa que leia um valor inteiro referente a uma quantia em reais e 
#calcule a menor quantidade possível de notas necessárias para pagar aquele valor. 
#As notas possíveis são: 100, 50, 20, 10, 5, 2, 1. A saída deve estar formatada exatamente como indicado. 
'''
Entrada:
576

Saída:
5 nota(s) de R$100,00
1 nota(s) de R$50,00
1 nota(s) de R$20,00
0 nota(s) de R$10,00
1 nota(s) de R$5,00
0 nota(s) de R$2,00
1 nota(s) de R$1,00'''

valor =int(input( "Digite o Valor,please: ") )
print(valor)
notas_100 = valor//100
valor = valor%100 # Valor recebe o resto

notas_50 = valor//50
valor = valor%50

notas_20 = valor//20
valor = valor%20

notas_10 = valor//20
valor = valor%10

notas_5 = valor//5
valor = valor%5

moeda_de_1_real = valor//1
valor = valor%1

print(f"{notas_100} notas de 100")
print(f"{notas_50} notas de 50")
print(f"{notas_20} notas de 20")
print(f"{notas_10} notas de 10")
print(f"{notas_5} notas de 5")
print(f"{moeda_de_1_real} notas de 1")