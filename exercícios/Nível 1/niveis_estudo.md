##### Nível 1: Fundamentos de Python
Tipos de Dados Primitivos
int, float, str, bool
Manipulação e conversão de tipos (exemplo: int("5"), str(10))
##### Estruturas Condicionais
if, elif, else: Controle de fluxo básico.
Operador ternário: Condicional simplificado (x = 10 if y > 5 else 0).
case (usando dicionários ou estruturas alternativas em Python).
##### Estruturas de Repetição
for (com exemplos de strings e range):
for i in 'oi tudo bem'
for i in range(0,7)
for i in range(0,2,8)
while: Loop com condição.
break, continue: Controle do fluxo dentro de loops.
for em uma única linha
aninhamento de for e ifs em uma única linha
##### Funções Básicas
Definição de funções (def), passando parâmetros e retornando valores.
Funções lambdas: Funções anônimas em uma linha (lambda x: x * 2).
Parâmetros nomeados: Passagem de parâmetros usando nome=valor.
Como é a passagem por valor e por referência em ponteiros no python
O que o nome de uma função guarda no python, após ser definida
Passagem de parâmetros: lista ou tupla de parâmetros (*) e dicionário de parâmetro (**)
##### Nível 2: Estruturas de Dados e Tratamento de Exceções
Tipos de Dados Não Primitivos
Listas: Definição e manipulação (adicionar, remover, acessar).
Tuplas: Diferentes de listas, imutáveis.
Dicionários: Chaves e valores, acessos e iteração.
Tratamento de Exceções
Uso de try e except para capturar e tratar erros.
##### Exemplos de exceções personalizadas.
Compreensão de Hash Table e Ordered List
Como dicionários funcionam (hashing e acesso eficiente).
Diferenças entre listas ordenadas e não ordenadas.
Complexidade de tempo O(n) (tempo de execução de operações comuns em listas e dicionários).
##### Operações com Strings
Métodos de manipulação de strings: .upper(), .lower(), .join(), .strip().
Map e Zip: Aplicando funções a coleções.

##### operações avançadas do python
funções list, map, lambda, filter, sum (com listas)
biblioteca itertools (usos para ela)
Regex e como usar no python (regex101.com)
##### Nível 3: Bibliotecas de Dados e Visualização
##### Pandas
DataFrames e Series: Criação, manipulação e acesso aos dados.
Leitura e escrita de arquivos CSV e Excel: read_csv(), read_excel().
.iloc e .loc: Slicing e acesso aos dados.
Query em DataFrame: Filtros e concatenação de DataFrames.
apply + lambda: Processamento de elementos com funções personalizadas.
##### Numpy
Arrays: Operações básicas e avançadas com arrays, como soma, subtração e manipulação de forma.
##### Matplotlib e Seaborn
Criação de gráficos e visualizações.
Personalização de gráficos para análise de dados.

##### módulos: typing e pydantics
boas práticas.
módulos são qualquer tipo de aquivo com extensão .py, mas idealmente, um módulo contém instruções, funções e definições de classes que giram em torno de um proósito semelhante.
Os módulos são mágicos porque nos oferecem ferramentas e métodos para resolver um problema que, de outra forma, teríamos que escrever nós mesmos.

##### Nível 5: Conceitos Avançados e Performance
##### Estruturas de Dados Avançadas
Deque (collections): Uso eficiente para filas e pilhas.
Acesso a elementos em dicionários e como as chaves podem ser tipos variados (ex.: listas, inteiros, etc.).
Funcionalidades de dicionário: .keys(), .items().
Acesso a elementos de dicionário com índice: dict[0].
##### Tipos Avançados e Transformações
astype(): Mudança de tipo de dados de uma coluna no Pandas.
read_csv e read_excel: Trabalhando com arquivos grandes e performance.
##### Nível 6: Práticas e Projetos
##### Projetos e Prática
Criar scripts que envolvam manipulação de arquivos, tratamento de exceções e processamento de dados.
Projetos integrados com Pandas e Pyspark para análise de grandes volumes de dados.
Exercícios práticos com Map, Zip e funções lambda.
##### Nível 4: Trabalhando com Big Data e Conectividade
##### Pyspark
Operações básicas: Criação de DataFrames no Pyspark, manipulação e consulta.
Realização de queries diretamente nas estruturas do Pyspark (sem SQL).
##### Manipulação de Dados em Pyspark
Como trabalhar com grandes volumes de dados e realizar operações eficientes utilizando o Pyspark.