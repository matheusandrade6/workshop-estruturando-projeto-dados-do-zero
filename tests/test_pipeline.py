import pandas as pd
from app.pipeline.transform import concat_dataframes

df_1 = pd.DataFrame({'col 1': [1,2], 'col 2': [3,5]})
df_2 = pd.DataFrame({'col 1': [4,5], 'col 2': [7,9]})

df_list = [df_1,df_2]

def test_concat_dataframes():
    arrange = pd.concat(df_list, ignore_index=True)
    act = concat_dataframes(df_list)

    assert arrange == act


# Para testar, rodar pytest -v