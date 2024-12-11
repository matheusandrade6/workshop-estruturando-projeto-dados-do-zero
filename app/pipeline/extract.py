import os # lib para manipular arquivos e pastas
import glob # lib para listar arquivos
import pandas as pd
from typing import List

"""
Função para ler os arquivos de uma pasta data/input 
e retornar uma lista de DataFrames

args: input_path(str): caminho da pasta

return: lista de dataframes
"""

path = '../../data'

def read_files(path: str) -> List[pd.DataFrame]:
    # glob lista todos os arquivos de uma pasta com o caminho conhecido
    all_files = glob.glob(os.path.join(path,'*.xlsx'))

    df_list = []
    for file in all_files:
        data = pd.read_excel(file)
        df_list.append(data)
    
    return df_list

if __name__ == '__main__':
    df_list = read_files(path)
