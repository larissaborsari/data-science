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


b1 = Bicicleta("vermelha", "caloi", 2022, 650)
