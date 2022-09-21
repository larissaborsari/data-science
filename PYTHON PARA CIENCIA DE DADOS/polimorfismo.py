#função com comportamentos diferentes para diferentes tipos de dados

class Passaro:
    def voar(self):
        print("Voando ...")
    
class Pardal(Passaro):
    def voar(self):
        super().voar()
    
class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa!") #até aqui é herança
    

def plano_voo(especie): #aqui aplica o polimorfismo
    especie.voar()


p1 = Pardal()
p2 = Avestruz()

plano_voo(p1)
plano_voo(p2)
