def meu_decorator(func):
    def wrapper():
        print("Antes da execução da minha função!")
        func()
        print("Depois da execução da minha função!")
    return wrapper



@meu_decorator
def despedida():
    print("Tchau!")


@meu_decorator
def cheguei():
    print("Oiiii")

cheguei()
despedida()