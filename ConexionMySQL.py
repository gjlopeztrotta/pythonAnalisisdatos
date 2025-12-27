import mysql.connector

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
        info_servidor = conexion.get_server_info()
        print(f"Versión de MySQL: {info_servidor}")

        # Crear un cursor para ejecutar comandos SQL
        cursor = conexion.cursor()

        # Ejemplo de consulta: mostrar bases de datos
        cursor.execute("SHOW DATABASES")
        for db in cursor:
            print("Bases de datos disponibles:")
            print(db)

except mysql.connector.Error as e:
    print(f"Error al conectar a MySQL: {e}")

finally:
    # Cerrar cursor y conexión
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'conexion' in locals() and conexion.is_connected():
        conexion.close()
        print("Conexión a MySQL cerrada.")