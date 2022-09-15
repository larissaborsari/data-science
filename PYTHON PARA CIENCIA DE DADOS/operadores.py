#ARITMETICOS

produto_1 = 10
produto_2 = 20

print("adição ", produto_1 + produto_2)
print("subtração ", produto_1 - produto_2)
print("multiplicação ", produto_1 * produto_2)
print("divisão ", produto_1 / produto_2)
print("inteiro ", produto_1 // produto_2)
print("módulo ", produto_1 % produto_2)
print("potência ", produto_1 ** produto_2)

#COMPARAÇÃO

saldo = 200
saque = 200 

print(saldo == saque)
print(saldo != saque)
print(saldo > saque)
print(saldo >= saque)
print(saldo <= saque)
print(saldo < saque)

#ATRIBUIÇÃO

saldo_2 = 500
print(saldo_2)

saldo_2 += 200
print(saldo_2)

saldo_2 -= 200
print(saldo_2)

saldo_2 *= 2
print(saldo_2)

saldo_2 /= 2
print(saldo_2)

saldo_2 **= 2
print(saldo_2)

#LOGICOS

print( True and True)
print(True and False)
print(True or True)
print(True or False)
print(False or False)
print(False and False)

saldo_3 = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo_3 >= saque and saque <= limite or conta_especial and saldo_3 >= saque

print(exp)

exp = (saldo_3 >= saque and saque <= limite) or (conta_especial and saldo_3 >= saque)

print(exp)


#IDENTIDADE

