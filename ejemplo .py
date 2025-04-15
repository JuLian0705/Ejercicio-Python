import os
import win32com.client  # Solo funciona en Windows
import pandas as pd

def excel_to_pdf(input_folder, output_folder):
    """
    Convierte todos los archivos Excel en una carpeta a formato PDF automáticamente.
    :param input_folder: Carpeta donde están los archivos Excel.
    :param output_folder: Carpeta donde se guardarán los PDFs.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = False  # Ejecuta Excel en segundo plano
    
    for file in os.listdir(input_folder):
        if file.endswith(".xlsx") or file.endswith(".xls"):
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, file.replace(".xlsx", ".pdf").replace(".xls", ".pdf"))
            
            try:
                workbook = excel.Workbooks.Open(input_path)
                workbook.ExportAsFixedFormat(0, output_path)  # 0 es para exportar como PDF
                workbook.Close(False)
                print(f"Convertido: {file} -> {output_path}")
            except Exception as e:
                print(f"Error al convertir {file}: {e}")
    
    excel.Quit()

# Configuración de carpetas
input_folder = "C:/Users/USER/Documents/bitacoras"  # Cambia esta ruta
output_folder = "C:/Users/USER/Documents/bitacoras/pdf"   # Cambia esta ruta

excel_to_pdf(input_folder, output_folder)
