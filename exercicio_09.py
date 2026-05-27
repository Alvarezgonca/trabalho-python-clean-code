from abc import ABC, abstractmethod


class Ave(ABC):
    @abstractmethod
    def emitir_som(self):
        pass


class AveVoadora(Ave):
    @abstractmethod
    def voar(self):
        pass


class Pardal(AveVoadora):
    def emitir_som(self):
        print("Piu piu")

    def voar(self):
        print("Pardal voando")


class Pinguim(Ave):
    def emitir_som(self):
        print("Quack pinguim")

    def nadar(self):
        print("Pinguim nadando")


if __name__ == "__main__":
    pardal = Pardal()
    pardal.emitir_som()
    pardal.voar()

    pinguim = Pinguim()
    pinguim.emitir_som()
    pinguim.nadar()
