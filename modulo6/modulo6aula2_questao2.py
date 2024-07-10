'''2) Faça um programa que gere aleatoriamente um valor entre 5 e 20 e armazene em uma variável chamada num_elementos. 
Em seguida gere aleatoriamente valores entre 1 e 10 em quantidade correspondente a num_elementos, e armazene em uma lista chamada elementos. 
Em seguida imprima:

A lista elementos
A soma dos valores da lista
A média dos valores da lista'''

#Importando bibliotecas
import random
# DAndo valor a variável num_elementos
lista_Aleatórios,elementos = [],[]
num_elementos = random.randint(5,20)

#Elaborando Lista
for i in range(num_elementos):
  valor = random.randint(1,10)
  elementos.append(valor)


print(elementos)
print(sum(elementos))
print((sum(elementos)/len(elementos)))