curso = "pYtHoN"

print(curso.lower())
print(curso.upper())
print(curso.title())

word = "  Palavra "

print(word.strip()) #remove os espaços antes e depois
print(word.lstrip()) #remove os espaços antes
print(word.rstrip()) #remove os espaços depois

other_word = "exemplo"

print(other_word.center(15,"#"))
print(".".join(other_word))

#interpolação

nome = "Larissa"
idade = 24
nacionalidade = "brasileira"

dados = {"nome":"Larissa", "idade":24}

print("Olá eu me chamo %s, tenho %d anos de idade e sou %s" %(nome, idade, nacionalidade))
print("Olá eu me chamo {}, tenho {} anos de idade e sou {}" .format (nome, idade, nacionalidade))
print("Olá eu me chamo {nome} e tenho {idade} anos de idade." .format (**dados))

PI = 3.14159

print(f"Valor de PI: {PI : .2f}")
print(f"Valor de PI: {PI : 10.2f}")
