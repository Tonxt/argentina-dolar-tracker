import requests

response = requests.get("https://dolarapi.com/v1/dolares")
data = response.json()
for elemento in data:
    print(elemento['casa'], elemento['compra'], elemento['venta'], elemento['fechaActualizacion'])
