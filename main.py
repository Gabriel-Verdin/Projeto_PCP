import pandas as pd
import tkinter as tk 
from tkinter import filedialog

# Abre o explorador de arquivos
root = tk.Tk()
root.withdraw()

caminho_arquivo = filedialog.askopenfilename(
    title="Selecione o Arquivo Excel",
    filetypes=[("Arquivos Excel", "*.xlsx *.xls")]
)

# Lê o arquivo usando ';' como separador
df = pd.read_csv(caminho_arquivo, sep=';', encoding='latin1', header=None)

print("Arquivo Selecionado: ", caminho_arquivo)
print(df.head())
