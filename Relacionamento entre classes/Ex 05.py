class Paciente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade


class Medico:
    def __init__(self, nome, crm, especializacao):
        self.nome = nome
        self.crm = crm
        self.especializacao = especializacao


class Exame:
    def __init__(self, descricao, resultado, medico, paciente):
        self.descricao = descricao
        self.resultado = resultado
        self.medico = medico
        self.paciente = paciente

    def imprimir_resultado(self):
        print("Nome do médico(a)", self.medico.nome)
        print("CRM: ", self.medico.crm)
        print("Especialização", self.medico.especializacao)
        print("Nome do paciente: ", self.paciente.nome)
        print("CPF: ", self.paciente.cpf)
        print("Idade:", self.paciente.idade)
        print("Descrição do exame: ", self.descricao)
        print("Resultado: ", self.resultado)


paciente1 = Paciente("João", "123456789", 18)
medico1 = Medico("Daiana", "123456", "Clinico Geral")
exame1 = Exame("Covid", "Negativo", medico1, paciente1)
exame1.imprimir_resultado()
