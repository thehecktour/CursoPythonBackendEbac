# Você recebe um array de números inteiros positivos.
# Alice e Bob estão jogando.
# No jogo, Alice pode escolher todos os números de um dígito ou todos os números de dois dígitos de meu_arrayzinho. 
# E o restante dos números é dado a Bob. 
# Alice ganha se a soma dos seus números for estritamente maior que a soma dos números de Bob.
# Retorne verdadeiro se Alice puder vencer este jogo, caso contrário, retorne falso.

meu_arrayzinho = [1,2,3,4,10,30,20,10,50,100]
alice = 0
bob = 0

for numero in meu_arrayzinho:
    if numero >= 100:
        bob += numero
    else:
        alice += numero


if alice > bob:
    print("Alice ganhou")
else:
    print("Bob ganhou")