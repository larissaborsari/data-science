#entendendo propriedades

class Foo:
    def __init__(self, x = None):
        self._x = x

    @property
    def x(self):
        return self._x or 0
    
    @x.setter
    def x(self, value):
        self._x += value
   
    @x.deleter
    def x(self):
        self._x = -1


foo = Foo(10)
print(foo.x)
foo.x = 10
print(foo.x)

del foo.x
print(foo.x)

#exemplo 2

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento
    
    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        _ano_atual = 2022
        return _ano_atual - self._ano_nascimento


pessoa = Pessoa("Larissa", 1998)
print(f" Nome: {pessoa.nome}, idade: {pessoa.idade}")
