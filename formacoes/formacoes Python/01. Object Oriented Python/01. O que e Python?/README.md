### O que é Python? — um guia completo para iniciar nessa linguagem de programação

```https://www.alura.com.br/artigos/python```

#### Os tipos de dados em Python

Tipos de dados padrao em `Python`:

1. inteiro (`int`) - exemplo: 1
2. ponto flutuante ou decimal (`float`) - exemplo: 1.2
3. tipo complexo (`complex`) - exemplo: 6h
4. string (`str`) - exemplo: hello
5. boolean (`bool`) - exemplo: ```PY true/false```
6. lista (`list`) - exemplo: ['Monica','Ana','Bruna',Alice']
7. tupla (`tuple`) - exemplo: (90, 79, 54, 37)
8. dicionario (`dic`) - exemplo: ```PY{`Camila`:1.65, `Larissa`:1.60, `Raissa`:1.70}```


Ver qual o tipo de variavel:

```PY
idade = {‘Catarina‘:35, ‘Elizabeth’:28, ‘Caitlyn’:24}”

print(type(idade))

<class ‘dict’>
```

Alterar o tipo de variavel:

```PY
# Float para String

#Antes de converter
altura=1.55
print(type(altura)

#Fazendo a conversão
altura = str(altura)”

#Depois da conversão
print(type(altura) 
print(altura)

<class ‘float’>
<class ‘str’>
 1.55
```

#### Estruturas condicionais em Python: if, elif e else

Uilizados para controlar o fluxo de execução de programas para qual bloco de código será executado a partir de uma determinada condição.

Em Python utilizando as estruturas `if`, `elif` e `else`.

Modelo de estruturas condicionais como referencia:

```PY
media = 6

if media < 5
print(“Você foi reprovado”)

elif media > 5 
media < 7
    print(“Você fará a recuperação”)

else:
    print(“Você foi aprovado”)
```

#### Estrutura Match

A partir do `Python 3.10`, podemos utilizar a estrutura `match`, e' mais organizada e legível para lidar com múltiplas condições.

Permite combinar padrões e executar o bloco de código correspondente ao primeiro padrão que for verdadeiro.

Modelo de estruturas condicionais como referencia:

```PY
media = 6

match media:
    case media if media < 5:
        print("Você foi reprovado")
    case media if 5 <= media < 7:
        print("Você fará a recuperação")
    case media if media >= 7:
        print("Você foi aprovado")
```

#### Estruturas de repetição Python: for e while

Utilizadas em um bloco de código seja executado várias vezes. Em Python existem duas formar: `while` ou `for`.

`for` é utilizado quando queremos iterar sobre um bloco de código por um determinado número de vezes.

Exemplo codigo:

```PY
for i in range(1,10):
    print(i)
```

Saida:
```PY
1
2
3
4
5
6
7
8
9
```

`while` é quando executamos o codigo até que uma condição seja satisfeita.

É necessário que uma expressão `booleana` seja verdadeira. A partir do momento que ela se tornar falsa, o while para de executar.

```PY
gastos=0
valor_gasto=0
while gastos < 1000
    valor_gasto = int(input(“Digite o valor gasto”))
    gastos = gastos + valor_gasto
print(gastos)

Digite o valor do novo gasto 20
Digite o valor do novo gasto 500
Digite o valor do novo gasto 480
1000
```

#### Módulos e bibliotecas em Python

De acordo com a documentacao da linguagem, o modulo é definido como: "Um módulo é um arquivo Python contendo definições e instruções."

O nome do arquivo é o módulo com o sufixo .py adicionado e o nome do módulo (string) está disponível na variável global name.

O conjunto dos módulos (arquivos) pode ser chamado de pacote ou biblioteca.

Os pacotes, segundo a documentação: “São uma maneira de estruturar namespaces para módulos Python utilizando a sintaxe de ‘nomes pontuados’ (dotted names).”

Um namespace é uma coleção de nomes simbólicos, atualmente definidos junto com informações sobre o objeto ao qual cada nome faz referência.

Pode pensar em um namespace como um dicionário, no qual as chaves são os nomes dos objetos e os valores são os próprios objetos. Cada par chave-valor mapeia um nome para seu objeto correspondente.

Exemplo:

- Criaremos um módulo que representa um círculo. Para isso, geramos um arquivo chamado `circulo.py` com o seguinte conteúdo:

```PY
PI = 3.14159

def area(raio):
  """Calcula a área de um círculo.

  Args:
    raio: O raio do círculo.

  Returns:
    A área do círculo.
  """
  return PI * (raio ** 2)

def comprimento_circunferencia(raio):
  """Calcula o comprimento da circunferência de um círculo.

  Args:
    raio: O raio do círculo.

  Returns:
    O comprimento da circunferência.
  """
  return 2 * PI * raio
```

Para usarmos o modulo, vamos importar seus dados para outro arquivo (`out_circulo.py`), com o seguinte codigo:

```PY
import circulo 

print(circulo.Pi)
print(circulo.area(5))
print(circulo.comprimento_circunferencia(5))
```

Para importar uma funcao mais especifica, podemos usar atraves do comando `from circulo import area`.


#### PythonPath

Utilizamos os módulos importados no mesmo nível do diretório daqueles que os importavam, em outros casos, o interpretador `Python` busca por módulos em outros diretórios.

Quando uma instrução `import` é executada, o interpretador primeiramente verifica se o módulo requerido está no diretório atual.

Caso contrário, a busca se estenderá ao `PYTHONPATH`. O `PYTHONPATH` é uma lista de diretórios na qual o interpretador `Python` irá buscar por módulos para importação.

Um exemplo de módulo mais utilizado é o `datetime`.

Para aprender mais sobre o módulo `datetime`, consulte o artigo [Python datetime: Como faço para definir data e hora em Python?](https://www.alura.com.br/artigos/lidando-com-datas-e-horarios-no-python)


#### PyPI

O `Python Package Index`, abreviado como `PyPI` é o repositório de software oficial de terceiros para `Python`.

De acordo com a documentação oficial:

“`PyPI` é o Índice de Pacotes padrão para a comunidade `Python`. Está aberto a todos os desenvolvedores `Python` para consumir e distribuir suas distribuições.”

Para saber mais sobre o `PyPI`, consulte o artigo [Como publicar seu código Python no PyPI](https://www.alura.com.br/artigos/como-publicar-seu-codigo-python-no-pypi)


#### Ambientes virtuais

Normalmente, aplicações em `Python` usam pacotes e módulos que não vêm como parte da instalação padrão.

Algumas aplicações podem precisar de uma versão específica de uma biblioteca caso seja necessária a resolução de algum problema em particular, ou ainda, se o software foi desenvolvido utilizando-se de uma versão obsoleta da interface da biblioteca.

A solução para esse problema é criar um ambiente virtual, uma árvore de diretórios que contenha uma instalação Python para uma versão particular do Python, além de uma série de pacotes adicionais.

Para aprender mais sobre esses ambientes, leia o artigo [Python: Venv e Poetry para criar ambientes virtuais.](https://www.alura.com.br/artigos/ven-poetry-no-python)


#### Python e Inteligência Artificial

`Python` é uma das linguagens de programação mais versáteis e poderosas para trabalhar com `inteligência artificial (IA)`.

Uma das vantagens de usar `Python` para `IA` é a disponibilidade de bibliotecas que facilitam a construção de modelos de aprendizado de máquina e deep learning. Algumas das bibliotecas mais populares incluem:

- `Scikit-learn`: ideal para tarefas de aprendizado de máquina tradicionais, como `classificação`, `regressão` e `clustering`. É fácil de usar e possui uma vasta gama de algoritmos.
- `TensorFlow` e `Keras`: utilizadas principalmente para `deep learning`. `TensorFlow`, desenvolvido pelo `Google`, é uma biblioteca para construir e treinar `redes neurais`.

`Keras` oferece uma interface de alto nível que facilita o desenvolvimento de modelos complexos. A biblioteca pode ser executada em conjunto com o `Tensorflow`.

- `PyTorch`: desenvolvido pelo `Facebook`, é outra biblioteca popular para `deep learning`, especialmente em pesquisa acadêmica. É conhecido pela sua flexibilidade e facilidade de uso.

Além de criar seus próprios modelos, também pode utilizar `APIs` de empresas especializadas em `IA` para acessar recursos avançados. Um exemplo é a `OpenAI`, que oferece uma `API` para `IA generativa`.

A `API` da `OpenAI` permite integrar capacidades avançadas de processamento de `linguagem natural (NLP)` em suas aplicações. Com a `API`, é possível realizar tarefas como geração de texto, tradução, resumo e muito mais, utilizando modelos treinados por especialistas em `IA`.


#### Bibliotecas e Frameworks mais utilizados

- `NumPy`: para computação numérica, permite a manipulação de arrays multidimensionais e funções matemáticas de alto desempenho.

- `Pandas`: para manipulação e análise de dados, fornece estruturas de dados flexíveis e eficientes para trabalhar com dados tabulares.

- `Matplotlib`: para criação de gráficos e visualizações de dados em `Python`.

- `TensorFlow`: `framework` de aprendizado de máquina de `código aberto` para desenvolver e treinar modelos de `aprendizado profundo`.

- `Django`: `framework web` de alto nível que facilita o desenvolvimento rápido e seguro de aplicativos `web`.

- `Flask`: `framework web` leve e flexível para a criação de aplicativos `web` em `Python`.

- `SciPy`: biblioteca para computação científica que fornece funcionalidades para otimização, interpolação, processamento de sinais, álgebra linear e muito mais.

- `Scikit-learn`: para aprendizado de máquina, fornece algoritmos de classificação, regressão, clustering e pré-processamento de dados.

- `BeautifulSoup`: para extração de dados de páginas `web`, permitindo a raspagem de dados de forma fácil e eficiente.

- `Requests`: para fazer requisições HTTP de maneira simples e fácil, muito útil para acessar `APIs` e baixar conteúdo da `web`.

- `Pillow`: para processamento de imagens, oferece funcionalidades para abrir, manipular e salvar muitos formatos de arquivos de imagem.

- `Asyncio`: para programação assíncrona, permite escrever código concorrente usando a estrutura de `async/await`, facilitando a execução de operações de `I/O` de forma eficiente.

- `Tkinter`: biblioteca padrão do `Python` para a criação de interfaces gráficas (`GUI`), permitindo o desenvolvimento de aplicativos desktop com uma variedade de `widgets`.

- `FastAPI`: é especificamente projetado para a construção de `APIs` com `Python`, oferecendo recursos e benefícios adicionais para aumentar a eficiência do desenvolvimento.


É importante lembrar que um `framework Python` é um conjunto de pacotes e módulos que tornam a programação mais fácil e rápida.

Para saber ainda mais sobre o assunto, leia o artigo sobre [frameworks](https://www.alura.com.br/artigos/framework-o-que-e-pra-que-serve-essa-ferramenta).

