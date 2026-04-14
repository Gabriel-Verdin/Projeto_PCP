import pandas as pd
import tkinter as tk 
from tkinter import filedialog

# data_frame = relatorio_estoque

# Abre o explorador de arquivos
root = tk.Tk()
root.withdraw()

caminho_arquivo = filedialog.askopenfilename(
    title="Selecione o Arquivo Excel",
    filetypes=[("Arquivos Excel", "*.xlsx *.xls")]
)

# Lê o arquivo usando ';' como separador
data_frame = pd.read_csv(caminho_arquivo, sep='\t', encoding='latin1', skiprows=3)

# Remove linhas totalmente vazias
data_frame = data_frame.dropna(axis=1, how='all')

# Renomeia as colunas para os nomes corretos
data_frame = data_frame.rename(columns={
    data_frame.columns[0]: 'Codigo',
    data_frame.columns[1]: 'Descricao',
    data_frame.columns[2]: 'Unid',
    data_frame.columns[3]: 'Estoque'
})

# Mantém só colunas principais
data_frame = data_frame[['Codigo', 'Descricao', 'Unid', 'Estoque']]

# Limpa valores de texto
for col in data_frame.select_dtypes(include=['object', 'string']).columns:
    data_frame[col] = data_frame[col].str.replace('="', '', regex=False).str.replace('"', '', regex=False).str.strip()

# Remove linhas que não contém numeros no 'Estoque'
data_frame = data_frame[data_frame['Estoque'].str.match(r'^[0-9.,]+$', na=False)]

# Converte 'Estoque' para float
data_frame['Estoque'] = (
    data_frame['Estoque']
    .str.replace('.', '', regex=False) # Remove separador de milhar
    .str.replace(',', '.', regex=False) # Troca virgula por ponto
    .astype(float)
)

print("Arquivo Selecionado: ", caminho_arquivo)
print(data_frame.head())

data_frame.to_csv('estoque_bruto.csv', index=False, encoding="utf-8")