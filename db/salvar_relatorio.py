import src.importar_relatorio as importar_relatorio
import sqlite3
import pandas as pd

# Fução de Importação do Relatório para o Banco de Dados
def db_relatorio_compras(conexao):
    relatorio_compras = importar_relatorio.importar_relatorio_generico()
    relatorio_compras.to_sql("relatorio_compras", conexao, if_exists="replace", index=False)

def db_relatorio_estoque(conexao):
    relatorio_estoque = importar_relatorio.importar_relatorio_generico()
    relatorio_estoque.to_sql("relatorio_estoque", conexao, if_exists="replace", index=False)

def db_relatorio_ns(conexao):
    relatorio_ns = importar_relatorio.importar_relatorio_generico()
    relatorio_ns.to_sql("relatorio_ns", conexao, if_exists="replace", index=False)

def db_relatorio_hot(conexao):
    relatorio_hot = importar_relatorio.importar_relatorio_generico()
    relatorio_hot.to_sql("relatorio_hot", conexao, if_exists="replace", index=False)

def db_relatorio_lucas(conexao):
    relatorio_lucas = importar_relatorio.importar_relatorio_generico()
    relatorio_lucas.to_sql("relatorio_lucas", conexao, if_exists="replace", index=False)

# Conexão com o Banco de Dados
conexao = sqlite3.connect('meu_banco.db')
cursor = conexao.cursor()

# Chamada da Função
db_relatorio_ns(conexao)

# Consulta do Banco de Dados
def consulta():
    conexao = sqlite3.connect('meu_banco.db')
    data_frame = pd.read_sql_query("SELECT * FROM relatorio_ns", conexao)
    conexao.close()
    return data_frame

# Fechamento da Conexão
conexao.commit()
conexao.close()