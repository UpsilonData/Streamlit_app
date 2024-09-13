import streamlit as st
import pandas as pd
import numpy as np

# Titre de l'application
st.title("Dashboard des Accidents de Voiture V2 formation")


# Insert containers separated into tabs:
tab1, tab2, tab3, tab4  = st.tabs(["Présentation de l'écosystème", "La SciPy Stack", "Librairies de visualisation", "Fichiers volumineux"])

# You can also use "with" notation:
with tab1:
    tab1_1, tab1_2, tab1_3  = tab1.tabs(["Guide", "Quiz sur venv", "Voir les réponses"])
    tab1_1.html("<h1>Guide de gestion des Environnements Python avec vend</h1>")
    tab1_1.write("Ce guide vous permettra...")


tab2.write("this is tab 2")
tab3.write("this is tab 3")
tab4.write("this is tab 4")


'''
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
'''