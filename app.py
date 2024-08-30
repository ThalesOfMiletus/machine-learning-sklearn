import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pizzas.csv")

modelo = LinearRegression()

x = df[["diametro"]]
y = df[["preco"]]

modelo.fit(x, y)

st.title("Preço de Pizzas")
st.divider()

diametro = st.number_input("Qual o diametro da pizza?", min_value=0.0, value=0.0, step=0.1)

if diametro:
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write(f"O preço previsto da pizza de {diametro}cm é de R${preco_previsto:,.2f}")