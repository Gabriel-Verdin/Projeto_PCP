import streamlit as st
import pandas as pd
import sqlite3

# Conexão com banco de dados
conexao = sqlite3.connect('meu_banco.db')
cursor = conexao.cursor()

# Cria tabela se não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hc TEXT NOT NULL,
    descricao TEXT NOT NULL,
    media_vendas INTEGER,
    partida INTEGER
)
""")

st.title("Cadastro de Produtos")

# Incicializar lista de produtos na sessão
if "produtos" not in st.session_state:
    st.session_state.produtos = []

hc = st.text_input("Digite o HC do Produto: ")
descricao = st.text_input("Digite a Descrição do Produto: ")
media_vendas = st.number_input("Digite a Média de Vendas: (0 se não possuir)", min_value=0, max_value=100000)
partida = st.number_input("Digite a Partida de Produção: (0 se não possuir)", min_value=0, max_value=100000)

if st.button("Cadastrar Produto"):
    if hc.strip() == "" or descricao.strip() == "":
        st.warning("Insira um cadastro válido! HC e Descrição são obrigatórios.")
    else:
        # Adiciona produto à lista
        st.session_state.produtos.append({
            "HC": hc,
            "Descrição": descricao,
            "Média de Vendas": media_vendas,
            "Partida": partida
        })

# Mostrar tabela com todos os cadastros
if st.session_state.produtos:
    st.subheader("Resumo dos Cadastros")
    df = pd.DataFrame(st.session_state.produtos)
    st.dataframe(df, use_container_width=True)

    if st.button("Salvar Cadastro"):
        cursor.execute(
            "INSERT INTO produtos (hc, descricao, media_vendas, partida) VALUES (?, ?, ?, ?)",
            (hc, descricao, media_vendas, partida)
        )
        conexao.commit()
        st.success("Cadastro salvo com sucesso!")

conexao.close()