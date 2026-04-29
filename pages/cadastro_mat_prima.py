import streamlit as st
import pandas as pd
import sqlite3

conexao = sqlite3.connect('meu_banco.db')
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS materia_prima (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo TEXT NOT NULL,
    descricao TEXT NOT NULL,
    unidade_medida TEXT NOT NULL,
    fornecedor TEXT NOT NULL,
    compra_minima INTEGER,
    lead_time INTEGER
)
""")

st.title("Cadastro de Matéria Prima")

if "materia_prima" not in st.session_state:
    st.session_state.materia_prima = []

codigo = st.text_input("Digite o código do produto: ")
descricao = st.text_input("Digite a descrição do produto: ")
unidade_medida = st.text_input("Digite a unidade de medida: ")
fornecedor = st.text_input("Digite o fornecedor: ")
compra_minima = st.number_input("Digite a compra mínima: (0 se não possuir)", min_value=0, max_value=100000)
lead_time = st.number_input("Digite o lead time do fornecedor: (Em dias)", min_value=0, max_value=100000)

if st.button("Cadastrar Matéria Prima"):
    if codigo.strip() == "" or descricao.strip() == "" or unidade_medida == "" or fornecedor == "":
        st.warning("Insira um cadastro válido! Existem campos obrigatórios vazios.")
    else:
        st.session_state.materia_prima.append({
            "Código": codigo,
            "Descrição": descricao,
            "Unidade de Medida": unidade_medida,
            "Fornecedor": fornecedor,
            "Compra Mínima": compra_minima,
            "Lead Time": lead_time 
        }) 

if st.session_state.materia_prima:
    st.subheader("Resumo dos Cadastros")
    df = pd.DataFrame(st.session_state.materia_prima)
    st.dataframe(df, width="stretch")

    if st.button("Salvar Cadastro"):
        cursor.execute(
            "INSERT INTO materia_prima (codigo, descricao, unidade_medida, fornecedor, compra_minima, lead_time) VALUES (?, ?, ?, ?, ?, ?)",
            (codigo, descricao, unidade_medida, fornecedor, compra_minima, lead_time)
        )
        conexao.commit()
        st.success("Cadastro salvo com sucesso!")

conexao.close()