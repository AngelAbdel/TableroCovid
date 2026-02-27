import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import time

# Cargar datos
df = pd.read_csv("CovidDB.csv")
st.title("Tablero Interactivo COVID-19")


# --- Visualización 1: Mapa coroplético por país ---
fig_map = px.choropleth(
    df,
    locations="country",              # Países reconocidos
    locationmode="country names",     # Le decimos que son nombres de países
    color="cases",                    # Número de casos
    hover_name="region",              # Región interna
    animation_frame="date",           # Evolución temporal
    color_continuous_scale="Blues",   # Escala de color
    scope="world",                    # Mostrar el mapa mundial completo
    labels={"country": "País", "cases": "Casos"},
    title="Mapa coroplético de casos por país"
)
st.plotly_chart(fig_map)

# --- Visualización 2: Heatmap temporal ---
# Convertir la columna date a tipo fecha para mejor formato
df["date"] = pd.to_datetime(df["date"])

# Agrupar casos por fecha
df_heat = df.groupby("date")["cases"].sum().reset_index()

# Crear heatmap
fig_heat = px.density_heatmap(
    df_heat,
    x="date",
    y="cases",
    nbinsx=30,
    nbinsy=20,
    color_continuous_scale="YlOrRd",  # escala más clara (amarillo → rojo)
    labels={"date": "Fecha", "cases": "Casos confirmados"},
    title="Mapa de calor temporal de contagios"
)

# Ajustes visuales
fig_heat.update_layout(
    xaxis_title="Fecha",
    yaxis_title="Casos confirmados",
    xaxis=dict(
        tickformat="%b %Y",   # mostrar mes y año en el eje X
        tickangle=45          # inclinar etiquetas para que no se encimen
    ),
    font=dict(size=12),       # tamaño de fuente más legible
    margin=dict(l=40, r=40, t=60, b=40)  # márgenes más equilibrados
)

# Mostrar valores dentro de las celdas
fig_heat.update_traces(
    texttemplate="%{z}",
    textfont_size=12,
    colorbar=dict(title="Frecuencia")
)

st.plotly_chart(fig_heat)

# --- Visualización 3: Bubble chart ---
# Agrupar por edad para reducir saturación
df_bubble = df.groupby("age")[["cases", "deaths"]].sum().reset_index()

fig_bubble = px.scatter(
    df_bubble,
    x="cases",
    y="deaths",
    size="cases",
    color="age",
    size_max=40,  # limitar tamaño máximo de burbujas
    labels={"cases": "Casos", "deaths": "Muertes", "age": "Edad"},
    title="Casos vs Muertes por Grupo de Edad",
    color_continuous_scale="Viridis"
)

fig_bubble.update_traces(
    hovertemplate="Edad: %{marker.color}<br>Casos: %{x}<br>Muertes: %{y}"
)

fig_bubble.update_layout(
    xaxis_title="Casos",
    yaxis_title="Muertes",
    font=dict(size=12),
    margin=dict(l=40, r=40, t=60, b=40)
)

st.plotly_chart(fig_bubble)

# --- Visualización 4: Monitoreo en tiempo real ---
st.header("Monitoreo en tiempo real")

# Inicializar dataset en sesión
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Tiempo", "Casos"])

# Generar un nuevo dato simulado
nuevo_dato = {
    "Tiempo": pd.Timestamp.now(),
    "Casos": np.random.randint(1000, 5000)  # valor aleatorio simulado
}
st.session_state.data = pd.concat([st.session_state.data, pd.DataFrame([nuevo_dato])])

# Mostrar KPI
st.metric("Casos actuales", nuevo_dato["Casos"])

# Mostrar gráfico de serie de tiempo
st.line_chart(st.session_state.data.set_index("Tiempo"))

# Refrescar cada 5 segundos
st.experimental_autorefresh(interval=5000, limit=None, key="refresh")