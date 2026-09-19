import streamlit as st
import matplotlib.pyplot as plt

st.title("Simulación de caudal - Río Cauca")

# Datos de la Tabla 1 - Estación La Virginia, Río Cauca
t = [0, 6, 12, 24, 30, 36]
Q = [1352.67, 1381.84, 1336.39, 1515.47, 1535.2, 1525.68]

# Mostrar la tabla de datos
st.subheader("Tabla 1 - Datos de la estación")
st.table({"Tiempo (horas)": t, "Caudal (m3/s)": Q})

# Selector de intervalo (los 2 botones)
st.subheader("Elige el intervalo")
opcion = st.radio("¿Qué quieres calcular?", ["Primer intervalo (0 a 6 horas)", "Todo el periodo (0 a 36 horas)"])

if opcion == "Primer intervalo (0 a 6 horas)":
    t_ini, t_fin = 0, 6
else:
    t_ini, t_fin = 0, 36

# Calcular el volumen sumando el área de cada segmento recto
def calcular_volumen(t_ini, t_fin):
    total = 0
    for i in range(len(t) - 1):
        if t[i] >= t_ini and t[i+1] <= t_fin:
            dt = t[i+1] - t[i]
            promedio = (Q[i] + Q[i+1]) / 2
            total = total + (promedio * dt * 3600)
    return total

volumen = calcular_volumen(t_ini, t_fin)

# Gráfica
fig, ax = plt.subplots()
ax.plot(t, Q, marker="o", color="orange")
t_sombra = [x for x in t if t_ini <= x <= t_fin]
Q_sombra = [Q[t.index(x)] for x in t_sombra]
ax.fill_between(t_sombra, Q_sombra, min(Q) - 50, color="blue", alpha=0.3)
ax.set_xlabel("Tiempo (horas)")
ax.set_ylabel("Caudal (m3/s)")
st.pyplot(fig)

# Resultado grande
st.subheader("Resultado")
st.metric("Volumen calculado", f"{volumen:,.0f} m3")
