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

# Limpa aspas e sinais de "=" nos nomes das colunas
data_frame.columns = data_frame.columns.str.replace('="', '', regex=False).str.replace('"', '', regex=False).str.strip()

# Limpa valores de texto
for col in df.select_dtypes(include=['object', 'string']).columns:
    data_frame[col] = data_frame[col].str.replace('="', '', regex=False).str.replace('"', '', regex=False).str.strip()

print("Arquivo Selecionado: ", caminho_arquivo)
print(data_frame.head())
