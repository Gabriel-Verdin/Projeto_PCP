import importar_relatorio
import sqlite3

relatorio = importar_relatorio.importar_relatorio_generico()

conexao = sqlite3.connect('meu_banco.db')
cursor = conexao.cursor()

relatorio.to_sql("relatorio_compras", conexao, if_exists="replace", index=False)

cursor.execute("SELECT * FROM relatorio_compras")
for linha in cursor.fetchall():
    print(linha)

conexao.commit()
conexao.close()