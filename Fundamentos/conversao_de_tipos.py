# Convertendo tipos
'''
Em alguns momentos é necessario converter o tipo de uma variavel para manipular de forma diferente. Por exemplo:
Variáveis do tipo string, que armazenam números e precisamos fazer alguma operação matematica com esse valor.
'''

# Inteiro para float
'''
preco = 10
print(preco)
>>> 10

preco = float(preco)
print(preco)
>>> 10.0

preco = 10 / 2
print(preco)
>>> 5.0
'''

# Float para inteiro
'''
preco = 10.30
print(preco)
>>> 10.3

preco = int(preco)
print(preco)
>>> 10

preco = 10
print(preco)
>>> 10

print(preco / 2)
>>> 5.0

print(preco // 2)
>>> 5

preco = 10.50
idade = 28

print(str(preco))
>>> 10.5

print(str(idade))
>>> 28

texto = f"idade {idade} preco {preco}"
print(texto)
>>> idade 28 preco 10.5

preco = "10.50"
idade "28"

print(float(preco))
>>> 10.50

print(int(idade))
>>> 28

preco = "python"
print(float(preco))
>>> Quando o valor da string são caracteres de texto, nao conseguimos converter para float
'''

print(int(1.9))
print(int(1.659854))
print(int("10"))
print(float("10.10"))
print(float(100))
print(str(10.10))

valor = 10
valor_str = str(valor)
print(type(valor))
print(type(valor_str))

print(100 / 2)
print(100 // 2)