import sqlite3
con = None

try:
    con = sqlite3.connect("data/dolar.db")
    print('=== TIMESTAMPS REGISTRADOS ===')
    resultado = con.execute("""SELECT DISTINCT timestamp_registro FROM dolar_datos""")
    for fila in resultado:
        print(fila)
    print('=== TODOS LOS REGISTROS ===')
    resultado_total = con.execute("""SELECT * FROM dolar_datos""")
    for dato in resultado_total:
        print(dato)
except Exception as e:
    print(f'Error: {e}, porfavor intentelo nuevamente')
finally:
    if con:
        con.close()

