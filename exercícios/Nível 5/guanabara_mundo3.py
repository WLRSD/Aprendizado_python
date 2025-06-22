valores_extenso = ("um", "dois", "três", "quatro", "cinco")
valor_numerico = (1, 2, 3, 4, 5)

while True:
    valor_usu = int(input("Digite um valor [1-5]: "))
    if valor_usu in valor_numerico:
        valor_mostrar = valores_extenso[valor_usu - 1]
        break
    else:
        print("Valor inválido, tente novamente.")

print(valor_mostrar)