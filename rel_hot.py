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

# Lê o arquivo utilizando '\t' como separador e pula as linhas 'sujas'
df = pd.read_csv(
    caminho_arquivo,
    sep='\t',
    encoding='latin1',
    engine='python',
    on_bad_lines='skip'
)

# Se vier mais de 4 colunas, selecione só as primeiras 4
df = df.iloc[:, :4]
df.columns = ['Codigo', 'Descricao', 'Unid', 'Estoque']

# Limpa valores de texto
for col in df.select_dtypes(include=['object', 'string']).columns:
    df[col] = df[col].str.replace('="', '', regex=False).str.replace('"', '', regex=False).str.strip()

# Remove linhas que não contém numeros no 'Estoque'
df = df[df['Estoque'].str.match(r'^[0-9.,]+$', na=False)]

# Converte 'Estoque' para float
df['Estoque'] = (
    df['Estoque']
    .str.replace('.', '', regex=False) # Remove separador de milhar
    .str.replace(',', '.', regex=False) # Troca virgula por ponto
    .astype(float)
)

print(df.head())

# Exporta o arquivo como csv
df.to_csv('estoque_bruto.csv', index=False, encoding="utf-8")

