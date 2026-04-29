# Variaveis e Constantes
'''
Variaveis

Em linguagens de programação podemos definir valores que podem sofrer
alterações no decorrer da execução do programa.
Esses valores recebem o nome de variaveis, pois eles nascem com um valor e
não necessariamente devem permanecer com o mesmo durante a execução do programa.

Exemplo:

age = 23
name = 'Guilherme'
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')
>>> Meu nome é Guilherme e eu tenho 23 ano(s) de idade.

age, name = (23, 'Guilherme')
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')
>>> Meu nome é Guilherme e eu tenho 23 ano(s) de idade.

Alterando os valores 

age = 23
name = 'Guilherme'
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')
>>> Meu nome é Guilherme e eu tenho 23 ano(s) de idade.

age = 27
name = 'Giovanna'
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')
>>> Meu nome é Giovanna e eu tenho 27 ano(s) de idade.

'''
'''
Constantes

Assim como as variáveis, constagentes são utilizadas para armazenar valores.
Uma constante nasce com um valor e permanece com ele até o final da execução 
do programa, ou seja, o valor é imutável.
'''
# Python não tem constantes
'''
Não existe uma palavra reservada para informar ao interpretador 
que o valor é constante. Em algumas linguagens por exemplo: JAVA e C utilizamos 'final' e 'const', respectivamente para declarar uma constante.
Em Python usamos a convenção que diz ao programador que a variável é uma constante. Para fazer isso, voce deve criar a variável com o nome todo em letras maiusculas:

ABS_PATH = '/home/guilherme/Documents/python_course/'
DEBUG = True
STATES = [
'SP',
'RJ',
'MG',
]
AMOUNT = 30.2
'''

# Boas práticas

'''
>>> O padrão de nomes deve ser snake case.
exemplo_de_nome
usar_underline_para_separar_as_palavras

>>> Escolher nomes sugestivos.
taxa_de_juros
valor_total
valor_produto

>>> Nomes de constantes todo em maiúsculo.
'''

nome = "Guilherme"
idade = 28

nome, idade = "Giovanna", 27 #variavel

print(nome, idade)

limite_saque_diario = 1000 #nome sugestivo

BRAZILIAN_STATES = ["SP", "RJ", "SC", "RS"] #constante
print (BRAZILIAN_STATES)