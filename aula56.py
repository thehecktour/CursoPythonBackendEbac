
# 1 2 3 4 5 6 7 8 9 10

# 1 4 9 16 25 36 49 64 81 100

quadrados_impares = [elemento**2 for elemento in range(1,11) if elemento % 2 != 0]

novo_arrayzinho = []

for elemento in range(1,11):
    novo_arrayzinho.append(elemento**2)


for elemento in novo_arrayzinho:
    if elemento % 2 != 0:
        print(elemento)