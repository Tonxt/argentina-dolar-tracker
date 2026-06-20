""" Llama a la API, transforma los datos, los guarda en SQLite con timestamp """

#Librerias utilizadas
import requests
import sqlite3
from datetime import datetime
con = None

try:
    #Llamado de la API y conexion a la database
    response = requests.get("https://dolarapi.com/v1/dolares")
    data = response.json()
    con = sqlite3.connect("data/dolar.db")
    timestamp = datetime.now()

    con.execute("""
        
        CREATE TABLE IF NOT EXISTS dolar_datos(
            casa TEXT,
            compra REAL,
            venta REAL,
            fecha TEXT,
            timestamp_registro TEXT
            )
        """)

    for elemento in data:
        print(elemento['casa'], elemento['compra'], elemento['venta'], elemento['fechaActualizacion'])
        con.execute("INSERT INTO dolar_datos VALUES(?, ?, ?, ?, ?)" ,(elemento['casa'],elemento['compra'],elemento['venta'],elemento['fechaActualizacion'], str(timestamp)))
        
    con.commit()
    print(f'\nSe guardaron {len(data)} registros a las {timestamp}')
except Exception as e:
    print(f'Error: {e}, porfavor intentelo nuevamente.')
finally:
    if con:
        con.close()
