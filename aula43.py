# Molde do Pokemon

# Vamos ter vários atributos

# A classe é o molde que vamos criar para poder conseguirmos construir coisas

class MoldePokemon:
    def __init__(self, nome, altura, peso, hp, ataque, tipo):
        self.nome = nome
        self.altura = altura
        self.peso = peso
        self.hp = hp
        self.ataque = ataque
        self.tipo = tipo

    def mostrar_nome_pokemon(self):
        print(f"O nome do meu pokemon é: {self.nome}")

    def mostrar_altura_pokemon(self):
        print(f"A altura do meu pokemon é: {self.altura}")

    def mostrar_peso_pokemon(self):
        print(f"O peso do meu pokemon é: {self.peso}")

# Chegou a hora de pegar a classe e de fato construir essas coisas
# Por enquanto, a gente ainda tem apenas o molde
# Construir dentro da Orientação a Objetos significa criar um Objeto

pikachu = MoldePokemon("Pikachu", 50, 15, 400, "Choque do Trovão", "Eletrico")
charizard = MoldePokemon("Charizard", 200, 1500, 500, "Lança Chamas", "Fogo")
miau = MoldePokemon("Miau", 50, 15, 100, "Unhada", "Generalista")

pikachu.mostrar_nome_pokemon()
pikachu.mostrar_peso_pokemon()
charizard.mostrar_nome_pokemon()
charizard.mostrar_peso_pokemon()
miau.mostrar_nome_pokemon()