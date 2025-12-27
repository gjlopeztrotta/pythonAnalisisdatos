import seaborn as sns
import numpy as np
import pandas as pd

def load_data(ruta):
    # Cargar el conjunto de datos 'titanic' de seaborn
    titanic = pd.read_csv(ruta)
    return titanic

def main():
    # Cargar el conjunto de datos 'tips' de seaborn
    path = 'titanic.csv'
    titanic = load_data(path)
    header(titanic, n=10)
    bottom(titanic, n=10)
    get_types(titanic)
    convert_to_category(titanic, 'Sex')
    print("#1-4:\n", titanic.dtypes)
    sum_column_result = sum_column(titanic, 'Fare')
    print(f"#1-5:\n Sum of fare: {sum_column_result}")
    print("#1-6:\n", get_statistics(titanic, 'Age'))
    print("#1-7:\n", NumpyArray(titanic, 'Age'))
    
    
 
def header(dataframe, n=5):     
    print("#1-1:\n", dataframe.head(n))
    
def bottom(dataframe, n=5):     
    print("#1-2:\n", dataframe.tail(n))
    
def get_types(dataframe):
    print("#1-3:\n", dataframe.dtypes)
    
def sum_column(dataframe, column_name):
    total = dataframe[column_name].sum()
    return total

def get_statistics(dataframe, column_name):
    stats = {
        'mean': dataframe[column_name].mean(),
        'median': dataframe[column_name].median(),
        'std_dev': dataframe[column_name].std()
    }
    return stats

def NumpyArray(dataframe, column_name):
    array = dataframe[column_name].to_numpy()
    return array    
    
    
def convert_to_category(dataframe, column_name):
    dataframe[column_name] = dataframe[column_name].astype('category')
    return dataframe

if __name__ == "__main__":
    main()
