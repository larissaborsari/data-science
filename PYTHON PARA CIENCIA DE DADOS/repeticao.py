#indentação

def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")
        print("retire seu dinheiro na boca do caixa")

    print("Obrigado por ser nosso cliente! Tenha um bom dia.")

def depositar(valor):
    saldo = 500
    saldo += valor
    print(saldo)


sacar(100)
depositar(250)
