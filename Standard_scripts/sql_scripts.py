import pandas as pd

def get_data_from_excel_forSQL():

    ## This is a simple method of turning a bunch of excel data into SQL prompts line by line

    excel = 'file_path'

    ### This is a converter method to clean data before even reading xlsx files
    def clean_float_as_str(val):
        if pd.isna(val):  # if the value is Nan - keep it as Nan
            return val
        elif isinstance(val, float) and val.is_integer(): # if the value is float but the value itself is an integer (1.0)
            return str(int(val)) # return a string made of the float 1.0 converted to int 1 -> '1'
        return str(val)
    
    excel_df = pd.read_excel(excel, converters={
        "col1": clean_float_as_str,
        "col2": clean_float_as_str
    })

    for index, row in excel_df.iterrows():
        print(row['col1'], row['col2'])
        with open('output.sql', 'w') as sql_file:
            if pd.isna(row['col2']):
                sql_file.write(f"SQL_1")
            else:
                sql_file.write(f"SQL_2")

