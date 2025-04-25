# criar um pequeno relatório que possa desenvolver minhas habilidades com pandas e mathplotlib
 
#conseguir conectar ao banco de dados do homol
from sqlalchemy import create_engine
from sqlalchemy.sql import text
import cx_Oracle
import pandas as pd
 
# Configurações de conexão (mudar para o meu)
username = ''
password = ''
host = ''
port = ''
service_name = ''
 
# String de conexão
connection_string = f'oracle+cx_oracle://{username}:{password}@{host}:{port}/?service_name={service_name}'
 
# Criação do engine
engine = create_engine(connection_string)
sql="SELECT * FROM ORAATDOW0002.INRO_ATDT WHERE ROWNUM <= 50"
 
with engine.connect() as connection:
    result = connection.execute(text(sql))
    # Converter o resultado para lista antes de criar o DataFrame (pois vem como uma tupla)
    result_list = list(result)
df = pd.DataFrame(result_list, columns=['id', 'telefone', 'valor1', 'data_completa', 'outra_data', 'valor2', 'valor3'])
print(df.head())
 
#passando para um dataframe do pandas ()
df = pd.DataFrame(result_list, columns=['id', 'telefone', 'valor1', 'data_completa', 'outra_data', 'valor2', 'valor3'])
colunas = list(df.columns)
print(f'Nome das colunas: {colunas}')
 
print('Primeiras linhas do dataframe: ')
print(df.head())