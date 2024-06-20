n = float(input("Digite um número"))
maior = 0
while n > 0:
    x = float(input())
    if x > maior:
        maior = x
        n = n-1
    else:
        n = n-1
print(maior)
