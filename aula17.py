# Escreva um programa que receba três números e exiba o segundo maior número entre eles.

# 1. Preciso receber esses numeros separadamente

numero1, numero2, numero3 = map(int, input().split())

# 2. Criar uma lógica para ver quem é o segundo maior

arrayzinho = []

arrayzinho.append(numero1)
arrayzinho.append(numero2)
arrayzinho.append(numero3)

arrayzinho.sort()

# 3. Mostrar na tela quem é o vencedor, ou seja, quem é o segundo maior

print(arrayzinho[1])