print("Coisas interessantes em python!")

graph = {1: [2, 3, 4, 5],
         2: [1, 3, 4, 5]}

print(graph.keys())  # uma lista contendo apenas as chaves
print(graph.values())  # uma lista contendo apenas os valores.
print(graph.items())  # tupla (chave, valor).

print(set(graph.keys()))  # um conjunto das chaves do meu dicionário, se fosse valores, iria dar unhashble type error.
print(len(set(graph.keys())))

conjunto1 = {1, 2, 3, 4, 5, 6, 7, 10, 20, 11}
conjunto2 = {1, 34, 54, 55, 67, 2, 3, 4, 56, 667}

u = conjunto1 | conjunto2
u2 = conjunto1.union(conjunto2)
i = conjunto1 & conjunto2
i2 = conjunto1.intersection(conjunto2)

print(u)
print(i)

from collections import Counter
from collections import namedtuple

lista = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 4, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

print(Counter(lista))

# definição da tupla nomeada.
user = namedtuple("usuario", 'nome idade sexo nacionalidade')

cadastro = user("Vinicius", 30, "masc", "br")

print(cadastro)


def soma(n1, n2):
    return n1 + n2


def subtracao(n1, n2):
    return n1 - n2


def matematica(n1, n2, op=soma):
    """
     Uma função simples que faz operações matemáticas simples. Testando doc strings

    :param n1:
    :param n2:
    :param op:
    :return:
    """
    return op(n1, n2)

print(matematica(1, 4, op=subtracao))

print(matematica.__doc__)