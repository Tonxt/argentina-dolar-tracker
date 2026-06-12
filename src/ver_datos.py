import sqlite3
con = sqlite3.connect("data/dolar.db")

print('=== EXECUTES ===')
resultado = con.execute("""SELECT DISTINCT timestamp_registro FROM dolar_datos""")
for fila in resultado:
    print(fila)
print('=== TODOS LOS REGISTROS ===')
resultado_total = con.execute("""SELECT * FROM dolar_datos""")
for dato in resultado_total:
    print(dato)
con.close()

