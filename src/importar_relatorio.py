import pandas as pd
# import tkinter as tk
# from tkinter import filedialog

def importar_relatorio_generico(uploaded_file):

    if uploaded_file is None:
        return None

    data_frame = pd.read_excel(uploaded_file, engine="xlrd")

    try: # Caso for o Relatório de Compras
        # Seleciona somente as colunas desejadas (F, L, M e S) e renomeia para algo mais explicativo
        data_frame = data_frame.iloc[:, [5, 11, 12, 18]]
        data_frame.columns = ["Fornecedor", "Cod_Produto", "Desc_Produto", "Qtd_pedida"]

        # Limpa valores de texto
        for col in data_frame.select_dtypes(include=['object', 'string']).columns:
            data_frame[col] = data_frame[col].str.replace('[', '', regex=False).str.replace(']', '', regex=False).str.strip()

        # Remove linhas totalmente vazias
        data_frame = data_frame.dropna(how='all')
        
    except: # Caso for outro Relatório
        # Seleciona somente as colunas necessárias
        data_frame = data_frame.iloc[:, [0, 1, 2, 3]]
        data_frame.columns = ["Cod_Produto", "Descricao", "Unid", "Estoque"]

        # Remove linhas onde o código está vazio ou NaN
        data_frame = data_frame[data_frame['Cod_Produto'].notna()]
        data_frame = data_frame[data_frame['Cod_Produto'].astype(str).str.strip() != '']

        # Remove linhas totalmente vazias
        data_frame = data_frame.dropna(how='all')

        # Remove aspas, sinais de igual e espaços extras
        data_frame['Estoque'] = data_frame['Estoque'].astype(str)
        data_frame['Estoque'] = data_frame['Estoque'].str.strip()
        data_frame['Estoque'] = data_frame['Estoque'].str.replace('="', '', regex=False)
        data_frame['Estoque'] = data_frame['Estoque'].str.replace('"', '', regex=False)

        # Remove linhas que não contém numeros no 'Estoque'
        data_frame = data_frame[data_frame['Estoque'].str.match(r'^[0-9.,]+$', na=False)]

    return data_frame