# MODULOS E FUNCOES

# Exercicio 1
print('1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.')

numero_escolhido = int(input('Escolha um numero: '))

if numero_escolhido % 2 == 0:
    print(f'o numero {numero_escolhido} é par')
else:
    print(f'o numero {numero_escolhido} é impar')

# Exercicio 2
print('2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:')

sua_idade = int(input('Digite sua idade: '))

if 0 <= sua_idade <= 12:
    print('Criança: 0 a 12 anos;')
elif 13 <= sua_idade <= 18:
    print('Adolescente: 13 a 18 anos;')
elif sua_idade > 18:
    print('Adulto: acima de 18 anos.')
else:
    print('Opcao invalida')


# Exercicio 3
print('3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.')

login = input('Digite seu login: ')
password = input('Digite sua senha: ')

if login == 'Aluno' and password == 'Alura':
    print("Acesso permitido!")
else:
    print("Acesso negado.")

# Exercicio 4
print('''4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer
      Utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra
      
      Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
      Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
      Terceiro Quadrante: os valores de x e y devem ser menores que zero;
      Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
      Caso contrário: o ponto está localizado no eixo ou origem.
      ''')

x = int(input("Passe a coordenada do ponto x: "))
y = int(input("Passe a coordenada do ponto y: "))

if x > 0 and y > 0:
    print(f'As coordenadas sao maiores que 0 e se encontram no Primeiro Quadrante: x = {x} e y = {y}')
elif x < 0 and y > 0:
    print(f'As coordenadas estao no Segundo Quadrante, x menor que zero e y maior que zero: x = {x} e y = {y}')
elif x < 0 and y < 0:
    print(f'As coordenadas estao no Terceiro Quadrante, x e y menores que zero: x = {x} e y = {y}')
elif x > 0 and y < 0:
    print(f'As coordenadas estao no Quarto Quadrante, x maior que zero e y menor que zero: x = {x} e y = {y}')
else:
    print('O ponto está localizado no eixo ou origem.')