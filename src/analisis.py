# Bibliotecas utilizadas 
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

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


    #Grafico
    df_pivot.plot()
    plt.title('Evolucion del Dolar por Tipo de Cambio(junio 2026)')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
except Exception as e:
    print(f'Error: {e}, porfavor intentelo nuevamente')
finally:
    if con:
        con.close()