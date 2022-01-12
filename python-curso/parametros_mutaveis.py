def lista_de_clientes(l1, l2=None):
    if l2 is None:
        l2 = []
    l2.extend(l1)
    l2.sort()
    return l2


cli1 = lista_de_clientes(['Maria', 'Florisberto', 'Capetinga'], ['Damasceno', 'Calango'])
cli2 = lista_de_clientes(['Gustavo', 'Alice', 'Aline'])

print(cli1)
print(cli2)
