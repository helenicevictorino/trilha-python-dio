# Maiúscula, minuscula e título

curso1 = "pYtHon"

print(curso1.upper())
# PYTHON

print(curso1.lower())
# python

print(curso1.title())
# Python 

# Eliminando espaços em branco

curso2 = "     Python   "

print(curso2.strip())
# "Python"

print(curso2.lstrip())
# "Python   "

print(curso2.rstrip())
# "     Python"

# Junções e centralização

curso3 = "Python"

print(curso3.center(10, "#"))
# ##Python## >>> 10 caracteres 

print(".".join(curso3))
# P.y.t.h.o.n

nome = "HelEnIce"

print(nome.upper())
# HELENICE

print(nome.lower())
# helenice

print(nome.title())
# Helenice

texto = "    Olá, mundo!        "

print(texto + ".")
#     Olá, mundo!        .

print(texto.strip() + ".")
# Olá, mundo!.

print(texto.lstrip() + ".")
# Olá, mundo!        .

print(texto.rstrip() + ".")
#     Olá, mundo!.

menu = "Python"

print("####" + menu + "####")
# ####Python####
print(menu.center(14))
#     Python      
print(menu.center(20, "#"))
# #######Python#######
print("-".join(menu))
# P-y-t-h-o-n