# pour créer une application web interactive en Python
import streamlit as st

# pour manipuler des données structurées au format json
import json

# pour l'analyse et la visualisation
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


# Affichage de l'application en plein écran
st.set_page_config(page_title="Assur’Aimant", page_icon="logo.jpeg", layout="centered")

# Ajouter un titre et un logo à la page web
import streamlit as st

# Add the background image
st.markdown("""
<style>
body {
  background-image: url("logo.jpeg");
}
</style>
""", unsafe_allow_html=True)

# Add the title
st.markdown("""
<h1 style="text-align: center; padding-top: 20px; color: white">Assur'Aimant</h1>
""", unsafe_allow_html=True)



