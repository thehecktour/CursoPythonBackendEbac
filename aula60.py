try:
    numero = int(input("Digite um numero: "))
    resultado = 10 / numero
    print(resultado)
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um número")
except ZeroDivisionError:
    print("Não existe divisão por zero!")