class Filme:
    def __init__(self, titulo, genero):
        self.__titulo = titulo
        self.__genero = genero

    def get_titulo(self):
        return self.__titulo

    def get_genero(self):
        return self.__genero

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_genero(self, genero):
        self.__genero = genero


lista = []
for i in range(3):
    titulo = input("Titulo: ")
    genero = input("Genêro: ")
    lista.append(titulo)
    lista.append(genero)

print("Os filmes e generos informados foram", lista)
