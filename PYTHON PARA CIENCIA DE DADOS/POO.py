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

b1 = Bicicleta("vermelha", "caloi", 2022, 650)
b1.buzinar()
b1.correr()
b1.parar()