import importar_relatorio
import sqlite3

# Fução de Importação do Relatório para o Banco de Dados
def db_relatorio_compras(conexao):
    relatorio_compras = importar_relatorio.importar_relatorio_generico()
    relatorio_compras.to_sql("relatorio_compras", conexao, if_exists="replace", index=False)

# Conexão com o Banco de Dados
conexao = sqlite3.connect('meu_banco.db')
cursor = conexao.cursor()

# Chamada da Função
db_relatorio_compras(conexao)

# Consulta do Banco de Dados
cursor.execute("SELECT * FROM relatorio_compras")
for linha in cursor.fetchall():
    print(linha)

# Fechamento da Conexão
conexao.commit()
conexao.close()