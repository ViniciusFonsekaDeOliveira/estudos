def adicionar_tarefa(af, re):
    tarefa = input("Digite a tarefa que deseja adicionar: ")
    af.append(tarefa)


def desfazer(af, re):
    if len(af) == 0:
        print("Nada a desfazer")
        return
    re.append(af.pop())
    return


def refazer(af, re):
    if len(re) == 0:
        print("Nada a refazer")
        return
    af.append(re.pop())
    return


def sair(af, re):
    print('Encerrando o programa.')
    print(f'Bora fazer as tarefas!\n{af}')
    exit(0)


def listar(af, re):
    print(af)


def executar(op, lt, h):
    print(f'Opcao escolhida {op}')
    operacao = acoes.get(op)
    operacao(lt, h)


acoes = {0: adicionar_tarefa,
         1: desfazer,
         2: refazer,
         3: sair}

afazeres = []
refazer = []

while True:
    print('0 - Adicionar tarefa')
    print('1 - Desfazer')
    print('2 - Refazer')
    print('3 - Sair')

    opcao = int(input('Insira uma opcao: '))
    executar(opcao, afazeres, refazer)
    listar(afazeres, refazer)
