import random
num = random.randint(1,100)
print("Esse é um jogo de adivinhação, entre os números de 1 a 100")
tentativa = int(input("Digite um número para tentar adivinhar: "))
while tentativa != num:
    tentativa = int(input("Digite um número para tentar adivinhar: "))
    if tentativa > num:
        print("O numéro que vc digitou é maior que o secreto")
    elif tentativa < num:
        print("O numéro que vc digitou é menor que o secreto")
    else:
        print("Você acertou!!!")
        print(num)