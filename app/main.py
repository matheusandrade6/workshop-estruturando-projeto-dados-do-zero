from pipeline.extract import read_files
from pipeline.transform import concat_dataframes
from pipeline.load import load_excel

if __name__ == '__main__':
    df_list = read_files('../data')
    df = concat_dataframes(df_list)
    load_excel(df, 'data/output', 'output')