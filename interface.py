import streamlit as st
import db.salvar_relatorio

st.title("Relatorios do MRP")
st.dataframe(db.salvar_relatorio.consulta())