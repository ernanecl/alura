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

#### Dica

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
