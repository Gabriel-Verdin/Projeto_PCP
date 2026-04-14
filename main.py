import pandas as pd
import tkinter as tk 
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

caminho_arquivo = filedialog.askopenfilename(
    title="Selecione o Arquivo Excel",
    filetypes=[("Arquivos Excel", "*.xlsx *.xls")]
)

df = pd.read_csv(caminho_arquivo, sep=';', encoding='latin1', header=None)

print("Arquivo Selecionado: ", caminho_arquivo)
print(df.head())
