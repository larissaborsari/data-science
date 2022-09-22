salario = float(input("Insira seu salário atual: R$ ")) 

if (salario >= 0 and salario <= 600.00):
  novo = salario * 1.17
  reajuste = salario * 0.17
  percentual = "17 %"

elif (salario >= 600.01 and salario <= 900.00):
  novo = salario * 1.13
  reajuste = salario * 0.13
  percentual = "13 %"

elif (salario >= 900.01 and salario <= 1500.00):
  novo = salario * 1.12
  reajuste = salario * 0.12
  percentual = "12 %"

elif (salario >= 1500.01 and salario <= 2000.00):
  novo = salario * 1.10
  reajuste = salario * 0.10
  percentual = "10 %"

else: 
  novo = salario * 1.05
  reajuste = salario * 0.05
  percentual = "5 %"
  
print("Novo salario: {:.2f}" .format(novo))
print("Reajuste ganho: {:.2f}\n" .format(reajuste))
print(f"Em percentual: {percentual}")