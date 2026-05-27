from abc import ABC, abstractmethod


class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class ItemPedido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def subtotal(self):
        return self.produto.preco * self.quantidade


class RegraDeDesconto(ABC):
    @abstractmethod
    def calcular(self, subtotal):
        pass


class SemDesconto(RegraDeDesconto):
    def calcular(self, subtotal):
        return 0


class DescontoPercentual(RegraDeDesconto):
    def __init__(self, percentual):
        self.percentual = percentual

    def calcular(self, subtotal):
        return subtotal * self.percentual


class FormaDePagamento(ABC):
    @abstractmethod
    def pagar(self, valor):
        pass


class PagamentoPix(FormaDePagamento):
    def pagar(self, valor):
        print(f"Pagamento via Pix: R$ {valor:.2f}")


class PagamentoCartao(FormaDePagamento):
    def pagar(self, valor):
        print(f"Pagamento no cartão: R$ {valor:.2f}")


class Notificador(ABC):
    @abstractmethod
    def notificar(self, cliente, mensagem):
        pass


class NotificadorEmail(Notificador):
    def notificar(self, cliente, mensagem):
        print(f"E-mail para {cliente.email}: {mensagem}")


class NotificadorWhatsApp(Notificador):
    def notificar(self, cliente, mensagem):
        print(f"WhatsApp para {cliente.nome}: {mensagem}")


class Pedido:
    def __init__(self, cliente, regra_desconto, forma_pagamento, notificador):
        self.cliente = cliente
        self.itens = []
        self.regra_desconto = regra_desconto
        self.forma_pagamento = forma_pagamento
        self.notificador = notificador

    def adicionar_item(self, produto, quantidade):
        self.itens.append(ItemPedido(produto, quantidade))

    def calcular_subtotal(self):
        return sum(item.subtotal() for item in self.itens)

    def calcular_total(self):
        subtotal = self.calcular_subtotal()
        return subtotal - self.regra_desconto.calcular(subtotal)

    def finalizar(self):
        total = self.calcular_total()
        self.forma_pagamento.pagar(total)
        self.notificador.notificar(
            self.cliente,
            f"Pedido finalizado. Total: R$ {total:.2f}"
        )


if __name__ == "__main__":
    cliente = Cliente("Eduardo", "eduardo@email.com")
    pedido = Pedido(
        cliente=cliente,
        regra_desconto=DescontoPercentual(0.10),
        forma_pagamento=PagamentoPix(),
        notificador=NotificadorEmail(),
    )
    pedido.adicionar_item(Produto("Teclado", 200.00), 1)
    pedido.adicionar_item(Produto("Mouse", 80.00), 2)

    print(f"Subtotal: R$ {pedido.calcular_subtotal():.2f}")
    print(f"Total com desconto: R$ {pedido.calcular_total():.2f}")
    pedido.finalizar()

# Aplicação dos princípios SOLID:
# SRP: cada classe tem uma única responsabilidade (Cliente, Produto, ItemPedido,
#      Pedido, regras de desconto, formas de pagamento e notificadores são separados).
# OCP: novas regras de desconto, formas de pagamento ou notificadores podem ser
#      adicionadas criando novas classes, sem alterar Pedido.
# LSP: qualquer subclasse de RegraDeDesconto, FormaDePagamento ou Notificador
#      pode ser usada no lugar da abstração sem quebrar o Pedido.
# ISP: as interfaces Notificador, FormaDePagamento e RegraDeDesconto são pequenas
#      e específicas, evitando obrigar classes a implementar métodos desnecessários.
# DIP: Pedido depende das abstrações (RegraDeDesconto, FormaDePagamento, Notificador),
#      e não de implementações concretas — elas são injetadas via construtor.
