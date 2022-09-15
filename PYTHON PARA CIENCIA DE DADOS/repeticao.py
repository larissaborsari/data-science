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

#condicional

MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Insira a sua idade: "))

if idade >= MAIOR_IDADE:
    print("O usuário já pode dar entrada na CNH")

elif idade == IDADE_ESPECIAL:
    print("O usuário pode fazer aulas teóricas, mas não pode fazer aulas práticas")

else:
    print("O usuário ainda não pode dar entrada na CNH")


#repeticao

fruits = ['apple', 'grape', 'papaya', 'orange']

for fruit in fruits:
  print(fruit)


while True: 
    numero = int(input("Informe um número: "))

    if numero == 100:
        break

    print(numero)

    