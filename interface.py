import streamlit as st
import db.salvar_relatorio

uploaded_file = st.file_uploader("Escolha o Relatório: ", type=["xls", "xlsx", "csv"])

if uploaded_file is not None:
    db.salvar_relatorio.consulta()