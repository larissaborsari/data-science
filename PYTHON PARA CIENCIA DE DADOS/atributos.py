from mailbox import NotEmptyError


class Estudante:
    escola = "DIO" #atributo

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)



aluno_1 = Estudante("ana", 12345)
aluno_2 = Estudante("maria", 54321)


mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "Python"
aluno_3 = Estudante("bruno", 34789)

aluno_1.matricula = 32145

mostrar_valores(aluno_1, aluno_2, aluno_3)
