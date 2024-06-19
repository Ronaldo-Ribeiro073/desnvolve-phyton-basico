#2) Leia um valor inteiro correspondente a uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
#Fórmula de conversão: C = (F - 32) * (5/9), sendo C o valor em graus Celsius e F o valor em Fahrenheit. ]
#Antes de imprimir, converta o valor em Celsius para inteiro. A mensagem deve estar formatada da seguinte maneira:

#86 graus Fahrenheit são 30 graus Celsius.

# F representa Fahrenheit e C representa Celsius
#Leitura da temperatura em Fahrenheit
F = int(input("Digite a temperatura em farenheith: "))
C = (F - 32) * (5/9)
print(f"A temperatura fornecida(F) é {C}° graus Celsius")

