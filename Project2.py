import numpy as np
import pandas as pd
import seaborn as sns


def load_data(ruta):
    # Cargar el conjunto de datos 'titanic' de seaborn
    titanic = pd.read_csv(ruta)
    return titanic


def filter_by_age(data_frame, value = 0):
    if value > 0:
        return data_frame[data_frame['Age'] > value]
    else:
        return data_frame.dropna(subset=['Age'])

def filter_by_sex_and_age(data_frame, sex, age):
    return data_frame[(data_frame['Sex'] == sex) & (data_frame['Age'] > age)]

def orfer_by_fare(data_frame):
    return data_frame.sort_values(by='Fare', ascending=True)

def order_by_age_and_class (data_frame):
    return data_frame.sort_values(by=[ 'Pclass' , 'Age'], ascending=[True, True])

def reset_index(data_frame):
    return data_frame.reset_index(drop=True)

def percentile(data_frame, column1=None, filtro = None ,column2=None, percent =1):
    if column1 is not None and column2 is not None and filtro is not None:
        df_aux = data_frame[(data_frame[column1] == filtro)  & (data_frame[column2]> data_frame[column2].quantile(percent))]
        return df_aux
    else:
        return data_frame

def main():
    # Cargar el conjunto de datos 'tips' de seaborn
    path = 'titanic.csv'
    pd_titanic = load_data(path)
    print("#2-1:\n", filter_by_age(pd_titanic,0))
    
    print("#2-2:\n", filter_by_age(pd_titanic,50))
    
    print("#2-3:\n", filter_by_sex_and_age(pd_titanic,'female',30))
    print("#2-4:\n", orfer_by_fare(pd_titanic))
    print("#2-5:\n", order_by_age_and_class(pd_titanic))
    print("#2-6:\n", reset_index(pd_titanic))
    print("#2-7:\n", percentile(pd_titanic, column1='Embarked', filtro='C', column2='Fare', percent=0.90))

   
if __name__ == "__main__":
    main()  