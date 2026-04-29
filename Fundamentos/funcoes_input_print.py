# input
'''
Usada para ler dados da entrada padrão (teclado).
Ela recebe um argumento do tipo string, que é exibido para o usuario na saída padrão (tela).
A função le a entrada, converte para string e retorna o valor.

Exemplo

nome = input("Informe o seu nome: ")
>>> Informe o seu nome: |
'''
# print
'''
É utilizada para exibir dados na saída padrão (tela). Ela recebe um argumento obrigatório  do tipo varargs de objetos e 4 argumentos opcionais (sep, end, file e flush).
Todos os objetos sao convertidos para string, separados por sep e terminados por end. A string final é exibiada para o usuário.

Exemplo

nome = "Guilherme"
sobrenome = "Carvalho"

print(nome, sobrenome)
print(nome, sobrenome, end="...\n")
print(nome, sobrenome, sep="#")

>>> Guilherme Carvalho
>>> Guilherme Carvalho...
>>> Guilherme#Carvalho
'''

nome = input("Informe o seu nome: ")
idade = input("Informe a sua idade: ")

print(nome, idade)
print(nome, idade, end="...\n")
print(nome, idade, sep="#", end="...\n")
print(nome, idade, sep="#")