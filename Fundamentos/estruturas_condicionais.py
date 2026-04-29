'''A estrutura condicional permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendiadas'''

MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe a sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.") 
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer as aulas práticas.")       
else:
    print("Ainda não pode tirar a CNH.")