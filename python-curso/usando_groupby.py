from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'B', 'matricula': '19.2.4033'},
    {'nome': 'Pedro', 'nota': 'C', 'matricula': '16.1.1099'},
    {'nome': 'Gustavo', 'nota': 'A', 'matricula': '18.2.4030'},
    {'nome': 'Lucas', 'nota': 'A', 'matricula': '20.2.8000'},
    {'nome': 'Carlos', 'nota': 'C', 'matricula': '19.1.4075'},
    {'nome': 'Joana', 'nota': 'A', 'matricula': '18.1.6060'},
    {'nome': 'Bianca', 'nota': 'B', 'matricula': '19.2.4031'},
    {'nome': 'Alice', 'nota': 'B', 'matricula': '19.1.3920'},
    {'nome': 'Luana', 'nota': 'A', 'matricula': '17.2.6000'},
    {'nome': 'Larissa', 'nota': 'B', 'matricula': '20.1.4503'}
]

ranking_alunos = sorted(alunos, key=lambda item: item['nota'])

alunos_mais_antigos = sorted(alunos, key=lambda item: item['matricula'])

print(f'Melhores alunos: {ranking_alunos}')
print(f'Alunos mais antigos: {alunos_mais_antigos}')


alunos_agrupados = groupby(ranking_alunos, key=lambda item: item['nota'])

print(alunos_agrupados)

for agrupamento, estudantes in alunos_agrupados:
    print(agrupamento)
    # print(estudantes)
    for est in estudantes:
        print(est)
