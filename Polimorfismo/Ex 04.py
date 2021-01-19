from abc import ABC, abstractmethod


class Funcionario(ABC):
    def __init__(self, nome, matricula, salario_base):
        self.nome = nome
        self.matricula = matricula
        self.salario_base = salario_base

    @abstractmethod
    def calcular_salario(self):
        pass


class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario_base):
        super().__init__(nome, matricula, salario_base)

    def calcular_salario(self):
        return self.salario_base * 2


class Assistente(Funcionario):
    def __init__(self, nome, matricula, salario_base):
        super().__init__(nome, matricula, salario_base)

    def calcular_salario(self):
        return self.salario_base


class Vendendor(Funcionario):
    def __init__(self, nome, matricula, salario_base):
        super().__init__(nome, matricula, salario_base)

    def calcular_salario(self):
        return self.salario_base + (self.salario_base * 0.10)


ger = Gerente("gabriel", 123456, 1500)
assist = Assistente("Jõao", 246810, 850)
vend = Vendendor("Pedro", 13579, 1000)

func = [ger, assist, vend]
for i in func:
    print(i.nome, "R$ %.2f" % i.calcular_salario())
