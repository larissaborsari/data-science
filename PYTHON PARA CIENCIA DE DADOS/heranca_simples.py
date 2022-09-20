class Veiculo:
    def __init__ (self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor ... ")

class Motocicleta(Veiculo):
    pass

class Caminhao(Veiculo):
    pass

class Carro(Veiculo):
    pass

moto = Motocicleta("azul", "AB45DC4", 2)
moto.ligar_motor()


carro = Carro("Preto", "we4532", 4)
carro.ligar_motor()


caminhao = Caminhao("vermelho", "qwe345f", 8)
caminhao.ligar_motor()
