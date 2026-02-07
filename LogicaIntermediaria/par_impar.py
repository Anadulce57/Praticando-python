# Crie um algoritmo que receba um número inteiro. - informar se é par, ímpar e múltiplo de 5 
num = int(input("Digite o número desejado: "))

if num %2 == 0:
    print("O número é par!")

    if num %5 == 0:
        print("O número também é múltiplo de 5")

elif num %2 != 0: 
    print("O número é ímpar!")

    if num %5 == 0:
        print("O número também é múltiplo de 5")