import streamlit as st
import pandas as pd
import plotly.express as px

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
fig_heat.update_traces(texttemplate="%{z}", textfont_size=10)
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