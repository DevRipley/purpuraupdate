# PurpuraUpdate

PurpuraUpdate es una herramienta que permite actualizar la cantidad de artículos en una base de datos a partir de un archivo Excel.

## Requisitos

- Python 3.x
- Pandas: `pip install pandas`
- Openpyxl: `pip install openpyxl`

## Uso

1. Coloca tu archivo Excel en la misma carpeta que el script y nómbralo `excel.xlsx`.
2. Asegúrate de que el archivo Excel tenga los datos en las columnas A y C, comenzando desde la fila 3.
3. Ejecuta el script `generator.py`.

```sh
python generator.py
```

## Descripción del Script

El script realiza las siguientes acciones:

1. Lee un archivo Excel (`excel.xlsx`) desde un rango específico (columnas A y C, comenzando desde la fila 3).
2. Renombra las columnas para mayor claridad.
3. Elimina las filas con valores nulos.
4. Genera consultas SQL para actualizar la cantidad de artículos en la base de datos.

## Ejemplo de Salida

El script generará consultas SQL como las siguientes:

```sql
UPDATE articulo SET cant_existen = cant_existen + 10 WHERE codigo_articulo = 'A001';
UPDATE articulo SET cant_existen = cant_existen + 5 WHERE codigo_articulo = 'A002';
```

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que desees realizar.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT.
