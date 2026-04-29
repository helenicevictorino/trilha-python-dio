# Leitura da entrada: preço e código de promoção
entrada = input().strip()
preco_str, codigo_promocao = entrada.split()

# Conversão do preço para float
preco = float(preco_str)

# TODO: Se o produto estiver em promoção ("S"), aplique 10% de desconto ao preço.
# Caso contrário, mantenha o preço original.
# Dica: Use uma estrutura condicional para decidir qual valor atribuir à variável preco_final.

preco_final = preco * 0.90 if codigo_promocao == "S" else preco

# preco_final = ...

# Exibe o valor final com duas casas decimais
print(f"{preco_final:.2f}")


