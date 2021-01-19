from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, n_conta, nome, saldo):
        self.n_conta = n_conta
        self.nome = nome
        self.saldo = saldo

    @abstractmethod
    def deposito(self, valor):
        return self.saldo + valor

    @abstractmethod
    def saque(self, valor):
        pass

    @abstractmethod
    def imprimir_saldo(self):
        print("Seu saldo é de: R$ %.2f" % self.saldo)


class ContaPoupanca(Conta):
    def __init__(self, n_conta, nome, saldo, aniversario):
        super().__init__(n_conta, nome, saldo)
        self.aniversario = aniversario

    def deposito(self, valor):
        self.saldo += valor
        return self.saldo

    def saque(self, valor):
        if valor > self.saldo:
            print("Transação não pode ser concluida.")
        else:
            self.saldo -= valor
            return self.saldo

    def imprimir_saldo(self):
        print("Seu saldo é de: R$ %.2f" % self.saldo)


class ContaComLimite(Conta):
    def __init__(self, n_conta, nome, saldo, limite):
        super().__init__(n_conta, nome, saldo)
        self.limite = limite

    def deposito(self, valor):
        self.saldo += valor
        return self.saldo

    def saque(self, valor):
        while self.saldo != self.limite:
            self.saldo -= valor
        return self.saldo

    def imprimir_saldo(self):
        print("Seu saldo é de: R$ %.2f" % self.saldo)


class ContaSemLimite(Conta):
    def __init__(self, n_conta, nome, saldo):
        super().__init__(n_conta, nome, saldo)

    def deposito(self, valor):
        self.saldo += valor
        return self.saldo

    def saque(self, valor):
        if valor > self.saldo:
            print("Transação não pode ser concluida.")
        else:
            self.saldo -= valor
            return self.saldo

    def imprimir_saldo(self):
        print("Seu saldo é de: R$ %.2f" % self.saldo)


def separador():
    separador = '=-' * 30
    print(separador)


cp = ContaPoupanca('1234567', "Gabriel", 1500, "30/07/2020")
separador()
print("Conta Poupança:")
separador()
cp.imprimir_saldo()
cp.deposito(50)
cp.imprimir_saldo()
separador()
cp.saque(500)
cp.imprimir_saldo()
separador()
cp.saque(2000)
cp.imprimir_saldo()
separador()

contac_limite = ContaComLimite('246810', "João", 1000, 500)
print("Conta com limite: ")
separador()
contac_limite.imprimir_saldo()
separador()
contac_limite.deposito(50)
contac_limite.imprimir_saldo()
separador()
contac_limite.saque(50)
contac_limite.imprimir_saldo()
separador()

print("Conta sem limite:")
separador()
contacs_limite = ContaSemLimite('1357911', "Pedro", 5000)
contacs_limite.imprimir_saldo()
separador()
contacs_limite.deposito(1000)
contacs_limite.imprimir_saldo()
separador()
contacs_limite.saque(5500)
contacs_limite.imprimir_saldo()
separador()
contacs_limite.saque(501)
contacs_limite.imprimir_saldo()
separador()
