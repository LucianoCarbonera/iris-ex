import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClaissifier

st.write("# Classificação de Iris")
st.write("## Exemplo com comprimentos de pétala e sépala")

st.sidebar.write("### Parâmetros")
st.sidebar.slider("Comprimento de sépala", 4.0, 8.0, 5.8, 0.1)
st.sidebar.slider("Comprimento de pétala", 0.9, 7.0, 3.8, 0.1)

with open("objetos.pkl", "rb") as arquivo:
  ss, dtc = pickle.load(arquivo)
