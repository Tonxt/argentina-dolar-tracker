import requests
import sqlite3
from datetime import datetime

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
con.close()
            




