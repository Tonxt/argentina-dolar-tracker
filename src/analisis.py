import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
con = sqlite3.connect("data/dolar.db")

df = pd.read_sql(
    """SELECT * FROM dolar_datos""",con
                 )

df['timestamp_registro'] = pd.to_datetime(df['timestamp_registro'])
df['fecha'] = df['timestamp_registro'].dt.date
ultimo_por_dia = df.groupby(['fecha','casa'])['timestamp_registro'].max()
ultimo_por_dia = ultimo_por_dia.reset_index()
df_limpio = df.merge(ultimo_por_dia, on=['fecha','casa','timestamp_registro'])

df_pivot = df_limpio.pivot(index='fecha',columns='casa',values='venta')
print(df_pivot.plot())
