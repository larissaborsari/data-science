contatos = {"guilherme@gmail.com" : {"nome": "Guilherme", "telefone": "3345-0000"},
"maria@gmail.com" : {"nome" : "Maria", "telefone" : "3345-1111"},
"bruna@gmail.com" : {"nome" : "Bruno", "telefone" : "3345-2222"},
"jose@gmail.com" : {"nome" : "José", "telefone" : "3345-3333"},
"murilo@gmail.com" : {"nome" : "Murilo", "telefone" : "3345-4444"},
}

telefone = contatos["bruna@gmail.com"]["telefone"]
print(telefone)

for chave, valor in contatos.items():
    print(chave, valor)

resultado = contatos.pop("carlos@gmail.com", "não encontrou")
print(resultado)