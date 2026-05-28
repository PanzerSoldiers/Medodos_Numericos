# App.py


import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

from sympy import symbols
from sympy import sympify
from sympy import lambdify

from metodos import *

# =========================================
# CONFIGURACIÓN GENERAL
# =========================================

st.set_page_config(
    page_title="Métodos Numéricos",
    page_icon="📘",
    layout="wide"
)

# =========================================
# CARGAR CSS
# =========================================

with open("style.css", encoding="utf-8") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# =========================================
# SIDEBAR
# =========================================

with st.sidebar:

    st.image(
        "Fondo_Sidebar.jpg",
        use_container_width=True
    )

    st.markdown("## 📘 Métodos Numéricos")

    st.markdown("---")

    st.markdown("### Tecnologías")

    st.markdown("- Python")
    st.markdown("- Streamlit")
    st.markdown("- NumPy")
    st.markdown("- SymPy")
    st.markdown("- Matplotlib")

    st.markdown("---")

    st.markdown("### Métodos Disponibles")

    st.markdown("✅ Trapecio")
    st.markdown("✅ Simpson 1/3")
    st.markdown("✅ Simpson 3/8")
    st.markdown("✅ Boole")

# =========================================
# HEADER PRINCIPAL
# =========================================

st.markdown(
    """
    <div class="titulo-principal">
        <h1>📘 Calculadora de Métodos Numéricos</h1>
        <p>
            Plataforma interactiva para resolver integraciones numéricas
            mediante métodos avanzados.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.latex(r"\int_a^b f(x)\,dx")

st.info(
    "Use funciones como: x**2, sin(x), cos(x), exp(x), sqrt(x)"
)

# =========================================
# VARIABLE SIMBÓLICA
# =========================================

x = symbols('x')

# =========================================
# ENTRADAS
# =========================================

col1, col2 = st.columns(2)

with col1:

    funcion = st.text_input(
        "Ingrese la función",
        "x**2"
    )

    a = st.number_input(
        "Límite inferior (a)",
        value=0.0
    )

with col2:

    b = st.number_input(
        "Límite superior (b)",
        value=5.0
    )

    n = st.number_input(
        "Número de particiones (n)",
        value=4,
        step=1
    )

# =========================================
# MÉTODOS
# =========================================

metodo = st.selectbox(
    "Seleccione el método",
    [
        "Trapecio",
        "Simpson 1/3",
        "Simpson 3/8",
        "Boole"
    ]
)

# =========================================
# FÓRMULAS
# =========================================

if metodo == "Trapecio":

    st.latex(
        r"\int_a^b f(x)dx \approx \frac{h}{2}[f(x_0)+2f(x_1)+f(x_n)]"
    )

elif metodo == "Simpson 1/3":

    st.latex(
        r"\int_a^b f(x)dx \approx \frac{h}{3}[f(x_0)+4f(x_1)+f(x_2)]"
    )

elif metodo == "Simpson 3/8":

    st.latex(
        r"\int_a^b f(x)dx \approx \frac{3h}{8}[f(x_0)+3f(x_1)+3f(x_2)+f(x_3)]"
    )

elif metodo == "Boole":

    st.latex(
        r"\int_a^b f(x)dx \approx \frac{2h}{45}[7f(x_0)+32f(x_1)+12f(x_2)+32f(x_3)+7f(x_4)]"
    )

# =========================================
# BOTÓN
# =========================================

if st.button("🚀 Resolver"):

    try:

        expr = sympify(funcion)

        f = lambdify(x, expr, "numpy")

        # =========================================
        # VALIDACIONES
        # =========================================

        if a >= b:
            st.error("El límite inferior debe ser menor que el superior.")
            st.stop()

        if metodo == "Trapecio" and n <= 0:
            st.error("n debe ser mayor que 0.")
            st.stop()

        if metodo == "Simpson 1/3" and n % 2 != 0:
            st.error("Simpson 1/3 requiere un número PAR.")
            st.stop()

        if metodo == "Simpson 3/8" and n % 3 != 0:
            st.error("Simpson 3/8 requiere múltiplos de 3.")
            st.stop()

        if metodo == "Boole" and n % 4 != 0:
            st.error("Boole requiere múltiplos de 4.")
            st.stop()

        # =========================================
        # CÁLCULOS
        # =========================================

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

        # =========================================
        # RESULTADO
        # =========================================

        st.success(
            f"Resultado aproximado: {resultado}"
        )

        col1, col2, col3 = st.columns(3)

        col1.metric("Método", metodo)
        col2.metric("Intervalos", int(n))
        col3.metric("Resultado", round(resultado, 6))

        # =========================================
        # TABLA
        # =========================================

        st.subheader("📋 Tabla de valores")

        xs_tabla = np.linspace(a, b, int(n) + 1)

        ys_tabla = f(xs_tabla)

        datos = {
            "x": xs_tabla,
            "f(x)": ys_tabla
        }

        st.dataframe(
            datos,
            use_container_width=True
        )

        # =========================================
        # GRÁFICA
        # =========================================

        st.subheader("📈 Gráfica")

        xs = np.linspace(a, b, 400)

        ys = f(xs)

        fig, ax = plt.subplots(figsize=(10, 5))

        fig.patch.set_facecolor('#0F172A')

        ax.set_facecolor('#111827')

        ax.plot(
            xs,
            ys,
            linewidth=3
        )

        ax.fill_between(
            xs,
            ys,
            alpha=0.3
        )

        ax.scatter(
            xs_tabla,
            ys_tabla
        )

        ax.set_title(
            "Gráfica de la función",
            color="white"
        )

        ax.set_xlabel(
            "x",
            color="white"
        )

        ax.set_ylabel(
            "f(x)",
            color="white"
        )

        ax.tick_params(colors='white')

        ax.grid(
            True,
            linestyle="--",
            alpha=0.4
        )

        st.pyplot(fig)

    except Exception as e:

        st.error(
            f"Error en la función o datos ingresados: {e}"
        )

