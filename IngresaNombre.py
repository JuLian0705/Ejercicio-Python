import mysql.connector
import tkinter as tk
from tkinter import messagebox

def guardar_datos():
    nombre = entry_nombre.get()
    edad = entry_edad.get()

    if not nombre or not edad:
        messagebox.showerror("Error", "Por favor, completa todos los campos.")
        return
    try:
        edad = int(edad)
    except ValueError:
        messagebox.showerror("Error", "La edad debe ser un número entero.")
        return

    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="test_python"
        )
        cursor = conexion.cursor()

        cursor.execute("INSERT INTO nombres_apellido (nombre, edad) VALUES (%s, %s)", (nombre, edad))
        conexion.commit()

        messagebox.showinfo("Éxito", "Datos guardados correctamente.")

        entry_nombre.delete(0, tk.END)
        entry_edad.delete(0, tk.END)

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al conectar a la base de datos: {err}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
    
ventana = tk.Tk()
ventana.title("Guardar Nombre y Edad")
ventana.geometry("300x200")

label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.pack(pady=5)

entry_nombre = tk.Entry(ventana)
entry_nombre.pack(pady=5)

label_edad = tk.Label(ventana, text="Edad:")
label_edad.pack(pady=5)

entry_edad = tk.Entry(ventana)
entry_edad.pack(pady=5)

boton_guardar = tk.Button(ventana, text="Guardar", command=guardar_datos)
boton_guardar.pack(pady=20)

ventana.mainloop()

