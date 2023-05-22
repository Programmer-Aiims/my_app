# streamlit_app.py

import pandas as pd
import streamlit as st

# Read in data from the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def load_data(sheets_url):
    sheet_url = "https://docs.google.com/spreadsheets/d/1shPozJI4zs2HuY9P7MWoQzPj1pmrPy8NnJUQ-aScYY0/edit#gid=0"
    url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
    #csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    #print(csv_url)
    return pd.read_csv(url_1)

#df = load_data(st.secrets["public_gsheets_url"])
df = load_data()
# Print results.
print(df)
