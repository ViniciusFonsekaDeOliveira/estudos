"""
Zip em Python
Verificando a melhor nota de cada aluno ao longo de um semestre.

"""
from random import random

prova1 = [nota for nota in [round(random()*10, 2) for _ in range(10)]]
prova2 = [nota for nota in [round(random()*10, 2) for _ in range(10)]]
prova3 = [nota for nota in [round(random()*10, 2) for _ in range(10)]]

alunos = [i for i in range(1, 11)]

print(prova1)
print(prova2)
print(prova3)
print(alunos)

melhor_nota_de_cada_aluno = dict(zip(alunos, [max(notas) for notas in list(zip(prova1, prova2, prova3))]))

print(melhor_nota_de_cada_aluno)
