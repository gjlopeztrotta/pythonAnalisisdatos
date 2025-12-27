from ast import arg
import mysql.connector
import sys
import pandas as pd
import numpy as np
import seaborn as sns


def conectar_mysql():
    try:
        # Conexión a la base de datos
        conexion = mysql.connector.connect(
        host="localhost",        # Tu servidor (ej: localhost, 127.0.0.1)
        user="gjlopeztrotta",       # Tu usuario de MySQL
        password="Megustaconducir@2024", # Tu contraseña
        database="gjlopeztrotta" # Nombre de tu base de datos
    )
        if conexion.is_connected():
            print("¡Conectado a MySQL exitosamente!")
            return conexion
    except mysql.connector.Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None
    
def cerrar_conexion(conexion):
    if conexion and conexion.is_connected():
        conexion.close()
        print("Conexión a MySQL cerrada.")

def insertar_datos(conexion, consulta, datos):
    try:
        cursor = conexion.cursor()
        cursor.execute(consulta, datos)
        conexion.commit()
        print("Datos insertados correctamente.")
        return "ok"
    except mysql.connector.Error as e:
        print(f"Error al insertar datos: {e}")
        return "ko"
    finally:
        if cursor:
            cursor.close()
            
def listar_datos(conexion, consulta):
    try:
        cursor = conexion.cursor()
        cursor.execute(consulta)
        resultados = cursor.fetchall()
        return resultados
    except mysql.connector.Error as e:
        print(f"Error al listar datos: {e}")
        return []
    finally:
        if cursor:
            cursor.close()
 
def load_data_from_csv(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Datos cargados desde el archivo CSV.")
        print(data.head())  # Muestra las primeras filas del DataFrame
        return data
    except Exception as e:
        print(f"Error al cargar datos desde CSV: {e}")
        return pd.DataFrame()  # Retorna un DataFrame vacío en caso de error 
    
def load_database(data,conexion):
    rechazados=0
    insertados=0
    for reg in range(len(data)):
        sql = "INSERT INTO titanic (PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked) VALUES (%s,%s, %s, %s, %s,%s,%s, %s, %s, %s,%s, %s)"
        valores = (
            int(data.loc[reg, 'PassengerId']),
            int(data.loc[reg, 'Survived']),
            int(data.loc[reg, 'Pclass']),
            data.loc[reg, 'Name'],
            data.loc[reg, 'Sex'], 
            int(data.loc[reg, 'Age'] if not np.isnan(data.loc[reg, 'Age']) else 0), 
            int(data.loc[reg, 'SibSp']),
            int(data.loc[reg, 'Parch']),
            data.loc[reg, 'Ticket'],
            float(data.loc[reg, 'Fare']) if not np.isnan(data.loc[reg, 'Fare']) else 0,
            data.loc[reg, 'Cabin'] if pd.notna(data.loc[reg, 'Cabin']) else None,
            data.loc[reg, 'Embarked'] if pd.notna(data.loc[reg, 'Embarked']) else None
        )
                       
        status = insertar_datos(conexion, sql, valores)  
        if status == "ko":
            rechazados+=1   
        else:   
            insertados+=1

    print(f"Registros insertados: {insertados}")
    print(f"Registros rechazados: {rechazados}")    
        

 
def estadisticas_datos(conexion):
    data=(listar_datos(conexion, "SELECT * FROM titanic"))
    pd_data=pd.DataFrame(data, columns=['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'])
    # Ejemplo de procesamiento: Mostrar estadísticas descriptivas
    print("Estadísticas descriptivas del conjunto de datos:")
    print(pd_data.describe())
    
    
def filtrar_datos(conexion, filtro, value):
    query = f"SELECT * FROM titanic WHERE {value} = {filtro}"
    data=(listar_datos(conexion, query))
    pd_data=pd.DataFrame(data, columns=['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'])
    print(pd_data)
    return pd_data
    

        
def main():
    conexion = conectar_mysql()
    if len(sys.argv) > 1 and sys.argv[1] == 'load':
        file_path = 'titanic.csv'  # Ruta al archivo CSV
        data = load_data_from_csv(file_path)
        load_database(data, conexion)
    elif len(sys.argv) > 1 and sys.argv[1] == 'list':
        consulta = "SELECT * FROM titanic"
        resultados = listar_datos(conexion, consulta)
        for fila in resultados:
            print(fila)
    elif len(sys.argv) > 1 and sys.argv[1] == 'Procesar':
        estadisticas_datos(conexion)
    elif len(sys.argv) > 3 and sys.argv[1] == 'Filtrar':
        filtro = sys.argv[2]
        value = sys.argv[3]
        filtrar_datos(conexion, filtro, value)
        filtro2=filtrar_datos(conexion, filtro, value)
        auxiliar=filtro2[filtro2[sys.argv[4]]== sys.argv[5]]
        #print(f"{auxiliar}=filtro2[filtro2['Sex']== {sys.argv[4]}]")
        print(auxiliar)
    else:
        print("Uso: python ConexionMySQL3.py [load|list|Procesar|Filtrar]")


    cerrar_conexion(conexion)
          
if __name__ == "__main__":
    main()