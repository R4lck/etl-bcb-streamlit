# 📊 Monitor Econômico Brasil (ETL & Dashboard)

## Descrição do Projeto
Este projeto é um pipeline de dados automatizado que coleta indicadores econômicos brasileiros (Selic, IPCA e Dólar) diretamente da API do Banco Central do Brasil (SGS). Os dados são transformados, 
armazenados em um banco de dados PostgreSQL na nuvem e exibidos em um painel interativo (Dashboard).

---

## 🏗️ Estrutura do Projeto
```text
projeto_etl_bcb/
├── .github/workflows/
│   └── etl_pipeline.yml     # Automação diária (GitHub Actions)
├── streamlit_app/
│   └── app.py               # Dashboard de visualização
├── main.py                  # Script de ETL (Extração, Transformação e Carga)
├── .env                     # Variáveis de ambiente (Segredos)
├── .gitignore               # Arquivos ignorados pelo Git
└── requirements.txt         # Dependências do projeto
