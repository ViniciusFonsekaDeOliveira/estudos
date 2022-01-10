from itertools import combinations, permutations, product


"""
Combinação a ordem não importa. p1 e p2, por exemplo, é o mesmo que p2 e p1.
Permutação a ordem importa. p1 e p2 é diferente de p2 e p1.
Produto (Product) - p1 e p2 é diferente de p2 e p1 e há repetição de valores únicos.

"""

pessoas = ["André", "Gustavo", "Aica", "Bianca", "Rasus", "Garen"]

for grupo in combinations(pessoas, 2):
    print(grupo)
