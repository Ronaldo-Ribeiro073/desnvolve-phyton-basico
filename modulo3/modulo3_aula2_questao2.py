'''2) Dando continuidade à questão anterior, um outro bar permite a entrada de grupos 
onde pelo menos uma pessoa é maior de idade (ficando responsável pelas outras). 
Ajuste sua resposta da questão anterior, ainda solicitando as idades de Juliana e Cris, 
mas ajustando a expressão para esse novo cenário, imprimindo True se puderem entrar no bar, e False caso contrário.'''


#Entradas
# Idade de Juliana e Idade de Cris
Idade_Juliana = int(input("Digite a idade de Juliana: "))
Idade_Cris = int(input("Digite a idade de Cris: "))

#Processamento Booleano

Podem_entrar = Idade_Cris>=18 or Idade_Juliana>=18
print(Podem_entrar)