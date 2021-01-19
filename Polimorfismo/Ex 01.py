class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def emitir_som(self):
        print("Au! Au!")


class Gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def emitir_som(self):
        print("Miau!!")


class Cavalo(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def emitir_som(self):
        print("Hinn in in")


class Veterinario:
    def examinar(self, animal):
        return animal.emitir_som()


def separador():
    a = "=-" * 30
    print(a)


separador()
dog = Cachorro("Rex", 3)
cat = Gato("Tina", 1)
horse = Cavalo("Horse", 6)

dog.emitir_som()
horse.emitir_som()
cat.emitir_som()

separador()
print("Veterinário Examinando:")

vet = Veterinario()
vet.examinar(dog)
vet.examinar(cat)
vet.examinar(horse)

separador()
