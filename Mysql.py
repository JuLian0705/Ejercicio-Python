import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test_python"
)

if conn.is_connected():
    print("Conexión exitosa a la base de datos")
else:
    print("Error al conectar a la base de datos")

conn.close()