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

# verifica se todos os indivíduos possuem a letra C
individuos = ["Camile", "carlos", "carlota", "Ciro", "Cintia", "august"]

print(all([nome[0].title() == 'C' for nome in individuos]))

# um interável vazio é interpretado pelo python como sendo False. Mas o all() o interpreta como True.
# entretanto se houver um 0, o all irá entendê-lo como False.


"""
O any é como se fosse a operação or. 
"Existe qualquer elemento que seja verdadeiro aqui?"

O all é como se fosse a operação and.
"Todos os elementos, incluindo o vazio, são verdadeiros?"
"""

generator = (x for x in range(1, 9))
print(all(x for x in range(8)))  # ocupa menos espaço na memória.
""" 
não é uma tupla, é uma expressão geradora. Complexidade de espaço é mais performática do que as outras coleções

"""

pacote = [(1, 2), (3, 4), (5, 6)]

print(*pacote)
print(list(zip(*pacote)))
