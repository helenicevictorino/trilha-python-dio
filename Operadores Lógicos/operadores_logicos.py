# Operadores logicos
'''
São operadores utilizados em conjunto com os operadores de comparação, para montar uma 
expressão logica. Quando um operador de comparação é utilizado, o resultado retornado é um booleano, dessa forma podemos combinar operadores de comparação com os operadores lógicos. 
Exemplo:

op_compracao + op_logico + op_comparacao... N...

Exemplo

saldo = 1000
saque = 200
limite = 100

saldo >= saque
>>> True

saque <= limite
>>> False
'''
# Operador AND (todas as condições precisam ser verdadeiras)
'''
saldo = 1000
saque = 200
limite = 100

saldo >= saque and saque <= limite
>>> False
'''
# Operador OR (pelo menos uma condição precisa ser verdadeira)
'''
saldo = 1000
saque = 200
limite = 100

saldo >= saque or saque <= limite
>>> True
'''
# Operador negação
'''
contatos_emergencia = []

not 1000 > 1500
>>> True

not contatos_emergencia
>>> True

not "saque 1500;"
>>> False

not ""
>>> True
'''
# Parenteses
'''
saldo = 1000
saque = 200
limite = 100
conta_especial = True

saldo >= saque and saque <= limite or conta_especial and saldo >= saque
>>> True

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
>>> True
'''

print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False and False)

saldo = 1000
saque = 200
limite = 100
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque

print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

print(exp_2)

conta_normal_com_saldo_suficiente = (saldo >= saque and saque <= limite) 
conta_especial_com_saldo_suficiente = (conta_especial and saldo >= saque)

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)