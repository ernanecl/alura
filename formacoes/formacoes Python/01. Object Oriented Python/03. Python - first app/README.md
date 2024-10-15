### Python - primeiro app

#### App Sabor Express

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

#### Exercicios:

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