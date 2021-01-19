class Produto:
    def __init__(self, nome, preco, descricao):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao

    def exibir_descricao(self):
        return "Descrição:", self.descricao


class Mouse(Produto):
    def __init__(self, nome, preco, descricao, tipo):
        super().__init__(nome, preco, descricao)
        self.tipo = tipo

    def exibir_descricao(self):
        super().exibir_descricao()
        return "Tipo:", self.tipo


class Livro(Produto):
    def __init__(self, nome, preco, descricao, autor):
        super().__init__(nome, preco, descricao)
        self.autor = autor

    def exibir_descricao(self):
        super().exibir_descricao()
        return "Autor:", self.autor


m1 = Mouse("Razer", 80.00, "Mouse Razer", "Óptico")
m2 = Mouse("HP", 30.00, "Mouse HP", "Sem fio")
m3 = Mouse("Multilaser", 35.00, "Mouse Multilaser", "Com esfera")
l1 = Livro("Sniper Americano", 60.00, "Drama", "Chris Kyle")
l2 = Livro("Não há dia fácil", 40.00, "Guerra", "Mark Owen")
l3 = Livro("Percy Jackson", 20.00, "Aventura", "Rick Riordan")

carrinho = [m1, m2, m3, l1, l2, l3]
for i in carrinho:
    print(i.exibir_descricao())
