# 1. Tenta dividir dois números e captura a exceção caso a divisão seja por zero
def divide_numbers():
    try:
        num1 = int(input("Digite um valor ai: "))
        num2 = int(input("Digite um valor ai: "))
        result = num1 / num2
        print(result)
    except ZeroDivisionError:
        print("Erro! Não é possível dividir por zero.")

divide_numbers()

# 2. Lê um número e captura a exceção caso o usuário digite um valor não numérico
def read_number():
    try:
        num = int(input("Digite um número: "))
        print(num)
    except ValueError:
        print("Erro! Valor não numérico.")

read_number()

# 3. Cria uma exceção personalizada para um erro específico em um cálculo
class CustomError(Exception):
    pass

def custom_exception():
    try:
        num = int(input("Digite um valor ai: "))
        if num < 0:
            raise CustomError("Número negativo não permitido!")
        print(num)
    except CustomError as e:
        print(e)

custom_exception()

# 4. Lê um arquivo e trata a exceção caso o arquivo não exista
def read_file():
    try:
        with open("file.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("Erro! Arquivo não encontrado.")

read_file()

# 5. Divide dois números, capturando exceções e exibindo mensagens personalizadas
def safe_divide():
    try:
        num1 = int(input("Digite um valor ai: "))
        num2 = int(input("Digite um valor ai: "))
        result = num1 / num2
        print(result)
    except ZeroDivisionError:
        print("Não é possível dividir por zero.")
    except ValueError:
        print("Erro! Entrada não numérica.")

safe_divide()

# 6. Aceita um número e verifica se ele é negativo. Lança uma exceção personalizada caso seja
class NegativeNumberError(Exception):
    pass

def check_negative_number():
    try:
        num = int(input("Digite um número: "))
        if num < 0:
            raise NegativeNumberError("Número negativo detectado!")
        print(num)
    except NegativeNumberError as e:
        print(e)

check_negative_number()

# 7. Lê a entrada do usuário e captura a exceção caso a entrada seja inválida
def user_input():
    try:
        user_input = int(input("Digite um valor ai: "))
        print(user_input)
    except ValueError:
        print("Entrada inválida!")

user_input()

# 8. Divide dois números e usa try-except para evitar divisão por zero
def divide():
    try:
        num1 = int(input("Digite um valor: "))
        num2 = int(input("Digite um valor: "))
        print(num1 / num2)
    except ZeroDivisionError:
        print("Erro! Divisão por zero.")

divide()

# 9. Tenta acessar um item de uma lista, capturando a exceção caso o índice seja inválido
def access_list():
    my_list = [1, 2, 3]
    try:
        index = int(input("Digite um inteiro: "))
        print(my_list[index])
    except IndexError:
        print("Erro! Índice inválido.")

access_list()

# 10. Lida com múltiplas exceções em um bloco try
def multiple_exceptions():
    try:
        num1 = int(input("Digite um valor: "))
        num2 = int(input("Digite um valor: "))
        result = num1 / num2
        print(result)
    except ZeroDivisionError:
        print("Erro! Não é possível dividir por zero.")
    except ValueError:
        print("Erro! Entrada não numérica.")
    except Exception as e:
        print(f"Erro desconhecido: {e}")

multiple_exceptions()
