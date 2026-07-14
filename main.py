import os
import pandas as pd
import logging
from bcb import sgs
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Força o carregamento do .env na pasta raiz
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=dotenv_path)

logging.basicConfig(level=logging.INFO)

def run_etl():
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        logging.error("DATABASE_URL não encontrada.")
        return
    
    engine = create_engine(db_url)
    
    try:
        series = {'selic': 432, 'ipca': 433, 'dolar': 1}
        df = sgs.get(series, start='2020-01-01')
        df = df.reset_index().rename(columns={'Date': 'data'})
        df['data'] = pd.to_datetime(df['data'])
        df = df.ffill()
        
        df.to_sql('indicadores_economicos', engine, if_exists='replace', index=False)
        logging.info("Sucesso!")
    except Exception as e:
        logging.error(f"Erro: {e}")

if __name__ == "__main__":
    run_etl()