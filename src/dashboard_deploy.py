""" Este script es la versión deploy del dashboard, lee directo de la API en lugar de SQLite """

#Librerias utilizadas
import streamlit as st
import requests
import pandas as pd
from datetime import datetime

try:
    #Llamado de API
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


    #Columnas y metricas 
    col_1, col_2, col_3, col_4 = st.columns(4)
    col_5, col_6, col_7 = st.columns(3)
    col_1.metric("Oficial", p_oficial)
    col_2.metric("Blue", p_blue)
    col_3.metric("Bolsa", p_bolsa)
    col_4.metric("Cripto", p_cripto)
    col_5.metric("Mayorista", p_mayorista)
    col_6.metric("Contado con Liqui", p_ccl)
    col_7.metric("Tarjeta", p_tarjeta)

    #Para que la tabla no arranque en 0
    df.index += 1
    #Renombre de la tabla por uno mas estetico
    df = df.rename(columns={'fechaActualizacion': 'Ultima actualizacion'})
    #Conversion de la tabla y estilo de fecha
    df['Ultima actualizacion'] = pd.to_datetime(df['Ultima actualizacion']).dt.strftime('%Y-%m-%d')

    st.dataframe(df)
except Exception as e:
    st.error(f'Error: {e}, porfavor intentelo nuevamente')

