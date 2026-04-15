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
rel_compras = rel_compras.iloc[:, [5, 11, 12, 18]]
rel_compras.columns = ["Fornecedor", "Cod_Produto", "Desc_Produto", "Qtd_pedida"]

# Remove linhas totalmente vazias
rel_compras = rel_compras.dropna(how='all')

# Printa as primeiras informações do arquivo 
print("Arquivo selecionado: ", caminho_arquivo)
print(rel_compras.head())

# Exporta o arquivo como csv
rel_compras.to_csv('estoque_bruto.csv', index=False, encoding="utf-8")