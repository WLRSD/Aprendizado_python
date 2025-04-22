# Primeiras Impressões sobre Tipos de Dados Não Primitivos Nível 4

## 1. Criação de uma lista e adição de elementos
Neste exercício, aprendi a criar uma lista e adicionar elementos a ela usando o método `append()`. As listas são estruturas de dados ordenadas e mutáveis, ou seja, podemos modificar seus elementos após a criação.

**O que aprendi**:
- Como criar e adicionar itens a uma lista usando `append()`.
- Como manipular elementos de uma lista.

## 2. Remoção de um item específico de uma lista
Aqui, usei o método `remove()` para excluir um item específico de uma lista. Se o item não existir, o Python gerará uma exceção `ValueError`.

**O que aprendi**:
- Como remover um item de uma lista de forma eficiente.
- Como gerenciar a remoção de itens sem usar índices diretamente.

## 3. Acesso a um elemento específico de uma lista utilizando índice
Aprendi que as listas em Python são indexadas, ou seja, podemos acessar qualquer elemento da lista pelo seu índice. O índice começa em 0, o que significa que o primeiro elemento tem índice 0, o segundo tem índice 1, e assim por diante.

**O que aprendi**:
- Como acessar um elemento de uma lista usando seu índice.

## 4. Criação de uma tupla com 3 elementos
Criei uma tupla, que é muito parecida com uma lista, mas com uma diferença fundamental: **tuplas são imutáveis**. Ou seja, uma vez criada, não podemos modificar seus valores. Tuplas são mais rápidas do que listas e são úteis quando você tem dados que não vão mudar.

**O que aprendi**:
- Tuplas são semelhantes às listas, mas imutáveis.
- Como criar e imprimir uma tupla.

## 5. Modificação de um item de uma lista utilizando índice
Aprendi a modificar um item de uma lista diretamente utilizando seu índice. Diferente das tuplas, **listas são mutáveis**, o que significa que seus valores podem ser alterados a qualquer momento.

**O que aprendi**:
- Como modificar elementos de uma lista usando seu índice.
- A diferença entre listas e tuplas em relação à mutabilidade.

## 6. Criação de um dicionário com três pares chave-valor
Neste exercício, criei um **dicionário**, que é uma estrutura de dados composta por pares chave-valor. Ao contrário das listas e tuplas, em que acessamos os dados por índices, em dicionários, os dados são acessados por **chaves únicas**. Dicionários são úteis quando você precisa associar dados a uma chave específica.

**O que aprendi**:
- Como criar e usar dicionários com pares chave-valor.
- Como os dicionários funcionam de forma diferente das listas e tuplas.

## 7. Acesso ao valor de uma chave em um dicionário
Aprendi a acessar os valores de um dicionário utilizando suas **chaves**. Isso é diferente de listas e tuplas, em que usamos índices para acessar os elementos. As chaves podem ser de qualquer tipo imutável, como números, strings, etc.

**O que aprendi**:
- Como acessar valores em dicionários usando chaves.

## 8. Adição de um novo par chave-valor em um dicionário
Neste exercício, aprendi a adicionar novos pares chave-valor em um dicionário. Como os dicionários são mutáveis, é possível adicionar, modificar ou excluir pares a qualquer momento.

**O que aprendi**:
- Como adicionar novos pares chave-valor a um dicionário.

## 9. Percorrendo um dicionário e imprimindo chaves e valores
Aqui, usei o método `items()` para percorrer um dicionário e acessar tanto as chaves quanto os valores. Isso foi útil para imprimir todas as informações do dicionário de forma dinâmica.

**O que aprendi**:
- Como percorrer e acessar chaves e valores em um dicionário.
- Como utilizar o método `items()` para facilitar esse processo.

## 10. Inserção em uma lista com verificação de duplicatas
Neste exercício, aprendi a verificar se um valor já existe na lista antes de adicionar um novo item. Isso é útil quando queremos evitar duplicatas e garantir que a lista contenha apenas valores exclusivos.

**O que aprendi**:
- Como verificar se um valor já existe em uma lista antes de adicionar um novo item.

---

## Diferenças entre Listas, Tuplas e Dicionários

### Listas
- **Mutabilidade**: Listas são mutáveis, o que significa que podemos adicionar, remover ou modificar seus elementos.
- **Indexação**: São indexadas por números inteiros, começando do índice 0.
- **Uso**: Use listas quando precisar de uma coleção ordenada e mutável, como uma lista de compras ou uma fila de espera.
  
### Tuplas
- **Imutabilidade**: Tuplas são imutáveis, ou seja, depois de criadas, seus elementos não podem ser alterados.
- **Indexação**: Assim como as listas, tuplas também são indexadas, mas você não pode modificar os elementos após a criação.
- **Uso**: Use tuplas quando os dados não precisarem ser modificados após a criação, por exemplo, em coordenadas geográficas (latitude, longitude) ou dados imutáveis em geral.

### Dicionários
- **Estrutura de chave-valor**: Dicionários armazenam dados como pares de chave e valor, em vez de apenas valores ordenados. As chaves são únicas e os valores podem ser de qualquer tipo.
- **Mutabilidade**: Dicionários são mutáveis, então você pode adicionar, alterar e remover pares chave-valor a qualquer momento.
- **Uso**: Use dicionários quando precisar de uma correspondência entre uma chave e um valor, como em registros de usuários, onde você tem um nome de usuário (chave) e uma senha (valor).

---

Esses exercícios me ajudaram a entender as diferenças fundamentais entre listas, tuplas e dicionários, como usá-los e quando escolher qual tipo de dado utilizar. Listas são ótimas para coleções mutáveis e ordenadas, tuplas são ideais quando precisamos de dados imutáveis, e dicionários são perfeitos para associar chaves a valores, oferecendo uma maneira muito eficiente de organizar dados.
