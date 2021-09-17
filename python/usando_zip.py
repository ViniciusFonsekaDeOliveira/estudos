"""
Zip em Python
Verificando a melhor nota de cada aluno ao longo de um semestre.

"""
from random import random

prova1 = [nota for nota in [round(random() * 10, 2) for _ in range(10)]]
prova2 = [nota for nota in [round(random() * 10, 2) for _ in range(10)]]
prova3 = [nota for nota in [round(random() * 10, 2) for _ in range(10)]]

alunos = [i for i in range(1, 11)]

print(prova1)
print(prova2)
print(prova3)
print(alunos)

# jeito 1
melhor_nota_de_cada_aluno_1 = dict(zip(alunos, [max(notas) for notas in list(zip(prova1, prova2, prova3))]))

# jeito 2 - usando map e expressão lambda.
melhor_nota_de_cada_aluno_2 = dict(zip(alunos, map(lambda notas: max(notas), list(zip(prova1, prova2, prova3)))))

print(melhor_nota_de_cada_aluno_1)
print(melhor_nota_de_cada_aluno_2)
