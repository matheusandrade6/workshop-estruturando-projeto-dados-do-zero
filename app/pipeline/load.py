import pandas as pd
import os




def load_excel(df: pd.DataFrame, output_path: str, file_name: str) -> str:
    """
    receber um dataframe e salvar como um excel .xlsx

    args: dataframe (pd.DataFrame)
    output_path
    file_name

    return "arquivo salvo com sucesso"
    """
    
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    df.to_excel(f'{output_path}/{file_name}.xlsx')
    return 'Arquivo salvo com sucesso'