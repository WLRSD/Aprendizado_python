# Primeiras Impressões sobre os Exercícios de Tratamento de Exceções nível 3

## 1. Tenta dividir dois números e captura a exceção caso a divisão seja por zero
Esse exercício foi interessante porque me ensinou a capturar o erro de divisão por zero. Eu usei o `try` para tentar realizar a operação e o `except` para capturar a exceção específica de `ZeroDivisionError`. Isso evita que o programa trave ou gere um erro inesperado.

**O que aprendi**:
- Como capturar exceções específicas usando `except`.
- Como usar `try-except` para evitar erros de execução.

## 2. Lê um número e captura a exceção caso o usuário digite um valor não numérico
Aqui, usei o `try-except` para capturar o erro quando o usuário entra com algo que não pode ser convertido para número, usando `ValueError`. Isso ajuda a garantir que o programa continue funcionando, mesmo que a entrada do usuário seja inválida.

**O que aprendi**:
- Como capturar erros de conversão de tipo com `ValueError`.
- Como garantir que a entrada do usuário seja válida.

## 3. Cria uma exceção personalizada para um erro específico em um cálculo
Neste exercício, aprendi a criar uma exceção personalizada usando `class CustomError(Exception)`. Isso me ajudou a entender como definir erros específicos para situações únicas no meu código. No caso, lancei essa exceção quando o número era negativo.

**O que aprendi**:
- Como criar exceções personalizadas com `class`.
- Como lançar uma exceção específica usando `raise`.

## 4. Lê um arquivo e trata a exceção caso o arquivo não exista
Esse exercício me ensinou a capturar a exceção `FileNotFoundError`, que ocorre quando o arquivo que você tenta abrir não existe. Isso é útil para lidar com problemas de leitura de arquivos sem causar falhas no programa.

**O que aprendi**:
- Como usar `try-except` para lidar com erros de arquivo.
- Como capturar erros como `FileNotFoundError` e exibir mensagens úteis.

## 5. Divide dois números, capturando exceções e exibindo mensagens personalizadas
Aqui, combinei o uso de várias exceções: `ZeroDivisionError` e `ValueError`. Eu aprendi a personalizar a mensagem de erro para diferentes exceções. Isso permite que o programa forneça feedback claro sobre o que deu errado.

**O que aprendi**:
- Como tratar múltiplas exceções em um bloco `try`.
- Como fornecer mensagens de erro mais amigáveis ao usuário.

## 6. Aceita um número e verifica se ele é negativo. Lança uma exceção personalizada caso seja
Neste exercício, criei uma exceção personalizada para lançar quando o número inserido fosse negativo. Isso ajudou a entender como controlar melhor as condições de erro no código e como usar exceções para erros de negócios específicos.

**O que aprendi**:
- Como lançar exceções personalizadas para condições específicas.
- Como usar exceções para controlar entradas de dados.

## 7. Lê a entrada do usuário e captura a exceção caso a entrada seja inválida
Esse exercício me ajudou a entender como capturar exceções genéricas de entrada, como quando o usuário tenta inserir um valor que não pode ser convertido para o tipo esperado. É uma boa maneira de garantir que o programa não quebre por entradas inesperadas.

**O que aprendi**:
- Como tratar entradas de usuários inválidas usando `try-except`.
- Como garantir que o programa não falhe por entradas mal formatadas.

## 8. Divide dois números e usa try-except para evitar divisão por zero
Aqui, apliquei o `try-except` para evitar a divisão por zero. Aprendi a tratar um erro comum de maneira simples e a informar o usuário sobre o problema sem interromper o programa.

**O que aprendi**:
- Como tratar erros de divisão por zero de forma segura e amigável.

## 9. Tenta acessar um item de uma lista, capturando a exceção caso o índice seja inválido
Esse exercício me ensinou a capturar exceções ao tentar acessar um índice inválido em uma lista. O uso de `IndexError` foi útil para garantir que o código não quebrasse ao tentar acessar um índice inexistente.

**O que aprendi**:
- Como tratar `IndexError` ao acessar elementos de uma lista.
- Como garantir que operações de acesso a lista sejam seguras.

## 10. Lida com múltiplas exceções em um bloco try
Neste exercício, pratiquei lidar com várias exceções em um único bloco `try`. Isso é muito útil quando há diferentes tipos de erros que podem ocorrer em um mesmo processo e é necessário tratá-los de maneira distinta.

**O que aprendi**:
- Como tratar múltiplas exceções em um único bloco `try-except`.
- Como usar exceções gerais (`Exception`) para capturar erros inesperados.

---

Esses exercícios me ajudaram a entender como capturar e lidar com diferentes tipos de exceções em Python. O tratamento de exceções é importante para criar programas mais robustos e que não falham quando enfrentam entradas inesperadas ou erros de execução. O uso de `try`, `except`, `else`, e `finally` se mostrou essencial para garantir a estabilidade e a usabilidade dos programas.
