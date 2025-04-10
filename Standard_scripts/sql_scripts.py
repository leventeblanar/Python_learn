import pandas as pd

def get_data_from_excel():

    excel = 'file_source'

    excel_df = pd.read_excel(excel)

    # dropping Nan values
    excel_df_notnan = excel_df.dropna()
    excel_df_notnan = excel_df_notnan.astype({'col1': int, 'col2': int})
    
    for index, row in excel_df_notnan.iterrows():
        print(row['col1'], row['col2'])
        with open('output.sql', 'a') as sql_file:
            sql_file.write(f"SQL_SCRIPT")