# =====================================================
# =============== Ainda não finalizado ================
# =====================================================

import pandas as pd
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

caminho_arquivo = filedialog.askopenfilename(
   title="Selecione o Arquivo",
    filetypes=[("Arquivos Excel", "*.xlsx *.xls")]
)

data_frame = pd.read_csv(caminho_arquivo, sep='\t', encoding='latin1', engine='python')

# Remove linhas totalmente vazias
data_frame = data_frame.dropna(how='all')

data_frame = data_frame[~data_frame.iloc[:,0].astype(str).str.contains(". N.o de Itens", na=False)]

# Mantem as 4 primeiras colunas
data_frame = data_frame.iloc[:, :4]
data_frame.columns = ['Nivel', 'Codigo', 'Descricao', 'Quantidade']

# Limpeza das colunas
for coluna in ['Nivel', 'Codigo', 'Descricao']:
    data_frame[coluna] = (
        data_frame[coluna]
        .astype(str)
        .str.replace('="', '', regex=False)
        .str.replace('"', '', regex=False)
        .str.replace('[ ', '', regex=False)
        .str.replace('[', '', regex=False)
        .str.replace(']', '', regex=False)
        .str.strip()
    )

# Ajuste da coluna quantidade
data_frame['Quantidade'] = (
    data_frame['Quantidade']
    .astype(str)
    .str.replace('.', '', regex=False)
    .str.replace(',', '.', regex=False)
    .str.strip()
    .astype(float)
)

print(data_frame)
data_frame.to_csv('teste.csv', index=False, encoding='utf-8')