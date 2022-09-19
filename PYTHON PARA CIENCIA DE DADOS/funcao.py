def exibir_mensagem(nome="Usuário"):
    print(f"Olá, {nome}! Esta função exibe uma mensagem")

exibir_mensagem("Maria") #retorna a variável com o valor que foi passado
exibir_mensagem()  #retorna a variável com o valor padrão

def calcular_total(numeros):
    return sum(numeros)

def antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

print(calcular_total([10, 20, 30, 55]))
print(antecessor_e_sucessor(9))