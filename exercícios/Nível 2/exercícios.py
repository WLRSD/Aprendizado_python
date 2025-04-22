# 1. Verifica se um número é positivo ou negativo
def check_number():
    num = float(input("Digite um valor ai: "))
    if num >= 0:
        print("Positivo")
    else:
        print("Negativo")

check_number()

# 2. Verifica se uma pessoa tem idade maior ou igual a 18
def check_age():
    idade = int(input("Digite uma idade ai: "))
    if idade >= 18:
        print("Maior de idade")
    else:
        print("Menor de idade")

check_age()

# 3. Classifica a idade em faixas etárias
def classify_age():
    idade = int(input("Digite uma idade ai: "))
    if idade <= 12:
        print("Criança")
    elif idade <= 17:
        print("Adolescente")
    elif idade <= 59:
        print("Adulto")
    else:
        print("Idoso")

classify_age()

# 4. Verifica se um número é par ou ímpar usando operador ternário
def check_par_impar():
    num = int(input("Digite um valor: "))
    print("Par" if num % 2 == 0 else "Ímpar")

check_par_impar()

# 5. Calcula a maior entre três números
def maior_entre_tres():
    a = int(input("Primeiro valor: "))
    b = int(input("Segundo valor: "))
    c = int(input("Terceiro valor: "))
    if a >= b and a >= c:
        print(a)
    elif b >= a and b >= c:
        print(b)
    else:
        print(c)

maior_entre_tres()

# 6. Verifica se um número está no intervalo de 1 a 10
def check_intervalo():
    num = int(input("Vamos verificar se está no intervalo: "))
    if 1 <= num <= 10:
        print("No intervalo")
    else:
        print("Fora do intervalo")

check_intervalo()

# 7. Controla um loop que imprime números de 1 a 10, mas pula o número 5
def loop_com_pulo():
    for i in range(1, 11):
        if i == 5:
            continue
        print(i)

loop_com_pulo()

# 8. Lê a entrada de idade e imprime se pode votar
def pode_votar():
    idade = int(input("Qual sua idade?: "))
    print("Pode votar" if idade >= 16 else "Não pode votar")

pode_votar()

# 9. Verifica se uma palavra contém a letra "a"
def verifica_letra():
    palavra = str(input("digite uma palavra ai: "))
    if "a" in palavra:
        print("Contém a letra a")
    else:
        print("Não contém a letra a")

verifica_letra()

# 10. Recebe a idade e imprime "Idoso" se maior que 60, caso contrário, "Não Idoso"
def verifica_idoso():
    idade = int(input("Digite a idade ai: "))
    print("Idoso" if idade > 60 else "Não Idoso")

verifica_idoso()


