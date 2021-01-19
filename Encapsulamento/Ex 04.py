class CarroCorrida:
    def __init__(self, numero, piloto, velocidade_maxima):
        self.__numero = numero
        self.__piloto = piloto
        self.__velocidade_maxima = velocidade_maxima
        self.__velocidade_atual = 0
        self.__ligado = False

    def ligar(self):
        self.__ligado = True
        return self.__ligado

    def desligar(self):
        self.__ligado = False
        return self.__ligado

    def acelerar(self, velocidade):
        self.__velocidade_atual += velocidade
        return self.__velocidade_atual

    def frear(self):
        self.__velocidade_atual = 0
        return self.__velocidade_atual

    def get_velocidade_atual(self):
        if self.__ligado is False:
            self.__velocidade_atual = 0
            return self.__velocidade_atual
        elif self.__ligado is True:
            if self.__velocidade_atual < self.__velocidade_maxima:
                return self.__velocidade_atual
            else:
                return "150, não ultrapassar a velocidade maxima."
        elif carro.frear():
            self.__velocidade_atual = 0


carro = CarroCorrida(1, "Paulo", 150)
carro.acelerar(20)
print(carro.get_velocidade_atual())
carro.ligar()
carro.acelerar(20)
print(carro.get_velocidade_atual())
carro.acelerar(80)
print(carro.get_velocidade_atual())
carro.acelerar(70)
print(carro.get_velocidade_atual())
carro.frear()
print(carro.get_velocidade_atual())
