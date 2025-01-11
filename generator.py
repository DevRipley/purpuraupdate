# Pandas Dependency: pip install pandas
# Openpyxl Dependency: pip install openpyxl
import pandas as pd

# ASCII art log
print(r"""

$$$$$$$\                                                             
$$  __$$\                                                            
$$ |  $$ |$$\   $$\  $$$$$$\   $$$$$$\  $$\   $$\  $$$$$$\  $$$$$$\  
$$$$$$$  |$$ |  $$ |$$  __$$\ $$  __$$\ $$ |  $$ |$$  __$$\ \____$$\ 
$$  ____/ $$ |  $$ |$$ |  \__|$$ /  $$ |$$ |  $$ |$$ |  \__|$$$$$$$ |
$$ |      $$ |  $$ |$$ |      $$ |  $$ |$$ |  $$ |$$ |     $$  __$$ |
$$ |      \$$$$$$  |$$ |      $$$$$$$  |\$$$$$$  |$$ |     \$$$$$$$ |
\__|       \______/ \__|      $$  ____/  \______/ \__|      \_______|
                              $$ |                                   
                              $$ |                                   
                              \__|                                   
      $$\   $$\                 $$\            $$\                   
      $$ |  $$ |                $$ |           $$ |                  
      $$ |  $$ | $$$$$$\   $$$$$$$ | $$$$$$\ $$$$$$\    $$$$$$\      
      $$ |  $$ |$$  __$$\ $$  __$$ | \____$$\\_$$  _|  $$  __$$\     
      $$ |  $$ |$$ /  $$ |$$ /  $$ | $$$$$$$ | $$ |    $$$$$$$$ |    
      $$ |  $$ |$$ |  $$ |$$ |  $$ |$$  __$$ | $$ |$$\ $$   ____|    
      \$$$$$$  |$$$$$$$  |\$$$$$$$ |\$$$$$$$ | \$$$$  |\$$$$$$$\     
       \______/ $$  ____/  \_______| \_______|  \____/  \_______|    
                $$ |                                                 
                $$ |                                                 
                \__|                                                 
      
""")
print("PurpuraUpdate iniciado...\n")

# Ruta al archivo Excel
file_path = "excel.xlsx"

# Leer desde un rango específico (A3 y C3 hasta abajo)
data = pd.read_excel(file_path, usecols="A,C", skiprows=2)  # Salta las 2 primeras filas (empezando en la fila 3)

# Renombrar columnas para mayor claridad (ajusta según tus datos reales)
data.columns = ["codigo_articulo", "cantidad"]

# Eliminar filas con valores nulos
data = data.dropna()

# Generar las consultas SQL
sql_statements = [
    f"UPDATE articulo SET cant_existen = cant_existen + {int(row['cantidad'])} WHERE codigo_articulo = '{row['codigo_articulo']}';"
    for _, row in data.iterrows()
]

# Guardar las consultas en un archivo SQL
sql_file_path = "actualizar_cantidades.sql"
with open(sql_file_path, "w") as sql_file:
    sql_file.write("\n".join(sql_statements))

# Log the number of rows read and affected
print(f"Total de filas leídas: {len(data)}")
print(f"Total de filas afectadas y agregadas al archivo SQL: {len(sql_statements)}")

# Imprimir mensaje de confirmación
print(f"Archivo SQL generado: {sql_file_path}")
