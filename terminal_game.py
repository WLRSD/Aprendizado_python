from mod_soma import add as somaai
import wikipedia

summary = wikipedia.summary("Python (programming language)", sentences=2)
print(summary)
vamosver = somaai(2,4)
print(vamosver)

# valid tuple
t1 = ('a',)

# valid tuple
t2 = 'a',

# NOT a tuple
t3 = ('a')

print(type(t3))

my_dna = ('GCT', 'AGC', 'AGG', 'TAA', 'ACT', 'CAT')
print(my_dna[2]) # Output: AGG

full_name = ('Ada', 'Lovelace')

first_name = full_name[0]

print(first_name) # Output: Ad

# Combining tuples
t1 = 'a',
t2 = 'b',
t3 = t1 + t2

print(t3)  # Output: ('a', 'b')

# criando o code:

my_address = float(input('Digite a sua localização (em latitude e longitude): '))
second_address = float(input('Digite a sua localização: '))
third_address = float(input('Digite a sua localização: '))

my_tuple = (my_address, second_address, third_address)
print(type(my_tuple))

#fazer o valor ficar negativo:
formatando = lambda t: tuple(map(lambda x: x * -1, t))

print(formatando(my_tuple))

formatted_tuple = formatando(my_tuple)

# Comparação entre second_address e third_address
if second_address >= third_address:
    print(f'O {formatted_tuple[1]} está mais longe')
else:
    print(f'O {formatted_tuple[2]} está mais longe')
    
    # multi-line
laptop = {
  'brand': 'Apple',
  'model': 'Macbook Pro',
  'size': 14,
  'year': 2023
}
print(laptop['brand'])

# Creating a dictionary
student_info = {'name': 'Alice', 'age': 9, 'grade': 'A'}

# Accessing dictionary elements
print('Name:', student_info['name'])
print('Age:', student_info['age'])
print('Grade:', student_info['grade'])

# Modifying dictionary elements
student_info['age'] = 10
print('Updated Age:', student_info['age'])

# Dictionary methods
print('Keys:', student_info.keys())
print('Values:', student_info.values())
print('Items:', student_info.items())

#exercício de dicionário:

museum = {
  'artist': ['Branca de neve', 'Homem-aranha', 'Superman'],
  'period': [1963, 1989, 1994],
  'date': ['21-12-1963', '32-09-1989', '14-02-1994']
}

print(museum)
print('Keys:', museum.keys())
print('Values:', museum.values())
print('Items:', museum.items())


conjuntos = {'valor1', 'valor2', 'valor3'}
dicionário = {'chave1':'valor1'}


print(type(conjuntos))
print(type(dicionário))

fruits = {'🍎 apple', '🍌 banana', '🍊 orange'}

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union of sets
union_result = set1.union(set2)

# Intersection of sets
intersection_result = set1.intersection(set2)

# Difference of sets
difference_result = set1.difference(set2)

print(union_result)
print(intersection_result)
print(difference_result)

# Output:
# {1, 2, 3, 4, 5, 6}
# {3, 4}
# {1, 2}

my_set = {1, 2, 3}

my_set.add(4)
print(my_set) # Output: {1, 2, 3, 4}

my_set.remove(2)
print(my_set) # Output: {1, 3, 4}

#exercício

minhas_compras = {'melancia', 'manga', 'laranja'}
compras_amigo = {'manga', 'morango', 'abacaxi'}

uniao = minhas_compras.union(compras_amigo)
print(uniao)

intersecao = minhas_compras.intersection(compras_amigo)
print(intersecao)
