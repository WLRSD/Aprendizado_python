# exercício 72: Criar com tuplas números por extenso, e ao usuário informar um número, dentro do escopo 
# oferecido, ele retornar o nome por extenso
# valores_extenso = ("um", "dois", "três", "quatro", "cinco")
# valor_numerico = (1, 2, 3, 4, 5)

# while True:
#     valor_usu = int(input("Digite um valor [1-5]: "))
#     if valor_usu in valor_numerico:
#         valor_mostrar = valores_extenso[valor_usu - 1]
#         break
#     else:
#         print("Valor inválido, tente novamente.") 

# print(valor_mostrar)

# Exercício 73: Criar um programa que vai buscar os 5 primeiros times do brasileirão e vai utilizar métodos
# para conseguir informações ou pequenas alterações da tupla

# times_brasileirao = ("Flamengo", "Palmeiras", "Botafogo", "Fluminense", "Santos")

# print(f"Lista de times do mundial: {times_brasileirao}")
# print(f"Lista dos tres primeiros: {times_brasileirao[:3]}")
# print(f"Lista dos ultimos 2: {times_brasileirao[-2:]}")
# print(f"Lista ordenadoos: {sorted(times_brasileirao)}")
# print(f"Lista da posição do Botafogo: {times_brasileirao.index('Botafogo')+1}°")

# Exercício 74: Crie um programa que gere 5 números aleatórios e coloque em uma tupla
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior

# from random import randint

# numero_randomico = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), 
#                     randint(1,10))

# print(f"Os valores foram: {numero_randomico}", end="")  

# for criacao in numero_randomico:
#     print(f"{numero_randomico} ", end="")
    
# print(f"\nO maior valor dentro da tupla foi: {max(numero_randomico)}")
# print(f"\nO menor valor dentro da tupla foi: {min(numero_randomico)}")
    
# Exercício 75: Crie um programa que leia quatro valores pelo teclado e guarde-os
# em uma tupla. No final, mostre: 
# Quantas vezes apareceu o 7
# Em que posição foi digitado o primeiro valor 1
# Quais foram os números pares

contador = 0
lembrar_numeros = []
while contador < 4:
    numero = (int(input("Digite um número: ")))
    lembrar_numeros.append(numero)
    contador += 1
    
lembrar_numeros = tuple(lembrar_numeros)
print(lembrar_numeros)
print(f"Quantas vezes apareceu o número 7: {lembrar_numeros.count(7)} vezes")
if 1 in lembrar_numeros:
    print(f"O valor 1 apareceu na {lembrar_numeros.index(1)+1}° posição")
else:
    print("O valor 1 não foi digitado")
print("Os valores pares digitados foram: ", end="")
for numero in lembrar_numeros:
   if numero % 2 == 0:
        print(numero, end=" ")
