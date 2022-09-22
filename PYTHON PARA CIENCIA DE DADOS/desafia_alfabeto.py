letra = input("Insira uma letra de A a Z: ")
letra = letra.upper()

#criando a lista do Alfabeto
alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
"Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

#encontrado a letra digitada na lista
posicao = alfabeto.index(letra)

#definindo o número correspondente
numero = posicao + 1

#exibindo o resultado
print(numero)