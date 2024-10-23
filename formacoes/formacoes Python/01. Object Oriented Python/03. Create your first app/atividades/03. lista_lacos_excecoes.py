# MODULOS E FUNCOES

# Exercicio 1
print('''1 - Crie uma lista para cada informação a seguir:

Lista de números de 1 a 10;
Lista com quatro nomes;
Lista com o ano que você nasceu e o ano atual.
      ''')

numbers = ['',1,2,3,4,5,6,7,8,9,10,'']
print(f'{numbers}\n')

names = ['Raissa','Zahira','Aada','Emma','']
print(f'{names}\n')

years = [1500,2024]
print(f'{years}\n')

for number in numbers:
    print(number)

for name in names:
    print(name)

for year in years:
    print(year)

################################################################################################################

# Exercicio 2
print('\n\n2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.\n')

names = ['','Raissa','Zahira','Aada','Emma','']

for name in names:
    print(name)

################################################################################################################
    
# Exercicio 3
print('\n\n3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.\n')

numbers = [1,2,3,4,5,6,7,8,9,10]
soma = 0

for number in numbers:
    if number % 2 != 0:
        soma += number

print(f'a soma total dos numeros impares: {soma}')

########################################################

# outra solucao:

soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i
print(soma_impares)

################################################################################################################

# Exercicio 4
print('\n\n4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.\n')

for i in range(10, 0, -1):
    print(i)
    
################################################################################################################

# Exercicio 5
print('\n\n5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.\n')

number = int(input('Digite um numero: '))

for i in range(1, 11, +1):
    tab = number * i
    print(f'{number} * {i} = {tab}')

################################################################################################################

# Exercicio 6
print('\n\n6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.\n')

number_list = [48,5,356,25,7926,439,-4789,'d']
counter = 0

try:
    for number in number_list:
        counter += number
    
    print(f'soma dos numeros: {counter}')

except Exception as e:
    print(f"Ocorreu um erro: {e}")
# except TypeError:
#     print("Uma das entradas não é um dado válido.")

################################################################################################################

# Exercicio 7
print('\n\n7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.\n')

values = [48,5,356,25,7926,439,-478974]
counter = 0

try:
    for value in values:
        counter += value
    average = counter / len(values)
    print(f'A média é: {average}')
except ZeroDivisionError:
    print('A lista está vazia.')
except Exception as e:
    print(f"Ocorreu um erro: {e}")

########################################################

# outras solucoes:
# solucao 1
def calcular_media(lista):
    soma = 0
    try:
        for numero in lista:
            soma += numero
        media = soma / len(lista)
        return media
    except ZeroDivisionError:
        return "A lista está vazia."

minha_lista = [1, 2, 3, 4, 5]
media = calcular_media(minha_lista)
print(f"A média é: {media}")

########################################################

# solucao 2

def calcular_media(lista):
    try:
        return sum(lista) / len(lista)
    except ZeroDivisionError:
        return "A lista está vazia."
    
########################################################

# solucao 3

import statistics

def calcular_media(lista):
    try:
        return statistics.mean(lista)
    except statistics.StatisticsError:
        return "A lista está vazia."
    
########################################################

# solucao 4

def calcular_media(lista):
    try:
        return sum(lista) / len(lista)
    except ZeroDivisionError:
        return "A lista está vazia."
    except TypeError:
        return "A lista contém elementos que não são números."

minha_lista = [1, 2, 'a', 3]
media = calcular_media(minha_lista)
print(media)  # Saída: A lista contém elementos que não são números.