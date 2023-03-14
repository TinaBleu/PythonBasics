##En caso de requerir una conexión a la nube --> importar librerias para las credenciales (aqui vienen unas adicionales para hacer analisis).
import numpy as np
import pandas as pd
import snowflake.connector as sf
import datetime as dt
import seaborn as sns
import getpass
#import scipy.stats as stats
#from sklearn.preprocessing import StandardScaler
#from sklearn.cluster import KMeans
#from collections import Counter
#import matplotlib.pyplot as plt

##Creamos variables que vamos a utilizar en la conexión
username = input('Usuario Snowflake: ')
password = getpass.getpass('Contraseña Snowflake: ') #Si, es la contraseña del usuario de snowflake que se quiere conectar.
account = 'cuenta.us-east-1' #aquí va la zona a la que se conecta snowflake, se puede encontrar desde el buscador como parte del link https
warehouse = 'INSERTE_NOMBRE_WAREHOUSE'

##Aqui vamos a definir la conexión a snowflake a través de un cursor. 
def sql_query(sql):
    
    ## snoflake connection
    with sf.connect(user = username, password = password, account = account, warehouse = warehouse) as conn:
        ## cursor
        with conn.cursor() as curs:
            ## EXECUTE
            curs.execute(sql)
            ## data frame
            df = curs.fetch_pandas_all()
        
    return df
print(sql_query)

##Extrayendo la información de la nube
data = """SELECT*FROM INSERTE_QUERY_DE_LO_QUE_SEA"""
data = sql_query(data)
data.head()

##Convirtiendo a Excel
data.to_excel(r'C:\Users\Este_Equipo\Documentos\Conteo_Users_por_Version_16012023.xlsx', startrow = 2, sheet_name = 'Nombre_hoja_excel')
