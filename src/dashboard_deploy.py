import streamlit as st
import requests
import pandas as pd
from datetime import datetime

response = requests.get("https://dolarapi.com/v1/dolares")
response = response.json()
df = pd.DataFrame(response)


st.title("Argentina Dolar Tracker")
st.write(f'Date: {datetime.today().strftime('%Y-%m-%d')}')


p_oficial = df[df['casa'] == 'oficial']['venta'].values[0]
p_blue = df[df['casa'] == 'blue']['venta'].values[0]
p_bolsa = df[df['casa'] == 'bolsa']['venta'].values[0]
p_cripto = df[df['casa'] == 'cripto']['venta'].values[0]
p_mayorista = df[df['casa'] == 'mayorista']['venta'].values[0]
p_ccl = df[df['casa'] == 'contadoconliqui']['venta'].values[0]
p_tarjeta = df[df['casa'] == 'tarjeta']['venta'].values[0]

col_1, col_2, col_3, col_4 = st.columns(4)
col_5, col_6, col_7 = st.columns(3)
col_1.metric("Oficial", p_oficial)
col_2.metric("Blue", p_blue)
col_3.metric("Bolsa", p_bolsa)
col_4.metric("Cripto", p_cripto)
col_5.metric("Mayorista", p_mayorista)
col_6.metric("Contado con Liqui", p_ccl)
col_7.metric("Tarjeta", p_tarjeta)

df.index += 1
df = df.rename(columns={'fechaActualizacion': 'Ultima actualizacion'})
df['Ultima actualizacion'] = pd.to_datetime(df['Ultima actualizacion']).dt.strftime('%Y-%m-%d')

st.dataframe(df)

