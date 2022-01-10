import math

phi = ((math.sqrt(5) + 1) / 2)


def potencia(x, y):
    return x ** y


def logn(n):
    return math.log(n, 10)


def eh_theta_de_logn():
    c1 = 0
    c2 = 0
    k1 = 0
    k2 = 0
    eh_o_grande = False
    eh_omega_grande = False
    eh_theta = False
    for c in range(1, 100):
        for k in range(1, 100):
            if (c * (logn(k)) <= ((math.sqrt(5) / 5) * potencia(phi, k))) and not eh_o_grande:  # é O(g(x))
                c1 = c
                k1 = k
                eh_o_grande = True
            elif c * (logn(k)) >= ((math.sqrt(5) / 5) * potencia(phi, k)) and not eh_omega_grande:  # é Omega(g(x))
                c2 = c
                k2 = k
                eh_omega_grande = True

            if eh_o_grande and eh_omega_grande:
                break

    if eh_o_grande and eh_omega_grande:
        eh_theta = True

    return eh_theta, c1, c2, k1, k2


resposta = eh_theta_de_logn()

print(resposta)


# (True, 1, 4, 1, 2)

print((1 * (logn(2)) <= ((math.sqrt(5) / 5) * potencia(phi, 2))))

print(4 * (logn(2)) >= ((math.sqrt(5) / 5) * potencia(phi, 2)))

"""
Considerando:

f(n) = {[(√5 + 1)/2] ^ n} / √5 => (√5/5) * phi^n
g(n) = log n,
condicao_theta =   C1 * |log n| <= |(√5/5) * phi^n| <= C2 * |log n|

Para demonstrar que f(n) é Theta(g(n)) basta encontrar algum
c1 e c2 que tornam verdadeira condicao_theta, sempre que n >= k.

Assim, condicao_theta é verdadeira para algum
C1 = 1 e C2 = 4, sempre que n >= 2.

"""