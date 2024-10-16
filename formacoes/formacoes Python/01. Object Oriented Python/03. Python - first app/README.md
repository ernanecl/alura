### Python - primeiro app

#### Manipulacao Strings

##### App Sabor Express

Vamos usar o `Python` para o desenvolvimento do `back-end` da aplicacao.

Iniciamos criando um diretorio com nome `sabor-express`, onde vai conter toda a aplicacao.

Para executar um arquivo `Python` em ambientes `Linux`, usamos o seguinte comando:

```BASH
python3 file_name.py
```

Lembrando que temos que informar a versao 3 do `Python` em sistemas `Linux`, com o `Windows` nao temos a necessidade de informar a versao.

&nbsp;

Artigo [Convenções de nomenclatura](https://www.alura.com.br/artigos/convencoes-nomenclatura-camel-pascal-kebab-snake-case)

&nbsp;


Primeira versao do codigo:

```PY
print('''
      Sabor Express      
      ''')

print('1. Cadastrar restaurante')
print('2. Listar restaurante')
print('3. Ativar restaurante')
print('4. Sair\n')

opcao_escolhida = input('Escolha uma opcao: ')

#print('\nVoce escolheu a opcao', opcao_escolhida)
print(f'\nVoce escolheu a opcao {opcao_escolhida}!4')
```

&nbsp;

##### Exercicios:

```PY
# Exercícios

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
```

&nbsp;

##### Dica

Quando usamos a funcao `print` para imprimir uma boa quantidade de conteudo com quebra de linhas, podemos usar mais de uma maneira para estar imprimindo, como no modelo a seguir:

```PY
# opcao 1
print('''Camiseta Unissex
Tamanho: P, M, G, GG
Material: 100% algodão
Cores disponíveis: Preto, Branco, Vermelho''')

# opcao 2
print("Camiseta Unissex","Tamanho: P, M, G, GG","Material: 100% algodão","Cores disponíveis: Preto, Branco, Vermelho", sep ='\n')
```

&nbsp;

Metodo para o usuario colocar dados dentro da variavel:

```PY
departamento = input("Digite o nome do departamento: ")
responsavel = input("Digite o nome da pessoa responsável: ")
print("O departamento de " + departamento + " é liderado por " + responsavel + ".")
```

&nbsp;


#### Modulos e funcoes

##### App Sabor Express

Essa etapa colocamos funcoes e tornamos o arquivo `app.py` como o arquivo principal do nosso programa.

Segue a baixo o codigo realizado nesse modulo:

```PY
import os

def exibir_nome_app():
    print('''
        Sabor Express      
        ''')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    # os.system('cls') - no Windows
    os.system('clear')
    print('Encerrando App\n')

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opcao: '))
    # opcao_escolhida = int(opcao_escolhida)

    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('Listar restaurante')
    elif opcao_escolhida == 3:
        print('Ativar restaurante')
    elif opcao_escolhida == 4:
        finalizar_app()
    else:
        print('Opcao invalida')

def main():
    exibir_nome_app()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
```

&nbsp;

##### Informativo:

def (funcao) e' um bloco de instrucao com o objetivo de realizar uma determinada acao quando acionada para execucao

&nbsp;

Para tornar um arquivo `Python` como arquivo principal, precisamos trabalhar com a variavel `name` criada pelo interpretador, essa variavel `name` recebendo o valor `main`, significa que o arquivo vai se tornar o principal da aplicacao e o codigo tambem nao pode ser importado para outros codigos.

&nbsp;

##### Alternativas:

No bloco do codigo que usamos a condicional `if`, `elfi` e `else`, temos a opcao de usar a instrucao `match` que tem um comportamento semelhante, podendo ser mais organizada e legível para lidar com múltiplas condições.

Bloco usando `if`, `elif` e `else`:

```PY
opcao_escolhida = int(input('Escolha uma opção: '))

if opcao_escolhida == 1:
    print('Adicionar restaurante')
elif opcao_escolhida == 2:
    print('Listar restaurantes')
elif opcao_escolhida == 3:
    print('Ativar restaurante')
elif opcao_escolhida == 4:
    print('Finalizar app')
else:
    print('Opção inválida!')
```

&nbsp;

Bloco usando `match`:

```PY
opcao_escolhida = int(input('Escolha uma opção: '))
match opcao_escolhida:
    case 1:
        print('Adicionar restaurante')
    case 2:
        print('Listar restaurantes')
    case 3:
        print('Ativar restaurante')
    case 4:
        print('Finalizar app')
    case _:
        print('Opção inválida!')
```

&nbsp;

###### Vantagens da Instrução `match`

Lidar com condições complexas e múltiplos padrões de maneira mais intuitiva.	
Sintaxe concisa melhora a legibilidade do código, especialmente em casos complexos.
Permite desestruturação direta, evitando repetição excessiva de variáveis.
Adiciona expressividade ao código, especialmente em situações de correspondência de padrões.


###### Vantagens da Estrutura `if` `elif` `else`

Implementação clássica e amplamente conhecida.
Amplamente suportada em todas as versões do Python.
Estrutura simples e direta para lógica condicional básica.
Pode ser mais intuitiva para devs familiarizados com estruturas de controle convencionais.

&nbsp;

##### Exercicios:

```PY
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
```

&nbsp;
&nbsp;

#### Lista, lacos e excecoes

##### App Sabor Express

Continuamos desenvolvendo funcoes, porem comecamos a trabalhar com novas instrucoes como as listas.

Segue a baixo o codigo realizado nesse modulo:

```PY
import os

restaurantes = ['Pizza', 'Sushi']

def exibir_nome_app():
    print('''
        Sabor Express      
        ''')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def exibir_subtitulo(texto):
    os.system('clear')
    print(texto)
    print()

def voltar_ao_menu_principal():
    input('Digite qualquer tecla para voltar ao menu ')
    print()
    main()
    
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_restaurante = input('Digite o nome do restaurante para cadastro: ')
    restaurantes.append(nome_restaurante)

    print(f'\nO restaurante {nome_restaurante} foi cadastrado com sucesso\n')

    voltar_ao_menu_principal()

def listar_restaurante():
    exibir_subtitulo('Listando restaurantes')

    for restaurante in restaurantes:
        print(f'.{restaurante}')

    voltar_ao_menu_principal()

def finalizar_app():
    exibir_subtitulo('Encerrando App')

def opcao_invalida():
    exibir_subtitulo('Opcao invalida')
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opcao: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('clear')
    exibir_nome_app()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
```

&nbsp;

##### Tuplas vs Listas

As `tuplas` são estruturas de dados que permite armazenar elementos de maneira ordenada e sequencial, assim como as `listas`.
Dessa forma, ambas mantêm a ordem dos elementos e oferecem índices para acessar esses valores.

Contudo, existem diferenças fundamentais entre `tuplas` e `listas` que as tornam adequadas para diferentes situações.

&nbsp;

Sintaxe:

O primeira diferenca entre eles é a sintaxe. As listas utiliza colchetes [ ], enquanto as tuplas utiliza parênteses ( ).
Como o exemplo a seguir:

```PY
lista = [1,’olá mundo’,True,9.7]
tupla = (1,’olá mundo’,True,9.7)
```

&nbsp;

Mutabilidade:

A maior diferença entre essas duas configurações são as propriedades de mutabilidade!

As listas são estruturas mutáveis, o que significa que é possível modificar seus elementos, adicionar novos itens ou remover existentes após a criação da lista.
Inclusive utilizar funções próprias como append(), remove(), pop(), e insert().

Ao contrário das listas, tuplas são imutáveis. Uma vez que uma tupla é criada, seus elementos não podem ser alterados, adicionados ou removidos.

&nbsp;

Desempenho:

Devido à sua imutabilidade, as tuplas têm um desempenho melhor do que listas para algumas operações. Elas são mais eficientes em termos de espaço e processamento em determinados cenários.

Sendo assim, listas podem ser menos eficientes em termos de desempenho para operações específicas, especialmente quando se trata de manipulação de grandes conjuntos de dados, devido à sua mutabilidade.

&nbsp;

Quando devo utilizar cada estrutura?

&nbsp;

As listas são ideais quando você precisa de uma coleção de elementos que pode ser modificada ao longo do tempo. Por exemplo, criar uma lista de tarefas que pode ser atualizada.

Como no código a seguir:

```PY
# Criando uma lista de compras
lista_de_compras = ["Maçã", "Banana", "Leite", "Pão", "Queijo"]

# Adicionando um item à lista
lista_de_compras.append("Ovos")

# Removendo um item da lista
lista_de_compras.remove("Banana")

# Exibindo a lista
print("Lista de Compras:")
for item in lista_de_compras:
    print("- " + item)
```

&nbsp;

As tuplas são apropriadas quando se deseja garantir que os elementos não sejam alterados após a criação. Isso é útil para dados que devem permanecer constantes ao longo do tempo.

Como as tuplas são imutáveis, elas podem ter um desempenho ligeiramente melhor em operações de leitura e acesso a elementos. Isso também as tornam adequadas para situações em que a eficiência é crucial.

Podemos ver um exemplo uma tupla que armazena as coordenadas geográficas de uma localização específica, que são dados imutáveis que queremos ter acesso, como mostrado a seguir:

```PY
# Definindo uma tupla de coordenadas geográficas
coordenadas_gps = (40.7128, -74.0060)

# Exibindo as coordenadas
print("Coordenadas GPS:")
print("Latitude:", coordenadas_gps[0])
print("Longitude:", coordenadas_gps[1])
```

Lembre-se de sempre avaliar as condições de projeto e escolher qual das duas estruturas é mais adequada para cada situação.

Para saber mais sobre Tuplas no Python, consulte os materiais:

[Documentação Python - Tuplas](https://docs.python.org/pt-br/3/tutorial/datastructures.html#tuples-and-sequences)
[Tupla no Python: o que é, como criar e manipular e suas diferenças com as Listas.](https://www.alura.com.br/artigos/conhecendo-as-tuplas-no-python)

&nbsp;
&nbsp;

##### While

Criar um programa em que o usuario tenha interacao com o sistema, precisamos garantir o a informacao que o usuario insere e' valido para o campo solicitado.

Uma maneira de trabalharmos com esse tipo de situacao podemos utilizar a estrutura de repeticao `for`, junto com `try`/`except` e `if` para que a condicao seja satisfeita.

Como no codigo a seguir:

```PY
numero = -1

try:
    for _ in range(3):  # Supondo um número máximo de tentativas (3) arbitrário
        numero = int(input("\nDigite um número positivo: "))
        print('''
numero invalido, o numero digitado foi menor que zero
              ''')
        
        if numero > 0:
            print(f'Você digitou: {numero}\n')
            break
except:
    print('''
opcao invalida
          ''')
```

Esse loop e' definido com um número arbitrário de tentativas para inserir o valor.

Isso acontece, porque o loop `for` é utilizado quando conhece previamente o número de iterações a ser realizadas.

Para que o usuario digite a quantidade de vezes ilimitada, a estrutura `for` nao atende esse tipo de acao.

Em Python, existe duas estruturas de controle de fluxo para a execução de blocos de repetição: o `for` e o `while`.

O uso do `while`, é quando a quantidade de iterações não é conhecido.

Ainda assim depende de uma condição específica para manter o bloco de código em repetição.

Sintaxe `while`:

```PY
while condição:
    # Bloco de código a ser repetido
```

Agora o uso do `while` no mesmo exemplo anterior, quando usamos `for`:

```PY
numero = -1

try:
    while numero <= 0:
        numero = int(input("Digite um número positivo: "))
        
    print("Você digitou:", numero)

except:
    print('\nopcao invalida')
```


Para saber mais sobre `while` no `Python`, acesse o link abaixo:

[Documentacao Python - While](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement)

&nbsp;
&nbsp;

##### Exercicios:

```PY
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
```