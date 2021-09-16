"""

Sintaxe: [ dado for dado in colecao_de_dados_qualquer ]

Entendimento: " Para cada dado em minha coleção de dados qualquer, crie uma lista considerando este dado,
processando-o como você bem entender."

Uma forma eficiente de processar dados de uma lista

Existem variações também com dicionário e conjuntos. {}

"""

dicionario = {'a': 1,
              'b': 2,
              'c': 3,
              'd': 4}


# se for par, eleve ao quadrado. Caso contrário, diminua uma unidade.
novo = {chave: (valor ** 2 if not valor % 2 else valor - 1) for chave, valor in dicionario.items()}

print(dicionario)
print(novo)
