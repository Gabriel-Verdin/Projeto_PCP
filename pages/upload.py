import streamlit as st
import db.salvar_relatorio

uploaded_file = st.file_uploader("Escolha o Relatório: ", type=["xls", "xlsx", "csv"])

if uploaded_file is not None:
    # Seleção de qual tabela salvar
    tabela = st.selectbox(
        "Qual relatório você está importando?",
        ["Compras", "Estoque", "NS", "HOT", "LUCAS"]
    )

    if st.button("Salvar Relatório"):
        funcoes = {
            "Compras": db.salvar_relatorio.db_relatorio_compras,
            "Estoque": db.salvar_relatorio.db_relatorio_estoque,
            "NS": db.salvar_relatorio.db_relatorio_ns,
            "HOT": db.salvar_relatorio.db_relatorio_hot,
            "LUCAS": db.salvar_relatorio.db_relatorio_lucas
        }

        funcao = funcoes[tabela]
        funcao(uploaded_file)

        st.success(f"Relatório '{tabela}' salvo com sucesso!")

        st.text("Pré-Visualização do Relatório:")
        data_frame = db.salvar_relatorio.consulta(tabela)
        st.dataframe(data_frame.head())