'''
2) Você está criando um sistema de classificação de filmes com base nas avaliações dos usuários.
 Escreva um programa em Python que solicita ao usuário para inserir a avaliação de um filme em uma escala de 1 a 5. 
 O programa deve imprimir uma mensagem correspondente à classificação do filme:
Se a avaliação for 5, imprima "Excelente!"
Se a avaliação for 4, imprima "Muito Bom!"
Se a avaliação for 3, imprima "Bom!"
Se a avaliação for 2, imprima "Regular."
Se a avaliação for 1, imprima "Ruim."
'''

avaliação_filme = int(input("Avalie o filme um a cinco sendo, 5 excelente e 1 ruim: "))

if(avaliação_filme == 5):
    print("Excelente")
if(avaliação_filme == 4):
    print("Muito bom")
if(avaliação_filme == 3):
    print("Bom!")
if(avaliação_filme == 3):
    print("Regular")
if(avaliação_filme == 1):
    print("Ruim")

