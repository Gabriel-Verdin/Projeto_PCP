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

data_frame = data_frame.iloc[:, :4]
data_frame.columns = ['Nivel', 'Codigo', 'Descricao', 'Quantidade']

print(data_frame)
data_frame.to_csv('teste.csv', index=False, encoding='utf-8')