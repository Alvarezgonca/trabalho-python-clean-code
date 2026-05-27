from abc import ABC, abstractmethod


class Ligavel(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass


class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self, documento):
        pass


class Escaneavel(ABC):
    @abstractmethod
    def escanear(self, documento):
        pass


class ImpressoraMultifuncional(Ligavel, Imprimivel, Escaneavel):
    def ligar(self):
        print("Impressora ligada")

    def desligar(self):
        print("Impressora desligada")

    def imprimir(self, documento):
        print(f"Imprimindo: {documento}")

    def escanear(self, documento):
        print(f"Escaneando: {documento}")


class Lampada(Ligavel):
    def ligar(self):
        print("Lâmpada acesa")

    def desligar(self):
        print("Lâmpada apagada")


if __name__ == "__main__":
    impressora = ImpressoraMultifuncional()
    impressora.ligar()
    impressora.imprimir("Relatório.pdf")
    impressora.escanear("Contrato.pdf")
    impressora.desligar()

    lampada = Lampada()
    lampada.ligar()
    lampada.desligar()
