import streamlit as st
import pandas as pd
import plotly.express as px   # ✅ Import correcto

# Cargar datos
df = pd.read_csv("CovidDB.csv")

st.write("Columnas en el dataset:", df.columns)
st.title("Tablero Interactivo COVID-19")

# --- Visualización 1: Mapa geoespacial ---
fig_map = px.scatter_mapbox(
    df,
    lat="Latitud",
    lon="Longitud",
    size="Casos",
    color="Casos",
    hover_name="Municipio",
    mapbox_style="carto-positron",
    zoom=4,
    title="Distribución geográfica de casos"
)
st.plotly_chart(fig_map)

# --- Visualización 2: Heatmap temporal ---
df_heat = df.groupby("Fecha")["Casos"].sum().reset_index()
fig_heat = px.density_heatmap(
    df_heat,
    x="Fecha",
    y="Casos",
    nbinsx=30,
    nbinsy=20,
    title="Patrones temporales de contagios"
)
st.plotly_chart(fig_heat)

# --- Visualización 3: Bubble chart ---
fig_bubble = px.scatter(
    df,
    x="Casos",
    y="Muertes",
    size="Casos",
    color="GrupoEdad",
    hover_name="GrupoEdad",
    title="Relación entre casos, muertes y grupos de edad"
)
st.plotly_chart(fig_bubble)