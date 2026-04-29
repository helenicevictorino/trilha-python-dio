# Old style %

nome = "Helenice"
idade = 36
profissao = "Programadora"
linguagem = "Python"
saldo = 45.238

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho com %s e estou matriculada no curso de %s." % (nome, idade, profissao, linguagem))

# Método format

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculada no curso de {}.".format(nome, idade, profissao, linguagem))

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculada no curso de {0}.".format(linguagem, profissao, idade, nome))

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculada no curso de {linguagem}.".format(nome= nome, idade= idade, profissao= profissao, linguagem= linguagem))

# f-string

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculada no curso de {linguagem}.")

# Olá, me chamo Helenice. Eu tenho 36 anos de idade, trabalho com Programadora e estou matriculada no curso de Python.

# Formatar strings com f-string

PI = 3.14159

print (f"Valor de PI: {PI:.2f}")
# Valor de PI: 3.14

print(f"Valor de PI: {PI:10.2f}")
# Valor de PI:       3.14

print("Nome: %s Idade: %d" % (nome, idade))
print("Nome: {} Idade: {}".format (nome, idade))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format (idade, nome))
print("Nome: {nome} Idade: {idade}".format (nome= nome, idade= idade))
print("Nome: {nome} Idade: {idade} {nome} {nome} {idade}".format (nome= nome, idade= idade))
# Nome: Helenice Idade: 36

dados = {"nome": "Helenice", "idade": 36}

print("Nome: {nome} Idade: {idade}".format(**dados))
print(f"Nome: {nome} Idade: {idade}")
# Nome: Helenice Idade: 36

print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
# Nome: Helenice Idade: 36 Saldo: 45.24