class Animal: 
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__ (self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs):
        self.cor_pelo = cor_pelo
        super().__init__(**kwargs)


class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ave(Animal):
    def __init__(self, tipo_bico, **kwargs):
        self.tipo_bico = tipo_bico
        super().__init__(**kwargs)

    

class Ornitorrinco(Mamifero, Ave):
    pass


# gato = Gato(4, "preto")
# print(gato)

ornito = Ornitorrinco(nro_patas=4, cor_pelo="cinza", tipo_bico="coreaceo")
print(ornito)