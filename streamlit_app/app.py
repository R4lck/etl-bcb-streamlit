import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()

st.set_page_config(page_title='Dashboard Econômico', layout='wide')
st.title('📊 Monitor Econômico Brasil')

@st.cache_data(ttl=3600)
def load_data():
    db_url = os.getenv('DATABASE_URL')
    engine = create_engine(db_url)
    return pd.read_sql('SELECT * FROM indicadores_economicos', engine)

try:
    df = load_data()
    st.line_chart(df.set_index('data'))
    st.write('Dados brutos:', df.tail())
except Exception as e:
    st.error(f'Erro ao conectar ao banco: {e}')