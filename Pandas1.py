import pandas as pd
import numpy as np

def process_data(df, value=None):
    mask = df['country'] == value
    df_filtered = df[mask]
    return df_filtered

def read_csv_file(file_path,value):
    df = pd.read_csv(file_path)
    process_DF=process_data(df,value)
    return process_DF.filter(['country','group_lead_time','group_stays_in_nights','adults','children','babies'])



def main():
    file_path = 'muestra.csv'  
    for i in range(5):
         df = read_csv_file(file_path,value=i)
         print(f"DataFrame with country == {i}:")
         print(df.head())
         print("\n")
         print("\nDataFrame Description:")
         print(df.describe())
         print(df.shape)
         print (df.columns)
         print(df["group_lead_time"])
        
         


if __name__ == "__main__":
    main()