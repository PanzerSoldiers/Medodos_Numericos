import numpy as np


# =========================
# MÉTODO DEL TRAPECIO
# =========================
def trapecio(f, a, b, n):

    h = (b - a) / n

    x = np.linspace(a, b, n + 1)

    suma = f(x[0]) + f(x[n])

    for i in range(1, n):
        suma += 2 * f(x[i])

    return (h / 2) * suma


# =========================
# MÉTODO SIMPSON 1/3
# =========================
def simpson_13(f, a, b):

    h = (b - a) / 2

    x0 = a
    x1 = a + h
    x2 = b

    resultado = (h / 3) * (
        f(x0) +
        4 * f(x1) +
        f(x2)
    )

    return resultado


# =========================
# MÉTODO SIMPSON 3/8
# =========================
def simpson_38(f, a, b):

    h = (b - a) / 3

    x0 = a
    x1 = a + h
    x2 = a + (2 * h)
    x3 = b

    resultado = (3 * h / 8) * (
        f(x0) +
        3 * f(x1) +
        3 * f(x2) +
        f(x3)
    )

    return resultado


# =========================
# MÉTODO DE BOOLE
# =========================
def boole(f, a, b):

    h = (b - a) / 4

    x0 = a
    x1 = a + h
    x2 = a + (2 * h)
    x3 = a + (3 * h)
    x4 = b

    resultado = (2 * h / 45) * (
        7 * f(x0) +
        32 * f(x1) +
        12 * f(x2) +
        32 * f(x3) +
        7 * f(x4)
    )

    return resultado