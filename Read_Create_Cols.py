# En nuestro Excel tenemos 3 columnas: 
#   COLUMNA (Contiene todos los nombres de las columnas de la tabla)
#   TIPO DE DATO (Contiene los datatypes de las columnas)
#   DESCRIPCIÓN (Contiene la descripción de las columnas)
#
# El código toma el contenido del excel y lo inserta en un string que se genera en la variable "linea_codigo"
#
# Se puede cambiar el texto a cualquier tipo de oracion que se desee replicar 

import pandas as pd

# Cargar el archivo Excel
archivo_excel = "/Users/tabla.xlsx"  # Reemplazar con la ruta del archivo
hoja = "Hoja1"  # Reemplazar con el nombre de la hoja (opcional si tenemos varias hojas)

# Leer la tabla desde Excel
df = pd.read_excel(archivo_excel, sheet_name=hoja)

# Generar código para cada columna. 
codigo_generado = []
for _, row in df.iterrows():
    nombre_columna = row["COLUMNA"]
    tipo_dato = row["TIPO DE DATO"]
    descripcion = row["DESCRIPCIÓN"]

    # Generar línea de código
    linea_codigo = f'{nombre_columna} = Column({tipo_dato}, primary_key=False, comment="{descripcion}")'
    codigo_generado.append(linea_codigo)

# Guardar el código en un archivo de texto o imprimirlo
codigo_final = "\n".join(codigo_generado)
print(codigo_final)