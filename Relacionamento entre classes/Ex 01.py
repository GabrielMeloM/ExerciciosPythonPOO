class Carro:
    def __init__(self, marca, modelo, placa, ano):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.ano = ano


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.carro = None

    def comprar_carro(self, carro):
        self.carro = carro


meu_carro = Carro('Volkswagen', 'Gol', 'AAA-1111', 2015)
eu = Pessoa("Gabriel", 18)
eu.comprar_carro(meu_carro)
print("Meu nome:", eu.nome)
print("Modelo do meu carro:", eu.carro.modelo)
print("Placa do meu carro:", eu.carro.placa)
