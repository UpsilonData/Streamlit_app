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
    tab1_1.html("<h4>Guide de gestion des Environnements Python avec vend</h4>")
    tab1_1.html("Ce guide vous permettra <span style='color:red;'> test </span>...")

    tab1_2.html("Quelle commande est utilisée pour créer un environnement virtuel avec ")


tab2.write("this is tab 2")
tab3.write("this is tab 3")
tab4.write("this is tab 4")
