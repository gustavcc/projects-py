meu_dicionario = {1: 'Zeca', 2: 'Maria', 3: 'Ana', 4: 'Carlos'}

# Ordena o dicionário pelos valores (nomes) em ordem alfabética
dicionario_ordenado = {k: v for k, v in sorted(meu_dicionario.items(), key=lambda item: item[1])}

print(dicionario_ordenado)
