import pandas as pd
import tkinter as tk 
from tkinter import filedialog

# Abre explorador de arquivos
root = tk.Tk()
root.withdraw()

caminho_arquivo = filedialog.askopenfilename(
    title="Selecione o Relatório de Compras",
    filetypes=[("Arquivos Excel", "*.xlsx *.xls")]
)

# Lê o arquivo usando '\t' como separador
rel_compras = pd.read_excel(caminho_arquivo, engine="xlrd")

# Seleciona somente as colunas desejadas (F, L, M e S) e renomeia para algo mais explicativo
colunas_desejadas = rel_compras.iloc[:, [5, 11, 12, 18]]
colunas_desejadas.columns = ["Fornecedor", "Cod_Produto", "Desc_Produto", "Qtd_pedida"]

# Remove linhas totalmente vazias
colunas_desejadas = colunas_desejadas.dropna(how='all')

# Printa as primeiras informações do arquivo 
print("Arquivo selecionado: ", caminho_arquivo)
print(colunas_desejadas.head())

# Exporta o arquivo como csv
rel_compras.to_csv('estoque_bruto.csv', index=False, encoding="utf-8")