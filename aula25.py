# Dado um endereço IP válido (IPv4), retorne uma versão ajustada desse endereço IP.
# Um endereço IP ajustado substitui cada ponto "." por "[.]".

# Endereço Original = 1.1.1.1
# Versão Ajustada = 1[.]1[.]1[.]1

# 1. Receber a string com nosso endereço IP

endereco_ip = input()

# 2. Fazer a operação para substituir os pontos por parenteses e ponto

novo_endereco_ip = ""

for i in endereco_ip:
    if i == ".":
        novo_endereco_ip += "[.]"
    else:
        novo_endereco_ip += i

print(novo_endereco_ip)

# 1.1.1.1
# 0123456

# 1[.]1[.]1[.]1