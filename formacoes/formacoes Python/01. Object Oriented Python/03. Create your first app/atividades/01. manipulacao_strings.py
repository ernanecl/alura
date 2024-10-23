# MANIPULACAO DE STRINGS

# Exercicio 1
print('1 - Imprima a frase: Python na Escola de Programação da Alura.\n')

print('Python na Escola de Programacao da Alura\n')

# Exercicio 2
print('\n2 - Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.\n')

name = input('Digite seu nome: ')
age = input('Digite sua idade: ')

print(f'\nMeu nome é {name} e tenho {age} anos\n')

# Exercicio 3
print('\n3 - Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha, como mostrado a seguir:')
print('''
      A
      L
      U
      R
      A
      ''')

# Exercicio 4
print('\n4 - Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma variável e arredondado para apenas duas casas decimais.\n')

numero = 3.14159
numero_arredondado = round(numero, 2)
print(f'O valor arredondado de pi é: {numero_arredondado}')