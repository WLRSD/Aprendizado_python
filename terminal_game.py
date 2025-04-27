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