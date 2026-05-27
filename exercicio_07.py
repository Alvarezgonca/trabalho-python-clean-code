from abc import ABC, abstractmethod


class RegraDeDesconto(ABC):
    @abstractmethod
    def calcular(self, valor):
        pass


class DescontoComum(RegraDeDesconto):
    def calcular(self, valor):
        return valor * 0.05


class DescontoVip(RegraDeDesconto):
    def calcular(self, valor):
        return valor * 0.10


class DescontoPremium(RegraDeDesconto):
    def calcular(self, valor):
        return valor * 0.15


class CalculadoraDeDesconto:
    def calcular(self, regra, valor):
        return regra.calcular(valor)


if __name__ == "__main__":
    calc = CalculadoraDeDesconto()
    print(f"Comum:   R$ {calc.calcular(DescontoComum(), 200):.2f}")
    print(f"Vip:     R$ {calc.calcular(DescontoVip(), 200):.2f}")
    print(f"Premium: R$ {calc.calcular(DescontoPremium(), 200):.2f}")
