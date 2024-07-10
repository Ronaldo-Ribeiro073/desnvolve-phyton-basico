"""1) Faça um programa que gere aleatoriamente 20 valores inteiros entre -100 e 100 e os armazene em uma lista. Em seguida imprima na ordem estabelecida:
A lista ordenada, sem modificar a lista original
A lista original
O índice do maior valor da lista
O índice do menor valor da lista"""

#Importando bibliotecas
import random
#Elaborando Lista
lista_Aleatórios = []
for i in range(20):
  valor = random.randint(-100,100)
  lista_Aleatórios.append(valor)
  # imprimindo valores demandados na questão
  print(sorted(lista_Aleatórios))
  print(lista_Aleatórios)
  print( "o maior valor está em", lista_Aleatórios.index(max(lista_Aleatórios)) )
  print( "o menor valor está em", lista_Aleatórios.index(min(lista_Aleatórios)) )