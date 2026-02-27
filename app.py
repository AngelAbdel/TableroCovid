import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
df = pd.read_csv("CovidDB.csv")

st.title("Tablero Interactivo COVID-19")
st.write("Columnas en el dataset:", df.columns)

# --- Visualización 1: Mapa coroplético ---
fig_map = px.choropleth(
    df,
    locations="region",              # Región o país
    color="cases",                   # Número de casos
    hover_name="country",            # Nombre del país
    animation_frame="date",          # Evolución temporal
    color_continuous_scale="Blues",  # Escala de color más clara
    labels={"region": "Región", "cases": "Casos"},
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
    color_continuous_scale="Reds",
    labels={"date": "Fecha", "cases": "Casos confirmados"},
    title="Mapa de calor temporal de contagios"
)
fig_heat.update_traces(texttemplate="%{z}", textfont_size=10)  # Mostrar valores
st.plotly_chart(fig_heat)

# --- Visualización 3: Bubble chart ---
fig_bubble = px.scatter(
    df,
    x="cases",
    y="deaths",
    size="cases",
    color="age",
    hover_name="region",
    labels={"cases": "Casos", "deaths": "Muertes", "age": "Edad"},
    title="Casos vs Muertes por Grupo de Edad"
)
fig_bubble.update_traces(
    hovertemplate="Región: %{hovertext}<br>Edad: %{marker.color}<br>Casos: %{x}<br>Muertes: %{y}"
)
st.plotly_chart(fig_bubble)