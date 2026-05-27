import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

from sympy import symbols
from sympy import sympify
from sympy import lambdify

from metodos import *

# CONFIGURACIÓN GENERAL

st.set_page_config(
    page_title="Métodos Numéricos",
    page_icon="📘",
    layout="centered"
)

# TÍTULO Y DESCRIPCIÓN

st.title("📘 Métodos Numéricos")
st.subheader("Integración Numérica")

st.info(
    "Use funciones como: x**2, sin(x), cos(x), exp(x), sqrt(x)"
)

# =========================
# VARIABLE SIMBÓLICA
# =========================

x = symbols('x')

# =========================
# ENTRADAS
# =========================

funcion = st.text_input(
    "Ingrese la función",
    "x**2"
)

a = st.number_input(
    "Límite inferior (a)",
    value=0.0
)

b = st.number_input(
    "Límite superior (b)",
    value=5.0
)

n = st.number_input(
    "Número de particiones (n)",
    value=4,
    step=1
)

# =========================
# MÉTODOS
# =========================

metodo = st.selectbox(
    "Seleccione el método",
    [
        "Trapecio",
        "Simpson 1/3",
        "Simpson 3/8",
        "Boole"
    ]
)


# =========================
# BOTÓN RESOLVER
# =========================

if st.button("Resolver"):

    try:

        # Convertir texto a expresión matemática
        expr = sympify(funcion)

        # Convertir a función numérica
        f = lambdify(x, expr, "numpy")


        # =========================
        # VALIDACIONES
        # =========================

        if a >= b:
            st.error("El límite inferior debe ser menor que el superior.")
            st.stop()

        if metodo == "Trapecio" and n <= 0:
            st.error("n debe ser mayor que 0.")
            st.stop()

        if metodo == "Simpson 1/3" and n % 2 != 0:
            st.error("Simpson 1/3 requiere un número PAR de intervalos.")
            st.stop()

        if metodo == "Simpson 3/8" and n % 3 != 0:
            st.error("Simpson 3/8 requiere múltiplos de 3.")
            st.stop()

        if metodo == "Boole" and n % 4 != 0:
            st.error("Boole requiere múltiplos de 4.")
            st.stop()


        # =========================
        # CÁLCULOS
        # =========================

        if metodo == "Trapecio":

            resultado = trapecio(
                f,
                a,
                b,
                int(n)
            )

        elif metodo == "Simpson 1/3":

            resultado = simpson_13(
                f,
                a,
                b
            )

        elif metodo == "Simpson 3/8":

            resultado = simpson_38(
                f,
                a,
                b
            )

        elif metodo == "Boole":

            resultado = boole(
                f,
                a,
                b
            )


        # =========================
        # RESULTADO
        # =========================

        st.success(
            f"Resultado aproximado: {resultado}"
        )


        # =========================
        # TABLA DE VALORES
        # =========================

        st.subheader("Tabla de valores")

        xs_tabla = np.linspace(a, b, int(n) + 1)
        ys_tabla = f(xs_tabla)

        datos = {
            "x": xs_tabla,
            "f(x)": ys_tabla
        }

        st.dataframe(datos)


        # =========================
        # GRÁFICA
        # =========================

        st.subheader("Gráfica")

        xs = np.linspace(a, b, 400)
        ys = f(xs)

        fig, ax = plt.subplots(figsize=(8, 5))

        ax.plot(xs, ys)

        ax.fill_between(
            xs,
            ys,
            alpha=0.3
        )

        ax.scatter(
            xs_tabla,
            ys_tabla
        )

        ax.set_title("Gráfica de la función")
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.grid(True)

        st.pyplot(fig)


    except Exception as e:

        st.error(
            f"Error en la función o en los datos ingresados: {e}"
        )