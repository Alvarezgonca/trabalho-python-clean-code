from abc import ABC, abstractmethod


class FormaDePagamento(ABC):
    @abstractmethod
    def pagar(self, valor):
        pass


class PagamentoCartao(FormaDePagamento):
    def pagar(self, valor):
        print(f"Pagamento de R$ {valor:.2f} realizado no cartão.")


class PagamentoPix(FormaDePagamento):
    def pagar(self, valor):
        print(f"Pagamento de R$ {valor:.2f} realizado via Pix.")


class PagamentoBoleto(FormaDePagamento):
    def pagar(self, valor):
        print(f"Boleto gerado no valor de R$ {valor:.2f}.")


class ProcessadorDePagamento:
    def processar(self, forma_pagamento, valor):
        forma_pagamento.pagar(valor)


if __name__ == "__main__":
    processador = ProcessadorDePagamento()
    processador.processar(PagamentoCartao(), 150.00)
    processador.processar(PagamentoPix(), 80.00)
    processador.processar(PagamentoBoleto(), 230.00)
