import mysql.connector
import tkinter as tk
from tkinter import ttk

def obtener_datos():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="test_python"
    )
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM nombres_apellido")
    datos = cursor.fetchall()
    conexion.close()
    return datos

ventana = tk.Tk()
ventana.title("Personas desde MySQL")

tabla = ttk.Treeview(ventana, columns=("Nombre", "Edad"), show="headings")
tabla.heading("Nombre", text="Nombre")
tabla.heading("Edad", text="Edad")

for fila in obtener_datos():
    tabla.insert("", tk.END, values=fila)

tabla.pack(expand=True, fill="both")

ventana.mainloop()
