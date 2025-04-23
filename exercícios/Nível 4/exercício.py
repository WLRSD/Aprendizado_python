#%%

# 1. Crie uma lista e adicione alguns elementos nela
my_list = [1, 2, 3]
my_list.append(4)
my_list.append(5)
print(my_list)
#%%

# 2. Remova um item específico de uma lista
my_list = [1, 2, 3, 4, 5]
my_list.remove(3)
print(my_list)
#%%

# 3. Acesse um elemento específico de uma lista utilizando índice
my_list = [10, 20, 30, 40, 50]
print(my_list[2])
#%%

# 4. Crie uma tupla com 3 elementos e imprima
my_tuple = (1, 2, 3)
print(my_tuple)
#%%

# 5. Modifique um item de uma lista utilizando índice
my_list = [1, 2, 3, 4, 5]
my_list[2] = 10
print(my_list)
#%%

# 4. Crie uma tupla com 3 elementos e imprima
my_tuple = (1, 2, 3)
print(my_tuple)
#%%

# 5. Modifique um item de uma lista utilizando índice
my_list = [1, 2, 3, 4, 5]
my_list[2] = 10
print(my_list)
#%%

# 6. Crie um dicionário com pelo menos três pares chave-valor
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict)
#%%

# 7. Acesse o valor de uma chave em um dicionário
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict["age"])
#%%

# 8. Adicione um novo par chave-valor em um dicionário
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
my_dict["job"] = "Engineer"
print(my_dict)
#%%

# 9. Faça um programa que percorre um dicionário e imprime as chaves e valores
my_dict = {"name": ["Alice", "Andreza"], "age": [25, 26], "city": ["New York", "Brazil"]}
for key, value in my_dict.items():
    print(key, value)
#%%

# 10. Crie um programa que aceita uma entrada do usuário e insere em uma lista se o valor não existir
my_list = [1, 2, 3, 4, 5]
user_input = int(input("Dgite um valor: "))
if user_input not in my_list:
    my_list.append(user_input)
print(my_list)
#%%

# 11: Crie uma lista com os números de 1 a 100 (int), utilizando um for de uma única linha
numeros = [i for i in range(1, 101)]
print(numeros)
# %%

# 12: Exiba o quadrado entre um intervalo de 1 a 10

numeros = [i*i for i in range(1, 11)]
print(numeros)
# %%

# 13: Exiba a lista de quadrados entre um intervalo de 1 a 10 desde que seja par
numeros = [i*i for i in range(1,11) if i%2 == 0]
print(numeros)


# %%

par = (10, 20)
a, b = par
 
print(f"Antes da troca: a = {a}, b = {b}")
 
a, b = b, a
print(f"Depois da troca: a = {a}, b = {b}")


def soma(numero1, numero2):
    print(f"o numero1: {numero1} e o numero2 é {numero2}.")
    return numero1 + numero2

resultado_soma = soma(*par)
print(resultado_soma)


par_dict = {"numero2":15,"numero1":20}
resultado_soma2 = soma(**par_dict)
print(resultado_soma2)

# %%
aluno = ["warlison", "junior", "andreza"]
nota = [7.0, 9.0, 8.0]
idade = [10,20,30]

for a,n,i in zip(aluno,nota,idade):
    print(f"{a}:{n} com idade {i}")
print(list(zip(aluno,nota,idade)))
for tupla in zip(aluno,nota,idade):
    print(f"{tupla[0]}:{tupla[1]} com idade {tupla[2]}")

teste = "warslison"
teste = "junior"

# %%
