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

# Seleciona somente as colunas necessárias
rel_compras = rel_compras.iloc[:, [0, 1, 2, 3]]
rel_compras.columns = ["Cod_Produto", "Descricao", "Unid", "Estoque"]

# Remove linhas onde o código está vazio ou NaN
rel_compras = rel_compras[rel_compras['Cod_Produto'].notna()]
rel_compras = rel_compras[rel_compras['Cod_Produto'].astype(str).str.strip() != '']

# Remove linhas totalmente vazias
rel_compras = rel_compras.dropna(how='all')

# Remove aspas, sinais de igual e espaços extras
rel_compras['Estoque'] = rel_compras['Estoque'].astype(str)
rel_compras['Estoque'] = rel_compras['Estoque'].str.strip()
rel_compras['Estoque'] = rel_compras['Estoque'].str.replace('="', '', regex=False)
rel_compras['Estoque'] = rel_compras['Estoque'].str.replace('"', '', regex=False)

# Remove linhas que não contém numeros no 'Estoque'
rel_compras = rel_compras[rel_compras['Estoque'].str.match(r'^[0-9.,]+$', na=False)]

# Printa as primeiras informações do arquivo 
print("Arquivo selecionado: ", caminho_arquivo)
print(rel_compras.head())

# Exporta o arquivo como csv
rel_compras.to_csv('estoque_bruto.csv', index=False, encoding="utf-8")