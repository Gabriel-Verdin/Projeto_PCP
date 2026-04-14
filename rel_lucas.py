import pandas as pd
import tkinter as tk 
from tkinter import filedialog

# Abre o explorador de arquivos
root = tk.Tk()
root.withdraw()

caminho_arquivo = filedialog.askopenfilename(
    title="Selecione o Relatório de Estoque",
    filetypes=[("Arquivos Excel", "*.xlsx *.xls")]
)

# Lê o arquivo usando '\t' como separador
rel_estoque = pd.read_csv(caminho_arquivo, sep='\t', encoding='latin1', skiprows=3)

# Remove linhas totalmente vazias
rel_estoque = rel_estoque.dropna(axis=1, how='all')

# Renomeia as colunas para os nomes corretos
rel_estoque = rel_estoque.rename(columns={
    rel_estoque.columns[0]: 'Codigo',
    rel_estoque.columns[1]: 'Descricao',
    rel_estoque.columns[2]: 'Unid',
    rel_estoque.columns[3]: 'Estoque'
})

# Mantém só colunas principais
rel_estoque = rel_estoque[['Codigo', 'Descricao', 'Unid', 'Estoque']]

# Limpa valores de texto
for col in rel_estoque.select_dtypes(include=['object', 'string']).columns:
    rel_estoque[col] = rel_estoque[col].str.replace('="', '', regex=False).str.replace('"', '', regex=False).str.strip()

# Remove linhas que não contém numeros no 'Estoque'
rel_estoque = rel_estoque[rel_estoque['Estoque'].str.match(r'^[0-9.,]+$', na=False)]

# Converte 'Estoque' para float
rel_estoque['Estoque'] = (
    rel_estoque['Estoque']
    .str.replace('.', '', regex=False) # Remove separador de milhar
    .str.replace(',', '.', regex=False) # Troca virgula por ponto
    .astype(float)
)

# Printa os primeiros dados dos arquivos
print("Arquivo Selecionado: ", caminho_arquivo)
print(rel_estoque.head())

# Exporta o arquivo como csv
rel_estoque.to_csv('estoque_bruto.csv', index=False, encoding="utf-8")