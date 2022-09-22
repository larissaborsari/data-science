#abstract base class
#quando utilizo a classe abstrata sou obrigado a implementar os métodos da
#classe pai nas classes filhas, todos eles.

from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Liganto a TV...")
    def desligar(self):
        print("Desligando a TV...")
    @property
    def marca(self):
        print("LG")

controle = ControleTV()

controle.ligar()
controle.desligar()

print(controle.marca)

