

'''
5) Solicite de um usuário seu gênero ("M" ou "F"), sua idade e seu tempo de serviço (em anos) e 
escreva uma expressão que imprima True se a pessoa já pode se aposentar, 
ou False caso contrário, de acordo com as seguintes regras:
A: Para mulheres, ter mais de 60 anos. Para homens, 65.
B: Ou ter trabalhado pelo menos 30 anos
C: Ou ter 60 anos  e trabalhado pelo menos 25.'''


#Entrada de Dados:
# Genero, Idade e Tempo de Serviço

Genero = input("Digite o genero,"\
               " sendo M para Masculino e F para Feminino: \
                ") 
Idade  = int(input("Digite a Idade: "))
Tempo  = int(input("Digite quantos anos de Contribuição: "))

#Processamento
Por_Idade  = ( Genero == 'M' and Idade >= 65 or \
                   Genero == 'F'and Idade>=60 )
Por_Tempo = (Tempo >= 30)
Por_I_T = ( Tempo>=25 and Idade >= 60)
Pode_Aposentar = Por_Idade or Por_I_T or Por_Tempo

print("Pode Aposentar: ", Pode_Aposentar)