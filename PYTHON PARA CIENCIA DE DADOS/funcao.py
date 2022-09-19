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


def exibir_poema(data_extenso, *args, **kwargs): #args -> asterisco denota a tupla, sempre os valores separados pela vírgula, kwargs -> dois astericos denotam estrutura chave valor
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)


exibir_poema("Segunda-feira, 19/09/2022", "Zen do Python", "Beautiful is better than uggly", autor="Tim Peters", ano="1999",)
