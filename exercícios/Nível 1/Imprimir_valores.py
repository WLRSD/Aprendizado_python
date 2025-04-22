# Criar váriaveis de diversos tipos e imprimir seus valores
numero_inteiro = 10       
numero_decimal = 3.14     
texto = "Olá, Mundo!"     
condicao = True          
nulo = None               

valores_inteiros = [1,2.5,40.55,10.000]

inteiros = [int(valor) for valor in valores_inteiros]

print("Os valores inteiros são: ", inteiros) #modelo antigo, mas ainda funciona no python3
print(f"Os valores inteiros são: {inteiros}") #modelo atual do python3 (PEP 498: Literal String Interpolation)


# Converta valores que são números ou não para pontos flutuantes

valores_decimal = ["3.14", 34.53]

flutuantes = [float(valor2) for valor2 in valores_decimal]

print(f"Os valores flutuantes são: {flutuantes}")

# Criar uma variável boolena de alguns jeitos (falando que uma coisa é maior que outra e se o resultado esperado e com uma condicional)
x = 10
y = 20
print(x > y)  
print(x < y)  

a = True
b = False
print(a and b)  
print(a and (not b))  
print(a or b)   
print(not a)    

# Caso precisasse em algum código, criar uma variável para forçar quando uma ação for veradeira ou falsa

is_active = True  
is_complete = False 

chuva = True

if chuva:
    print("Leve um guarda-chuva!") 
else:
    print("Não precisa de guarda-chuva.")
    
# Cálculo de um inteiro/decimal e um float, ou seja, cálculo entre tipos númericos diferentes
def calculate():
    num1 = 10  
    num2 = 5.5  
    result = num1 + num2
    print(result)

calculate()


