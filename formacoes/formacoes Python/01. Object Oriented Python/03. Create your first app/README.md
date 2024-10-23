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

#### Dicionarios

Esta etapa trabalhou com dicionarios `(dictionary{key:value})` e na visualizacao do codigo e execucao do sistema.

Segue o codigo com os novos recursos:

```PY
import os

restaurantes = [{'nome':'Praca', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'Italiana', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Arabe', 'ativo':False}]

def exibir_nome_app():
    print('''
        Sabor Express      
        ''')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado restaurante')
    print('4. Sair\n')

def exibir_subtitulo(texto):
    os.system('clear')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_ao_menu_principal():
    input('\nDigite qualquer tecla para voltar ao menu ')
    print()
    main()
    
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_restaurante = input('Digite o nome do restaurante para cadastro: ')
    categoria = input(f'Digite a categoria do restaurante {nome_restaurante}: ')

    dados_restaurante = {'nome':nome_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_restaurante)

    print(f'\nO restaurante {nome_restaurante} foi cadastrado com sucesso\n')

    voltar_ao_menu_principal()

def listar_restaurante():
    exibir_subtitulo('Listando restaurantes')

    print(f'{' Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status do restaurante')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternando estado restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante nao foi encontrado')

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
            alternar_estado_restaurante()
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

##### Exercicios

```PY
# EXERCICIO 1
print('1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.')

personal_data = {'Name':'Zahira','Age':'25 years old','City':'Ajman'}
print(f'\n{personal_data['Name']}\n{personal_data['Age']}\n{personal_data['City']}\n')
print(personal_data.keys())
print(personal_data.values())

# Imprimindo todas as chaves
print('\nTodas as chaves:', personal_data.keys())

# Convertendo para lista
key_list = list(personal_data.keys())
print("\nLista de chaves:", key_list)

# Iterando sobre as chaves e valores
for key, value in personal_data.items():
    print(f"\n{key}: {value}")

################################################################################################################

# EXERCICIO 2
print('''
      2 - Utilizando o dicionário criado no item 1:
      Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
      Adicione um campo de profissão para essa pessoa;
      Remova um item do dicionário.
      ''')

personal_data.update({'Age' : '29 years old'})

for key, value in personal_data.items():
    print(f"\n{key}: {value}")

print('\n#############################################################################\n')

personal_data.update({'Profession' : 'Businesswoman'})
personal_data['Height'] = 1.72

for key, value in personal_data.items():
    print(f"\n{key}: {value}")

print('\n#############################################################################\n')

del personal_data['Height']
personal_data['Weight'] = ''

for key, value in personal_data.items():
    print(f"\n{key}: {value}")

################################################################################################################

# EXERCICIO 3
print('3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.')

for x in range(1, 6, +1):
    numbers_and_their_squares = {f'Number: {int(x)}':f'Number squared: {int(x*x)}'}

    for key, value in numbers_and_their_squares.items():
        print(f"\n{key} | {value}")

#############################
#OUTRO METODO PARA A QUESTAO#
#############################

numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)

################################################################################################################

# EXERCICIO 4
print('4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.')

profiles = [{'Name':'Zahira','Age':'29 years old','City':'Ajman','Profession' : 'Businesswoman','Height':1.73},
            {'Name':'Aada','Age':'20 years old','City':'Kazan','Profession':'Aeronautical Engineer'},
            {'Name':'Raissa','Age':'27 years old','City':'Oulu','Profession':'Doctor'},
            {'Name':'Sofia','Age':'33 years old','City':'Merida','Profession':'Professional Cook'}
]

profile1 = profiles[1]
check1 = 'key exists' if 'Profession' in profile1 else 'key does not exists'

print(type(profile1))
print(profile1)
print(check1)

################################
#OUTRAS SOLUCOES PARA A QUESTAO#
################################

##########
#METODO 1#
##########
profile2 = profiles[0]

if 'Height' in profile2:
    print('\n\nA chave "Height" existe no dicionário.')
    print(f'{profile2}\n\n')
else:
    print('\n\nA chave "Height" não existe no dicionário.')
    print(f'{profile2}\n\n')


##########
#METODO 2#
##########
profile3 = profiles[2]

check2 = profile3.get('Profession', 'No infortion')
print(check2)  # Saída: Não informada (já que a chave 'profissao' não existe)
print(f'{profile3}\n\n')

##########
#METODO 3#
##########
profile4 = profiles[3]

try:
    check3 = profile4['Profession']
    print(check3)
except KeyError:
    print("A chave 'Profession' não existe.")

################################################################################################################

# EXERCICIO 5
print('5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.')


def count_words(phrase):
    '''
    Args:
    professional_profile: A frase a ser analisada.

    Returns:
    Um dicionário onde as chaves são as palavras e os valores são as suas frequências.
    '''

    # Limpa a frase, removendo pontuação e convertendo para minúsculas
    words = phrase.lower().split()

    # Cria um dicionário para armazenar as frequências
    frequency = {}

    # Itera sobre cada palavra e incrementa a contagem no dicionário
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency

# Exemplo de uso:
phrase = 'Professional Profile: Eu me chamo Aada, sou uma profissional altamente qualificada em projeto, desenvolvimento e análise de aeronaves, com sólidos conhecimentos em aerodinâmica, estruturas e sistemas aeronáuticos. Engenheira aeronáutica especialista em design, desenvolvimento e análise de aeronaves. Graduada em Engenharia Aeronáutica com conhecimentos em aerodinâmica, estruturas e sistemas aeronáuticos.'
result = count_words(phrase)
print(result)


#############################
#OUTRO METODO PARA A QUESTAO#
#############################

frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)
```

#### Docstring

Esta etapa segue a recomendacao para documentar o codigo para um melhor entendimento do que esta sendo realizado em um determinado bloco de codigo.

Logo abaixo, segue o codigo atualizado com docstring adicionados.

```PY
import os

restaurantes = [{'nome':'Praca', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'Italiana', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Arabe', 'ativo':False}]

def exibir_nome_app():
    '''Essa função é responsável em exibir o nome do app'''

    print('''
        Sabor Express      
        ''')

def exibir_opcoes():
    '''Essa função é responsável em exibir os itens disponiveis no menu principal'''

    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado restaurante')
    print('4. Sair\n')

def exibir_subtitulo(texto):
    '''Essa função é responsável em exibir o subtitulo de cada item do menu principal ao acessa-los'''
    
    os.system('clear')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_ao_menu_principal():
    '''Essa função é responsável por retornar ao menu principal'''
    
    input('\nDigite qualquer tecla para voltar ao menu ')
    print()
    main()
    
def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria
    - Ativo

    Output:
    - Adiciona novo restaurante, categoria e estado a lista de restaurante
    '''
    
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_restaurante = input('Digite o nome do restaurante para cadastro: ')
    categoria = input(f'Digite a categoria do restaurante {nome_restaurante}: ')

    dados_restaurante = {'nome':nome_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_restaurante)

    print(f'\nO restaurante {nome_restaurante} foi cadastrado com sucesso\n')

    voltar_ao_menu_principal()

def listar_restaurante():
    '''Essa função é responsável por listar o nome de todos os restaurantes registrados no app'''

    exibir_subtitulo('Listando restaurantes')

    print(f'{' Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status do restaurante')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Essa função é responsável por alternar o estado em que o restaurante se encontra'''

    exibir_subtitulo('Alternando estado restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante nao foi encontrado')

    voltar_ao_menu_principal()

def finalizar_app():
    '''Essa função é responsável por encerrar o app'''

    exibir_subtitulo('Encerrando App')

def opcao_invalida():
    '''Essa função é responsável por informar que dado inserido é uma opção invalida'''

    exibir_subtitulo('Opcao invalida')
    voltar_ao_menu_principal()

def escolher_opcao():
    '''Essa função é responsável em executar a ação de escolher opção do menu principal'''

    try:
        opcao_escolhida = int(input('Escolha uma opcao: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Essa função é a principal do app'''

    os.system('clear')
    exibir_nome_app()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
```