# pour créer une application web interactive en Python
import streamlit as st

# pour manipuler des données structurées au format json
import json

# pour l'analyse et la visualisation
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import pickle

# conversion bmi en catégorie
def convert_bmi_to_cat(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "healthy"
    elif bmi <30:
        return "overweight"
    elif bmi < 40:
        return "obesity"
    else:
        return "morbid_obesity"



st.set_page_config(page_title="Assur’Aimant", page_icon="logo.jpeg", layout="centered")

st.image(image="logo.png")
st.markdown(""" <img src="logo.jpeg" alt="">
<h1 style="text-align: center; padding-top: 20px; color: white">Assur'Aimant</h1>
""", unsafe_allow_html=True)

st.subheader("Estimez une prime d'assurance selon vos critères : ")

pickle_in = open('model_en.pkl','rb')
model_ElasticNet = pickle.load(pickle_in)

columns_model = ['age', 'sex','children', 'smoker', 'region','bmi']

carac_personne = [0 for i in range(6)]

age = st.number_input(label="Age :",min_value=18,step=1, value=18, key="age")
carac_personne[0] = age

sexe = st.radio(
     "Sexe :",
     ('Homme','Femme' ))

if sexe == 'Homme':
    carac_personne[1] = 'male'
elif sexe == 'Femme':
    carac_personne[1] = 'female'

children  = st.number_input(label="Nombre d'enfants : ",value=0, min_value=0, key="children")
carac_personne[2] = children

smoker = st.radio(
     "Fumeur ? :",
     ('Oui','Non' ))

if smoker == 'Oui':
    carac_personne[3] = 'yes'
elif smoker == 'Non':
    carac_personne[3] = 'no'

liste_region= ['northeast', 'southeast', 'southwest', 'northwest']

region = st.selectbox("Region: ", 
                     liste_region)
carac_personne[4] = region

bmi = st.number_input(label="Bmi :",value=20.5,min_value=10.,step=1.,format="%.2f", key="bmi")
carac_personne[5] = convert_bmi_to_cat(bmi)


if(st.button("Valider")):
    
    predic__ElasticNet = int(model_ElasticNet.predict(pd.DataFrame(np.array(carac_personne).reshape(1, -1),columns=columns_model)))

    st.markdown("<h3 style='text-align: center;'>Estimation de la prime d'assurance :</h3>", unsafe_allow_html=True)
    new_title = '<p style="font-family:sans-serif; color:Green;width:100%;text-align:center; font-size: 36px;">{} $</p>'.format(predic__ElasticNet)
    st.markdown(new_title, unsafe_allow_html=True)


