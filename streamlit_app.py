import streamlit as st
import pandas as pd
import numpy as np

# Titre de l'application
st.title("Dashboard des Accidents de Voiture")


# Simuler des données
np.random.seed(0)
dates = pd.date_range('2015-01-01', periods=2000, freq='D')
data = {
    'Date': dates,
    'Accidents': np.random.poisson(2, size=len(dates)),
    'Weather_Condition': np.random.choice(['Clear', 'Rainy', 'Snowy', 'Foggy'], size=len(dates)),
    'Weekend': (dates.weekday >= 5).astype(int)
}
df = pd.DataFrame(data)

# Convertir 'Date' en index datetime
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Ajouter des colonnes pour l'année, le mois, et le jour de la semaine
df['Year'] = df.index.year
df['Month'] = df.index.month
df['Weekday'] = df.index.weekday

print(df.head())

x = df['Year'].unique()

with st.sidebar:
    st.radio("Select one:", [1, 2])
    # Sélectionner l'année
    st.selectbox('Sélectionner l\'année:', x)
