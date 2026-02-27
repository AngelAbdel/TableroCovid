import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
df = pd.read_csv("CovidDB.csv")

st.write("Columnas en el dataset:", df.columns)
st.title("Tablero Interactivo COVID-19")

# --- Visualización 1: Mapa geoespacial ---
# Usaremos 'region' como ubicación (si tienes coordenadas, se puede mejorar)
fig_map = px.choropleth(
    df,
    locations="region",
    color="cases",
    hover_name="country",
    animation_frame="date",
    title="Mapa coroplético de casos por región"
)
st.plotly_chart(fig_map)

# --- Visualización 2: Heatmap temporal ---
df_heat = df.groupby("date")["cases"].sum().reset_index()
fig_heat = px.density_heatmap(
    df_heat,
    x="date",
    y="cases",
    nbinsx=30,
    nbinsy=20,
    title="Mapa de calor temporal de contagios"
)
st.plotly_chart(fig_heat)

# --- Visualización 3: Bubble chart ---
fig_bubble = px.scatter(
    df,
    x="cases",
    y="deaths",
    size="cases",
    color="age",
    hover_name="region",
    title="Casos vs muertes por grupo de edad"
)
st.plotly_chart(fig_bubble)