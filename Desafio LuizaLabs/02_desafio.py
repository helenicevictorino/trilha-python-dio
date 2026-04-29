# Lê a linha de entrada e separa os produtos em uma lista
produtos = input().strip().split()

# TODO: Crie uma estrutura para contar quantas vezes cada produto aparece na lista

# Dica: Use um laço para percorrer a lista e atualizar a contagem de cada produto

# Inicialize variáveis para armazenar o produto mais frequente e sua contagem
mais_frequente = None
maior_contagem = -1

# Percorra a lista original para garantir o critério de desempate (primeira ocorrência)
for produto in produtos:
    # TODO: Obtenha a contagem do produto atual e atualize mais_frequente se necessário
    pass  # Substitua pelo código que compara e atualiza o produto mais frequente

for produto in produtos:
    contagem_atual = produtos.count(produto)
    if contagem_atual > maior_contagem:
        maior_contagem = contagem_atual
        mais_frequente = produto

# Imprima o produto mais frequente
print(mais_frequente)