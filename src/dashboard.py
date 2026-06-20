""" Versión local del dashboard, lee de SQLite y muestra tabla, métricas y gráfico histórico """

# Librerias utilizadas 
import streamlit as st
import sqlite3
import pandas as pd


con = None
try:
    #Conexion a la database
    con = sqlite3.connect("data/dolar.db")
    
    
    #Carga de datos
    df = pd.read_sql(
                """SELECT * FROM dolar_datos""",con
                )


    #Limpieza de datos  
    df['timestamp_registro'] = pd.to_datetime(df['timestamp_registro'])
    df['fecha'] = df['timestamp_registro'].dt.date
    ultimo_por_dia = df.groupby(['fecha','casa'])['timestamp_registro'].max()
    ultimo_por_dia = ultimo_por_dia.reset_index()
    df_limpio = df.merge(ultimo_por_dia, on=['fecha','casa','timestamp_registro'])
    df_pivot = df_limpio.pivot(index='fecha',columns='casa',values='venta')
    
    
    #Dashboard 
    fecha_reciente = df_limpio['fecha'].max()
    fecha_antigua = df_limpio['fecha'].min()
    st.title("Argentina Dolar Tracker")
    st.write(f'Data from {fecha_antigua} to {fecha_reciente}')
    st.subheader("Raw Data")
    st.dataframe(df_limpio[['casa','compra','venta','fecha']])
    st.subheader("Price Evolution")


    #Creacion columnas y metricas
    df_hoy = df_limpio[df_limpio['fecha']== fecha_reciente]
    p_oficial = df_hoy[df_hoy['casa'] == 'oficial']['venta'].values[0]
    p_blue = df_hoy[df_hoy['casa'] == 'blue']['venta'].values[0]
    p_bolsa = df_hoy[df_hoy['casa'] == 'bolsa']['venta'].values[0]
    p_cripto = df_hoy[df_hoy['casa'] == 'cripto']['venta'].values[0]
    p_mayorista = df_hoy[df_hoy['casa'] == 'mayorista']['venta'].values[0]
    p_ccl = df_hoy[df_hoy['casa'] == 'contadoconliqui']['venta'].values[0]
    p_tarjeta = df_hoy[df_hoy['casa'] == 'tarjeta']['venta'].values[0]
    col_1, col_2, col_3, col_4 = st.columns(4)
    col_5, col_6, col_7 = st.columns(3)
    col_1.metric("Oficial", p_oficial)
    col_2.metric("Blue", p_blue)
    col_3.metric("Bolsa", p_bolsa)
    col_4.metric("Cripto", p_cripto)
    col_5.metric("Mayorista", p_mayorista)
    col_6.metric("Contado con Liqui", p_ccl)
    col_7.metric("Tarjeta", p_tarjeta)


    st.subheader("Historical Chart")
    st.line_chart(df_pivot)
except Exception as e:
    st.error(f'Error: {e}, por favor intentelo nuevamente')
finally:
    if con:
        con.close()