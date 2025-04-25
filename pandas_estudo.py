# criar um pequeno relatório que possa desenvolver minhas habilidades com pandas e mathplotlib

#conseguir conectar ao banco de dados do homol
from pyparsing import alphas
from sqlalchemy import create_engine
from sqlalchemy.sql import text
import cx_Oracle, tempo
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurações de conexão
username = ''
password = ''
host = ''
port = ''
service_name = ''

# String de conexão
connection_string = f'oracle+cx_oracle://{username}:{password}@{host}:{port}/?service_name={service_name}'

# Criação do engine
engine = create_engine(connection_string)
sql="""SELECT a.CD_INRO,
  a.NR_CTU_UTZD_AGT_CNH,
  a.NM_ARQ_OGM_DADO,
  a.TS_INC_INRO,
  a.QT_DRCO_TTL_CHMD,
  a.NR_PTL_ATDT,
  b.NR_SEQL_LNH_CTU,
  b.TX_LNH_CTU 
FROM ORAATDOW0002.INRO_ATDT a
LEFT JOIN ORAATDOW0002.LNH_CTU_UTZD_AGT_CNH b
ON a.NR_CTU_UTZD_AGT_CNH = b.NR_CTU_UTZD_AGT_CNH
WHERE TRUNC(a.TS_INC_INRO) = TO_DATE('2025-03-22', 'YYYY-MM-DD')
ORDER BY a.CD_INRO, b.NR_SEQL_LNH_CTU """

start_time = tempo.tempo_iniciar()
with engine.connect() as connection:
    result = connection.execute(text(sql))
    # Converter o resultado para lista antes de criar o DataFrame (pois vem como uma tupla)
    result_list = list(result)

execution_time = tempo.tempo_finalizar(start_time)
print(f'\n\nTempo de execução para trazer os dados necessários do banco de dados: {execution_time:.2f} segundos.\n\n')

start_time = tempo.tempo_iniciar()
df = pd.DataFrame(result_list, columns=['cd_inro', 'nr_ctu_utzd', 'nm_arq_ogm', 'data', 'duracao_chmd', 'protocol', 'nr_seql', 'txt'])
print(df.head())
execution_time = tempo.tempo_finalizar(start_time)
print(f'\n\nTempo de execução para tranformar em um dataframe: {execution_time:.2f} segundos.\n\n')



#passando para um dataframe do pandas ()
df = pd.DataFrame(result_list, columns=['cd_inro', 'nr_ctu_utzd', 'nm_arq_ogm', 'data', 'duracao_chmd', 'protocol', 'nr_seql', 'txt'])
colunas = list(df.columns)
print(f'Nome das colunas: {colunas}')

# ver as primeiras linhas de um dataframe
#print('Primeiras linhas do dataframe: ')
#print(df.head())

# ver as últimas linhas de um datafreame
#print(f'Últimas linhas do dataframe: \n {df.tail(10)}')

# ver o que está no meio de um dataframe (uso do fatiamento)
#print(f'As linhas do meio do dataframe: {df[20:30]}')

# ver o descritivo de um dataframe
# print(f'Descrição do dataframe: {df.describe()}')

# primeiro devo ordernar o dataframe (precisei ordernar na hora de trazer do banco de dados)
start_time = tempo.tempo_iniciar()
df = df.sort_values(by=['cd_inro', 'nr_seql']) #mas fica aqui para estudo

# agora devo agrupar pelo cd_inro
texto_agrupado = df.groupby('cd_inro')['txt'].apply(''.join).reset_index()

# verificando o tamanho do texto após agrupar
texto_agrupado['texto_completo'] = texto_agrupado['txt']
texto_agrupado['comprimento'] = texto_agrupado['texto_completo'].apply(len)
execution_time = tempo.tempo_finalizar(start_time)
print(f'\n\nTempo de execução para fazer ordenação, agrupar e verificar o tamanho dos textos: {execution_time:.2f} segundos.\n\n')


# resultado: tamanho de um texto concatenado, baseado na ordenação e agrupamento de 2 colunas da tabela
print(texto_agrupado)


start_time = tempo.tempo_iniciar()
# criando um novo dataframe para as faixas
bins = [0, 999, 4999, 9999, 19999, float('inf')]
labels = ['0 a 999', '1000 a 4999', '5000 a 9999', '10000 a 19999', '20000+']

texto_agrupado['faixa_caracteres'] = pd.cut(texto_agrupado['comprimento'], bins=bins, labels=labels, right=True)

df_faixa = texto_agrupado.groupby('faixa_caracteres', observed=False).agg(quantidade=('cd_inro', 'count')).reset_index()

execution_time = tempo.tempo_finalizar(start_time)
print(f'\n\nTempo de execução para fazer a criação de um novo dataframe com faixas: {execution_time:.2f} segundos.\n\n')


print(df_faixa)

# aprender um pouco de matplotlib: bar plot
start_time = tempo.tempo_iniciar()
plt.figure(figsize=(10,6))
sns.barplot(x='faixa_caracteres', y='quantidade', data=df_faixa, palette='viridis')

plt.title('Distribuição de CD_INRO por FAIXA_CARACTERE', fontsize=16)
plt.xlabel('Faixa_caracteres', fontsize=16)
plt.ylabel('Quantidade de cd_inro', fontsize=12)

plt.xticks(rotation=45)
plt.show()
execution_time = tempo.tempo_finalizar(start_time)
print(f'\n\nTempo de execução para criar e mostrar o gráfico bar plot: {execution_time:.2f} segundos.\n\n')


# agora fazer um outro gráfico: scatter plot
start_time = tempo.tempo_iniciar()
plt.figure(figsize=(10,6))
sns.scatterplot(x='comprimento', y='cd_inro', data=texto_agrupado, color='blue', alpha=0.6)

plt.title('Distribuição de comprimento dos textos', fontsize=16)
plt.xlabel('Comprimento do texto', fontsize=16)
plt.ylabel('Cd_inro', fontsize=12)
execution_time = tempo.tempo_finalizar(start_time)
print(f'\n\nTempo de execução para criar e mostrar o gráfico scatter plot: {execution_time:.2f} segundos.\n\n')


plt.show()


# agora fazer um outro gráfico: histogram
start_time = tempo.tempo_iniciar()
plt.figure(figsize=(10,6))
sns.histplot(data = texto_agrupado, x='comprimento', kde=True, color='green', bins=30)

plt.title('Ditribuição do comprimento de textos', fontsize=16)
plt.xlabel('Comprimento do texto', fontsize=16)
plt.ylabel('Frequência', fontsize=12)
execution_time = tempo.tempo_finalizar(start_time)
print(f'\n\nTempo de execução para criar e mostrar o gráfico histogram: {execution_time:.2f} segundos.\n\n')

plt.show()