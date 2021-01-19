class Imovel:
    def __init__(self, endereco, preco):
        self.endereco = endereco
        self.preco = preco


class Novo(Imovel):
    def __init__(self, endereco, preco, adicional):
        super().__init__(endereco, preco)
        self.adicional = adicional

    def calcular_preco(self):
        return self.preco + self.adicional


class Velho(Imovel):
    def __init__(self, endereco, preco, desconto):
        super().__init__(endereco, preco)
        self.desconto = desconto

    def calcular_preco(self):
        return self.preco - self.desconto


def separador():
    separador = "=-" * 30
    print(separador)


separador()

imovel1 = Imovel("Rua Silva, 123", 300000.0)
imovel_novo = Novo("Rua Joaquim, 999", 250000.0, 20000.0)
imovel_velho = Velho("Av. Brasil, 777", 500000.0, 35000.0)

print(imovel1.endereco)
print("Preço: R$ %.2f" % imovel1.preco)

separador()

print(imovel_novo.endereco)
print("Preço: R$ %.2f" % imovel_novo.preco)
print("Preço Atualizado: R$ %.2f" % imovel_novo.calcular_preco())

separador()

print(imovel_velho.endereco)
print("Preço: R$ %.2f" % imovel_velho.preco)
print("Preco Atualizado: R$ %.2f" % imovel_velho.calcular_preco())

separador()
