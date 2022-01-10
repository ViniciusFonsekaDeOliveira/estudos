lista = [1, 2, 3, 4, 5, 6, 6, 7, 7, 8]

elemento_considerado = [0] * 11
elemento_repetido = [0] * 11

for elemento in lista:
    print(elemento)
    if elemento_considerado[elemento] == 0:
        elemento_considerado[elemento] = 1
    else:
        elemento_repetido[elemento] = 1
        break

print(elemento_repetido)
