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

times_brasileirao = ("Flamengo", "Palmeiras", "Botafogo", "Fluminense", "Santos")

print(f"Lista de times do mundial: {times_brasileirao}")
print(f"Lista dos tres primeiros: {times_brasileirao[:3]}")
print(f"Lista dos ultimos 2: {times_brasileirao[-2:]}")
print(f"Lista ordenadoos: {sorted(times_brasileirao)}")
print(f"Lista da posição do Botafogo: {times_brasileirao.index('Botafogo')+1}°")