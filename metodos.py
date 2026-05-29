import numpy as np

# =========================================
# MÉTODO DEL TRAPECIO
# =========================================

def trapecio(f, a, b, n):

    h = (b - a) / n

    x = np.linspace(a, b, n + 1)

    suma = f(x[0]) + f(x[n])

    for i in range(1, n):

        suma += 2 * f(x[i])

    return (h / 2) * suma


# =========================================
# MÉTODO SIMPSON 1/3
# =========================================

def simpson_13(f, a, b, n):

    h = (b - a) / n

    x = np.linspace(a, b, n + 1)

    suma = f(x[0]) + f(x[n])

    for i in range(1, n):

        if i % 2 == 0:

            suma += 2 * f(x[i])

        else:

            suma += 4 * f(x[i])

    return (h / 3) * suma


# =========================================
# MÉTODO SIMPSON 3/8
# =========================================

def simpson_38(f, a, b, n):

    h = (b - a) / n

    x = np.linspace(a, b, n + 1)

    suma = f(x[0]) + f(x[n])

    for i in range(1, n):

        if i % 3 == 0:

            suma += 2 * f(x[i])

        else:

            suma += 3 * f(x[i])

    return (3 * h / 8) * suma


# =========================================
# MÉTODO DE BOOLE
# =========================================

def boole(f, a, b, n):

    h = (b - a) / n

    x = np.linspace(a, b, n + 1)

    suma = 7 * (f(x[0]) + f(x[n]))

    for i in range(1, n):

        if i % 2 != 0:

            suma += 32 * f(x[i])

        elif i % 4 == 0:

            suma += 14 * f(x[i])

        else:

            suma += 12 * f(x[i])

    return (2 * h / 45) * suma