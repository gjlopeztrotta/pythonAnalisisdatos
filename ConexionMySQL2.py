import mysql.connector


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
        
def main():
    conexion = conectar_mysql()
    consulta = "SELECT * FROM gjlopeztrotta.usuarios"
    Resultado = listar_datos(conexion, consulta)
    for fila in Resultado:
        print(fila) 
    
    sql = "INSERT INTO usuarios (Nombre,Apellido, Mail, Telefono, Pais, Edad) VALUES (%s, %s, %s, %s,%s, %s)"
    valores = ("Juan", "Perez", "juan@example.com","696656585", "Argentina", "30")

    status = insertar_datos(conexion,sql, valores)
    print(f" registro insertado: {status}")
    cerrar_conexion(conexion)
          
if __name__ == "__main__":
    main()