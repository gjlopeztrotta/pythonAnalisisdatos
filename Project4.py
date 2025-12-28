import pandas as pd
import numpy as np      
import seaborn as sns

def main():
    file_path = 'auto-mpg.csv'  
    pd=load_data_from_csv(file_path)
    listar_datos(pd,7,'l')
    replace_missing_with_mean(pd,'horsepower')
    filter_data_by_origin_and_cylinders(pd,1,4)
    highest_car(pd,['car_name', 'mpg'])
    highest_car(pd,['car_name', 'displacement'])
    highest_car(pd,['car_name', 'mpg'])
    
def listar_datos(pd,q,fl):
    if fl == 'f':
        print(pd.head(q))
    else:
        print(pd.tail(q))

def replace_missing_with_mean(pd, column_name):
    if column_name in pd.columns:
        mean_value = pd[column_name].replace('?', np.nan).astype(float).mean()
        pd[column_name] = pd[column_name].replace('?', mean_value).astype(float)
        print(f"Valores faltantes en la columna '{column_name}' reemplazados por la media: {mean_value}")
    else:
        print(f"La columna '{column_name}' no existe en el DataFrame.")
    

def load_data_from_csv(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Datos cargados desde el archivo CSV.")
        return data
    except Exception as e:
        print(f"Error al cargar datos desde CSV: {e}")
        return None

def filter_data_by_origin_and_cylinders(pd, origin_value, cylinders_value):
    filtered_data = pd[(pd['origin'] == origin_value) & (pd['cylinders'] == cylinders_value)]
    print(f"Datos filtrados por origin={origin_value} y cylinders={cylinders_value}:")
    print(f"Number of cars from 'usa' with 4 cylinders:{len(filtered_data)}")
    print(filtered_data)
    return filtered_data

def highest_car(pd,visual,filtro='mpg'): 
    max_value = pd[filtro].max()
    car_with_max_mpg = pd[pd[filtro] == max_value]
    print("Car with the highest MPG:")
    print(car_with_max_mpg[visual])



if __name__ == "__main__":
    main()
    