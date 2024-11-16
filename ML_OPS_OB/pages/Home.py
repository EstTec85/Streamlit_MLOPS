import streamlit as st
import Home, Metrics, Predictions  # Importa solo las necesarias
from Metrics import show_metrics
from Predictions import show_predictions

st.sidebar.title("Navegación")
page = st.sidebar.radio("Ir a:", ["Home", "Metrics", "Predictions"])

def show():
    st.title("Bienvenido a la Página Principal")
    st.write("Esta es la página principal.")

if page == "Home":
    Home.show()
elif page == "Metrics":
    show_metrics()
elif page == "Predictions":
    show_predictions()
