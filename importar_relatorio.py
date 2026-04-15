import pandas as pd
import tkinter as tk
from tkinter import filedialog

def importar_relatorio_generico():

    # Abre o explorador de Arquivos para escolha do relatório em específico
    root = tk.Tk()
    root.withdraw()

    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione o Arquivo",
        filetypes=[("Arquivos Excel", "*.xlsx *.xls")]
    )

    try:
        # Tenta ler o arquivo como excel primeiro
        data_frame = pd.read_excel(
            caminho_arquivo, 
            engine="xlrd")
    except:
        # Se der erro, le o arquivo como csv
        data_frame = pd.read_csv(
            caminho_arquivo, sep='\t', 
            encoding='latin1', 
            engine="python", 
            on_bad_lines='skip', 
            skiprows=3)


    print(data_frame.head())

relatorio = importar_relatorio_generico()
print(relatorio)