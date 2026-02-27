import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
df = pd.read_csv("CovidDB.csv")

st.title("Tablero Interactivo COVID-19")

# --- Visualización 1: Mapa geoespacial ---
st.subheader("Mapa geoespacial de casos")
# Supongamos que tu dataset tiene columnas: 'lat', 'lon', 'casos'
fig_map = px.scatter_mapbox(
    df,
    lat="lat",
    lon="lon",
    size="casos",
    color="casos",
    hover_name="municipio",
    mapbox_style="carto-positron",
    zoom=4,
    title="Distribución geográfica de casos"
)
st.plotly_chart(fig_map)

# --- Visualización 2: Heatmap temporal ---
st.subheader("Mapa de calor temporal")
# Supongamos que tienes columnas: 'fecha' y 'casos'
df_heat = df.groupby("fecha")["casos"].sum().reset_index()
fig_heat = px.density_heatmap(
    df_heat,
    x="fecha",
    y="casos",
    nbinsx=30,
    nbinsy=20,
    title="Patrones temporales de contagios"
)
st.plotly_chart(fig_heat)

# --- Visualización 3: Bubble chart ---
st.subheader("Gráfico de burbujas")
# Supongamos que tienes columnas: 'grupo_edad', 'casos', 'muertes'
fig_bubble = px.scatter(
    df,
    x="casos",
    y="muertes",
    size="casos",
    color="grupo_edad",
    hover_name="grupo_edad",
    title="Relación entre casos, muertes y grupos de edad"
)
st.plotly_chart(fig_bubble)