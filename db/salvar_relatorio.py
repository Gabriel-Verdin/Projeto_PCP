import src.importar_relatorio as importar_relatorio
import sqlite3
import pandas as pd

# Fução de Importação do Relatório para o Banco de Dados
def db_relatorio_compras(uploaded_file):
    relatorio_compras = importar_relatorio.importar_relatorio_generico(uploaded_file)

    if relatorio_compras is not None:
        conexao = sqlite3.connect('meu_banco.db') # Abre a Conexão 
        relatorio_compras.to_sql("compras", conexao, if_exists="replace", index=True)
        conexao.close() # Fecha a Conexão

def db_relatorio_estoque(uploaded_file):
    relatorio_estoque = importar_relatorio.importar_relatorio_generico(uploaded_file)

    if relatorio_estoque is not None:
        conexao = sqlite3.connect('meu_banco.db') # Abre a Conexão
        relatorio_estoque.to_sql("estoque", conexao, if_exists="replace", index=True)
        conexao.close() # Fecha a Conexão

def db_relatorio_ns(uploaded_file):
    relatorio_ns = importar_relatorio.importar_relatorio_generico(uploaded_file)

    if relatorio_ns is not None:
        conexao = sqlite3.connect('meu_banco.db') # Abre a Conexão
        relatorio_ns.to_sql("ns", conexao, if_exists="replace", index=True)
        conexao.close() # Fecha a Conexão

def db_relatorio_hot(uploaded_file):
    relatorio_hot = importar_relatorio.importar_relatorio_generico(uploaded_file)

    if relatorio_hot is not None:
        conexao = sqlite3.connect('meu_banco.db') # Abre a Conexão
        relatorio_hot.to_sql("hot", conexao, if_exists="replace", index=True)
        conexao.close() # Fecha a Conexão

def db_relatorio_lucas(uploaded_file):
    relatorio_lucas = importar_relatorio.importar_relatorio_generico(uploaded_file)

    if relatorio_lucas is not None:
        conexao = sqlite3.connect('meu_banco.db') # Abre a Conexão
        relatorio_lucas.to_sql("lucas", conexao, if_exists="replace", index=True)
        conexao.close() # Fecha a Conexão

# Consulta do Banco de Dados
def consulta(tabela):
    conexao = sqlite3.connect('meu_banco.db')
    data_frame = pd.read_sql_query(f"SELECT * FROM {tabela}", conexao)
    conexao.close()
    return data_frame