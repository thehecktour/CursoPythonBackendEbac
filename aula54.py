# A tradução da língua Berland para a língua Birland não é uma tarefa fácil. 
# Essas línguas são muito semelhantes: 
# Uma palavra berlandesa difere um pouco de uma palavra birlandesa com o mesmo significado: 
# é escrita (e pronunciada) inversamente. 
# Por exemplo, palavra berlandês "code" corresponde a uma palavra birlandesa "edoc". 
# Porém, cometer um erro durante a “tradução” é fácil. 
# Vasya traduziu a palavra s de Berlandish para Birlandish como t. 
# Ajude-o: descubra se ele traduziu a palavra corretamente.

# o que significa inversamente?
# o que significa traduzir?
# ele espera que eu traduza como?
# ele espera que eu compare duas strings?
# tem alguma coisa que eu to deixando passar?

primeira_stringzinha = "code"
segunda_stringzinha = "edoc"

# edoc
# code == code

if primeira_stringzinha == segunda_stringzinha[::-1]:
    print("Passou no teste!!!")
else:
    print("reprovado")