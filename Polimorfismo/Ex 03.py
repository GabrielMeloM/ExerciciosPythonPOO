from abc import ABC, abstractmethod


class Veiculo(ABC):

    @abstractmethod
    def limpar(self):
        print("Bicicleta/Veículo foi limpo.")

    @abstractmethod
    def consertar(self):
        print("Bicicleta/Veículo foi consertado.")


class Bicicleta(Veiculo):
    def limpar(self):
        print("Bicicleta/Veículo foi limpo.")

    def consertar(self):
        print("Bicicleta/Veículo foi consertado.")


class Automovel(Veiculo):
    def limpar(self):
        print("Bicicleta/Veículo foi limpo.")

    def consertar(self):
        print("Bicicleta/Veículo foi consertado.")
        print("O óleo foi trocado.")

    def trocar_oleo(self):
        print("O óleo foi trocado.")


def separador():
    separador = "=-" * 17
    print(separador)


bike = Bicicleta()
carro = Automovel()

separador()
print("Bicicleta:")
bike.limpar()
bike.consertar()

separador()
print("Carro:")
carro.limpar()
carro.consertar()
carro.trocar_oleo()
separador()
