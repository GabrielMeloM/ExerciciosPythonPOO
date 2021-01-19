class Cliente:
    def __init__(self, nome, cpf, senha):
        self.nome = nome
        self.__cpf = cpf
        self.__senha = senha

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def get_senha(self):
        return self.__senha


class ContaBancaria:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.__saldo = 0

    def get_saldo(self, senha):
        return self.__saldo

    def depositar(self, valor, senha):
        if senha == self.cliente.get_senha():
            self.__saldo += valor
        else:
            print("Senha Inválida")

    def sacar(self, valor, senha):
        if senha == self.cliente.get_senha():
            self.__saldo -= valor
        else:
            print("Senha inválida")


cli = Cliente("João", "1111111111", "123")
cb = ContaBancaria(200, cli)

print("Saldo:R$ %.2f " % cb.get_saldo("123"))

cb.depositar(200, "123")
print("Saldo:R$ %.2f " % cb.get_saldo("123"))
cb.sacar(50, "123")
print("Saldo:R$ %.2f " % cb.get_saldo("123"))

'''
SENHA INVÁLIDA
'''

cb.depositar(200, "122")
print("Saldo:R$ %.2f " % cb.get_saldo("123"))
cb.sacar(50, "111")
print("Saldo:R$ %.2f " % cb.get_saldo("123"))
