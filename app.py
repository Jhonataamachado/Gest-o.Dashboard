import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard de Leads", layout="wide")

st.title("📊 Painel de Gestão de Leads B2B")
st.markdown("Visualização rápida dos contactos extraídos para a equipa comercial.")

try:
    # Carregar os dados gerados no Projeto 2
    df = pd.read_csv("leads_gerados.csv", sep=";")
    
    # Criar cartões com métricas principais
    total_leads = len(df)
    cidades_unicas = df["Cidade"].nunique()
    
    col1, col2 = st.columns(2)
    col1.metric("Total de Leads Extraídos", total_leads)
    col2.metric("Cidades Alcançadas", cidades_unicas)
    
    # Exibir a tabela de forma interativa
    st.subheader("Base de Contactos")
    st.dataframe(df, use_container_width=True)
    
except FileNotFoundError:
    st.error("Ficheiro 'leads_gerados.csv' não encontrado. Certifique-se de que está na mesma pasta que o ficheiro app.py.")
    