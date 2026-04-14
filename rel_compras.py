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

# Remove linhas totalmente vazias
rel_compras = rel_compras.dropna(axis=1, how='all')

# Printa as primeiras informações do arquivo 
print("Arquivo selecionado: ", caminho_arquivo)
print(rel_compras.head())

# Exporta o arquivo como csv
rel_compras.to_csv('estoque_bruto.csv', index=False, encoding="utf-8")