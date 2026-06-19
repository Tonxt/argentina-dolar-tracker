import streamlit as st
import requests
import pandas as pd
from datetime import datetime

response = requests.get("https://dolarapi.com/v1/dolares")
response = response.json()
df = pd.DataFrame(response)


st.title("Argentina Dolar Tracker")
st.write(f'Date: {datetime.today().strftime('%Y-%m-%d')}')


st.dataframe(df)

