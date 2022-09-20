from distutils import core
from imp import init_builtin
from importlib.util import module_for_loader
from mimetypes import init


class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim! Plim!")
    
    def parar(self):
        print("Parando bicicleta ...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vruuuummmmmm")

    def __str__ (self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("vermelha", "caloi", 2022, 650)
b1.buzinar()
b1.correr()
b1.parar()

b2 = Bicicleta("verde", "monark", 2000, 180)

print(b1)