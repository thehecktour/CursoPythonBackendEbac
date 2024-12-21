# Retorne a media de todos os salarios, com exceção do maior e menor

array_de_salariozinhos = [4000,3000,1000,2000,5000,6000,500,4500,4700]

novo_arrayzinho = sorted(array_de_salariozinhos)

novo_arrayzinho.remove(novo_arrayzinho[0])
novo_arrayzinho.remove(novo_arrayzinho[-1])

media_dos_salarios = 0

for salario in novo_arrayzinho:
    media_dos_salarios += salario


print(media_dos_salarios // len(novo_arrayzinho))