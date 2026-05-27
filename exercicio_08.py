from abc import ABC, abstractmethod
from math import pi


class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass


class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura


class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2


class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return pi * self.raio ** 2


def calcular_areas(formas):
    for forma in formas:
        print(f"{type(forma).__name__}: {forma.calcular_area():.2f}")


if __name__ == "__main__":
    calcular_areas([Retangulo(4, 5), Quadrado(3), Circulo(2)])
