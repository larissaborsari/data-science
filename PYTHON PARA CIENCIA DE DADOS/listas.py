# frutas = ["laranja", "maca", "uva", "banana", "manga", "limao", "melancia"]
# print(frutas)
# print(frutas[0])
# print(frutas[4])

# letras = list("python")
# print(letras)

# lista = [1, "Python", [40, 30, 20]]

# l2 = lista.copy()

# print(lista)
# print(l2)

# print(id(l2), id(lista)) #o que faço em l2 não reflete em lista, porque é uma cópia e não a mesma lista

# l2[0] = "Lari"
# print(l2)


# cores = ["vermelho", "azul", "laranja", "verde", "amarelo", "rosa", "cinza", "amarelo", "azul", "preto", "roxo", "branco", "vermelho", "marrom", "verde", "preto"]

# print(cores.count("vermelho"))
# print(cores.count("azul"))
# print(cores.count("laranja"))
# print(cores.count("amarelo"))
# print(cores.count("dourado"))

nomes = ["maria", "marcos", "gabriela"]
print(nomes)

nomes.extend(["cristian", "larissa", "udo"])
print(nomes)

print(nomes.index("marcos"))

nomes.pop()
print(nomes)

nomes.pop(0)
print(nomes)

len(nomes)


