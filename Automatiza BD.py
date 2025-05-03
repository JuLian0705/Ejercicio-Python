import pandas as pd
from sqlalchemy import create_engine

usuario = 'root'
contraseña = ''
host = 'localhost'
puerto = '3306'
base_datos = 'test_python'
tabla = 'nombres_apellido'

conexion = f'mysql+pymysql://{usuario}:{contraseña}@{host}:{puerto}/{base_datos}'

df = pd.read_sql(f'SELECT * FROM {tabla}', con=conexion)

df.to_excel(f'{tabla}.xlsx', index=False)

print(f"Datos exportados a {tabla}.xlsx")
