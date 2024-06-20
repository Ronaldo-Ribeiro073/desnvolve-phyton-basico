'''1) Juliana e Cris querem entrar em um bar, mas só podem se ambos forem maiores de idade (>17). 
Escreva um programa que solicite as idades de Juliana e Cris e imprima True se ambas forem maiores de 17 anos, 
indicando que podem entrar no bar, e False caso contrário.'''

#Entradas
# Idade de Juliana e Idade de Cris
Idade_Juliana = int(input("Digite a idade de Juliana: "))
Idade_Cris = int(input("Digite a idade de Cris: "))

#Processamento Booleano

Podem_entrar = Idade_Cris>=18 and Idade_Juliana>=18
print(Podem_entrar)