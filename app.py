import streamlit as st
import pandas as pd
import plotly.express as px


# Cargar dataset
df = pd.read_csv("covid_dataset.csv")

# Título del tablero
st.title("Proyecto Final - Tablero Interactivo de COVID-19")

# Introducción breve
st.markdown("""
Este tablero permite analizar la evolución de la pandemia de COVID-19
por país, región y grupo poblacional. Se pueden explorar contagios,
defunciones, recuperaciones y saturación hospitalaria.
""")

# Filtro por país
countries = df["country"].unique()
selected_country = st.selectbox("Selecciona un país:", countries)

# Filtrar datos por país
filtered_df = df[df["country"] == selected_country]

# Gráfico de casos en el tiempo
fig_cases = px.line(filtered_df, x="date", y="cases",
                    title=f"Casos confirmados en {selected_country}")
st.plotly_chart(fig_cases)

# Gráfico de defunciones vs recuperados
fig_outcomes = px.bar(filtered_df, x="date", y=["deaths", "recovered"],
                      title=f"Defunciones y Recuperados en {selected_country}")
st.plotly_chart(fig_outcomes)

# Distribución por edad
fig_age = px.histogram(filtered_df, x="age", nbins=20,
                       title=f"Distribución de edades en {selected_country}")
st.plotly_chart(fig_age)

# Ocupación hospitalaria
fig_beds = px.line(filtered_df, x="date", y="beds_occupied",
                   title=f"Ocupación hospitalaria en {selected_country}")
st.plotly_chart(fig_beds)

# Comparación por regiones dentro del país
fig_region = px.box(filtered_df, x="region", y="cases",
                    title=f"Casos por región en {selected_country}")
st.plotly_chart(fig_region)