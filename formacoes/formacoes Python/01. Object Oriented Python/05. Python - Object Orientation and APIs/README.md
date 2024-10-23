## Python - avance na Orientacao a Objetos e consuma API

O que sera trabalhado durante o treinamento:

- Heranca
- Polimorfismo e metodo abstrato
- Ambientes virtuais
- Requisicoes, json e arquivos
- FastAPI

&nbsp;
&nbsp;

Para esse estudo continuaremos com o projeto desenvolvido no treinamento **Python: aplicando a Orientação a Objetos**.

### 01. Heranca

Neste capitulo foi criado novas *classes* com seus respectivos arquivos.

Segue a arquitetura do sistema atual com os novos itens em **negrito** e o item alterado em *italico*:

* sabor-express
  * *app.py*
  * modelos
    * **cardapio**
      * **bebida.py**
      * **item_cardapio.py**
      * **prato.py**
    * avaliacao.py
    * restaurante.py

&nbsp;

Com isso, seguiremos com os conteudos de cada arquivo:

&nbsp;

**`sabor-express/modelos/cardapio/item_cardapio.py`**

```PY
class ItemCardapio:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
```
&nbsp;

**`sabor-express/modelos/cardapio/bebida.py`**

```PY
from modelos.cardapio.item_cardapio import ItemCardapio


class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome,preco)
        self._tamanho = tamanho

    def __str__(self):
        return self._nome
```

&nbsp;

**`sabor-express/modelos/cardapio/prato.py`**

```PY
from modelos.cardapio.item_cardapio import ItemCardapio


class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome,preco)
        self._descricao = descricao

    def __str__(self):
        return self._nome
```

&nbsp;

**`sabor-express/app.py`**

```PY
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5, 'grande')
prato_pao = Prato('Pao', 2, 'Melhor pao da cidade')

def main():
    print(bebida_suco)
    print(prato_pao)

if __name__ == '__main__':
    main()
```

&nbsp;

O novo reccurso que trabalhamos entre as classes é a *herança* que possibilita o uso de *atributos* e *métodos* de uma *classe* em outra.

Uma definicao sobre *herança*, é a passada no treinamento da *Alura*, diz o seguinte: '*A herança é um conceito fundamental na programação orientada a objetos (OO) e desempenha um papel crucial no desenvolvimento de software. A importância da *herança* está relacionada à capacidade de criar novas classes reutilizando ou estendendo o comportamento de classes existentes.*'.

&nbsp;

**Herança em Python: Criando Hierarquias de Classes**

***O que é Herança?***

Na programação *orientada a objetos*, a *herança* é um mecanismo que permite que uma *classe* (*classe filha*) herde *atributos* e *métodos* de outra *classe* (*classe pai*). Isso cria uma relação *hierárquica* entre as classes, onde a classe filha é uma especialização da classe pai.

&nbsp;

***Por que usar Herança?***

- **Reutilização de código:** Evita a duplicação de código, pois as **classes filhas** herdam as características da *classe pai*.
- **Organização do código:** Cria uma estrutura *hierárquica* clara, facilitando a compreensão e a manutenção do código.
- **Polimorfismo:** Permite que objetos de diferentes *classes* sejam tratados de forma uniforme, através de *métodos* com o mesmo nome, mas comportamentos diferentes.

&nbsp;

***Como funciona em Python?***

Para criar uma *classe* que *herda* de outra, basta colocar o nome da *classe pai* entre parênteses após o nome da *classe filha*:

```PY
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comer(self):
        print(f"{self.nome} está comendo.")

class Cachorro(Animal):
    def latir(self):
        print("Au au!")

class Gato(Animal):
    def miar(self):
        print("Miau!")
```

Neste exemplo:

- `Animal` é a *classe pai*.
- `Cachorro` e `Gato` são **classes filhas** que *herdam* de `Animal`.
- `Cachorro` e `Gato` podem acessar e utilizar o *método* `comer` da *classe pai*.
- `Cachorro` e `Gato` possuem seus próprios *métodos* específicos (`latir` e `miar`).

&nbsp;

***Sobreescrita de Métodos:***

Uma *classe filha* pode sobrescrever um *método herdado* da *classe pai*, fornecendo uma implementação diferente:

```PY
class Animal:
    def fazer_som(self):
        print("Fazendo um som genérico.")

class Cachorro(Animal):
    def fazer_som(self):
        print("Au au!")
```

&nbsp;

***Método `super()`:***

O *método* `super()` permite acessar *métodos* da *classe pai* a partir da *classe filha*, mesmo que eles tenham sido sobrescritos:

```PY
class Animal:
    def __init__(self, nome):
        self.nome = nome

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca
```

&nbsp;

***Herança Múltipla:***

*Python* suporta *herança* múltipla, ou seja, uma *classe* pode *herdar* de múltiplas *classes pais*:

```PY
class Voador:
    def voar(self):
        print("Estou voando!")

class Nadador:
    def nadar(self):
        print("Estou nadando!")

class Pinguim(Voador, Nadador):
    pass
```

&nbsp;

***Quando usar Herança:***

- **Relação "é um":** Se uma *classe* é um tipo específico de outra *classe* (por exemplo, um cachorro é um animal), a *herança* é adequada.
- **Reutilização de código:** Quando precisa de funcionalidades semelhantes em várias *classes*.
- **Criação de hierarquias:** Para organizar o código em uma estrutura *hierárquica* clara.

&nbsp;

***Quando evitar Herança:***

- **Relação "tem um":** Se uma *classe* possui um *atributo* que é outra classe (por exemplo, um carro tem um motor), a composição é mais adequada.
- **Herança profunda:** *Hierarquias* muito profundas podem tornar o código difícil de entender e manter.

&nbsp;

***Em resumo:***

A *herança* é uma ferramenta poderosa em *Python* que permite criar *classes* mais complexas e reutilizáveis. Ao entender os conceitos de *herança*, sobreescrita de *métodos* e *super*, poderá criar designs de software mais eficientes e bem estruturados.

&nbsp;

**Exercícios**

01. Crie uma Classe Pai (Veiculo): Implemente uma classe chamada Veiculo com um construtor que aceita dois parâmetros, marca e modelo. A classe deve ter um atributo protegido _ligado inicializado como False por padrão.

```PY
class Veiculo1:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False
```

&nbsp;

02. Construa o Método Especial str: Adicione um método especial str à classe Veiculo que retorna uma mensagem formatada com a marca, modelo e o estado de ligado/desligado do veículo.

```PY
class Veiculo2:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f'Marca: {self.marca} | Veiculo {self.modelo} | Status: {status} ({self._ligado})'
```

&nbsp;

03. Crie uma Classe Filha (Carro): Agora, crie uma classe chamada Carro que herda da classe Veiculo. No construtor da classe Carro, inclua um novo atributo chamado portas que indica a quantidade de portas do carro.

```PY
# veiculo3.py

class Veiculo3:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f'Marca: {self.marca} | Veiculo {self.modelo} | Status: {status} ({self._ligado})'
```

```PY
# carro3.py
from veiculo import Veiculo3

class Carro3(Veiculo3):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas
```

&nbsp;

04. Implemente o Método Especial str na Classe Filha: Adicione um método especial str à classe Carro que estenda o método da classe pai (Veiculo) e inclua a informação sobre a quantidade de portas do carro.

```PY
# veiculo4.py

class Veiculo4:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f'Marca: {self.marca} | Veiculo {self.modelo} | Status: {status} ({self._ligado})'
```

```PY
# carro4.py
from veiculo import Veiculo4

class Carro4(Veiculo4):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f'Carro {self.modelo} | Marca: {self.marca} | Portas: {self.portas} | Status: {status} ({self._ligado})'
```

&nbsp;

05. Crie uma Classe Filha (Moto): Similarmente, crie uma classe chamada Moto que também herda de Veiculo. Adicione um novo atributo chamado tipo ao construtor, indicando se a moto é esportiva ou casual.

```PY
# veiculo5.py

class Veiculo5:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f'Marca: {self.marca} | Veiculo {self.modelo} | Status: {status} ({self._ligado})'
```

```PY
# moto5.py
from veiculo import Veiculo5

class Moto5(Veiculo5):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo
```

&nbsp;

06. Implemente o Método Especial str na Classe Filha (Moto): Adicione um método especial str à classe Moto que estenda o método da classe pai (Veiculo) e inclua a informação sobre o tipo da moto.

```PY
# veiculo6.py

class Veiculo6:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f'Marca: {self.marca} | Veiculo {self.modelo} | Status: {status} ({self._ligado})'
```

```PY

# moto6.py
from veiculo import Veiculo6

class Moto5(Veiculo6):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f'Moto {self.modelo} | Marca: {self.marca} | tipo: {self.tipo} | Status: {status} ({self._ligado})'
```

&nbsp;

07. Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no mesmo diretório que suas classes.

```BASH
touch main.py
```

&nbsp;

08. Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto. Em seguida, crie três instâncias de Carro e Moto com diferentes marcas, modelos, quantidade de portas e tipos.

```PY
# main.py
from carro import Carro
from moto import Moto

carro1 = Carro('Chevrolet', 'Corsa', 4)
carro2 = Carro('Ford', 'Focus', 4)
carro3 = Carro('Dodge', 'Viper', 2)

moto1 = Moto('Honda', 'CG 160', 'Casual')
moto2 = Moto('Yamaha', 'Factor 150', 'Casual')
moto3 = Moto('Kawasaki', 'Ninja 400', 'Esportiva')
```

&nbsp;

09. Exiba as Informações: Para cada instância, imprima no console as informações utilizando o método str.

```PY
print(carro1)
print(carro2)
print(carro3)

print(moto1)
print(moto2)
print(moto3)
```

&nbsp;
&nbsp;

### 02. Polimorfismo e metodo abstrato

**Topicos do capitulo:**

- Metodos para adicionar itens
- Refatoracao
- Exibindo o cardapio
- Metodos abstrato
- Polimorfismo

&nbsp;

#### OO Sabor Express

Segue a arquitetura do sistema atual com os itens criados ou alterados:

* sabor-express
  * app.py
  * modelos
    * cardapio
      * bebida.py
      * item_cardapio.py
      * prato.py
    * avaliacao.py
    * restaurante.py

&nbsp;

#### 01. Metodos para adicionar itens

No arquivo `restaurante.py`, adicionamos os *metodos* `adicionar_bebida_cardapio` e `adicionar_prato_cardapio` na *classe* `Restaurante`.
Tambem adicionamos um novo *atributo* `self._cardapio = []` ao *metodo construtor*.
Para finalizarmos, colocamos duas novas *instancias* no arquivo `app.py`.

&nbsp;

**`sabor-express/modelos/restaurante.py`**

```PY
# ... (resto do seu código)

class Restaurante:
    # ... (resto do seu código)

    def __init__(self, nome, categoria):
        # ... (resto do seu código)
        self._cardapio = []

    # ... (resto do seu código)
    
    def adicionar_bebida_cardapio(self, bebida):
        self._cardapio.append(bebida)

    def adicionar_prato_cardapio(self, prato):
        self._cardapio.append(prato)
```

&nbsp;

**`sabor-express/app.py`**

```PY
# ... (resto do seu código)

restaurante_praca.adicionar_bebida_cardapio(bebida_suco)
restaurante_praca.adicionar_prato_cardapio(prato_pao)

# ... (resto do seu código)
```

&nbsp;

#### 02. Refatoracao

A refatoracao feita foi diminuir *metodos* na *classe* `Restaurante`, eliminando os *metodos* `adicionar_bebida_cardapio` e `adicionar_prato_cardapio` para adicionar o *metodo* `adicionar_cardapio`.

&nbsp;

**`sabor-express/modelos/restaurante.py`**

```PY
# ... (resto do seu código)
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    # ... (resto do seu código)

    def adicionar_cardapio(self, item): # Esse método é responsável por adicionar um item ao cardápio do restaurante.
        if isinstance(item, ItemCardapio): # Verificação de Tipo: Antes de adicionar o item ao cardápio, o código verifica se o objeto passado como argumento (item) é uma instância da classe ItemCardapio. Isso garante que apenas objetos do tipo ItemCardapio possam ser adicionados ao cardápio, evitando erros e mantendo a integridade dos dados.
            self._cardapio.append(item) # Se o objeto passado for do tipo ItemCardapio, ele é adicionado a uma lista chamada _cardapio que armazena os itens do cardápio do restaurante.
```

&nbsp;

**Benefícios e Conceitos Utilizados**

- **Polimorfismo:** A verificação `isinstance(item, ItemCardapio)` demonstra o *polimorfismo*. O *método* `adicionar_cardapio` pode aceitar qualquer objeto que seja uma *instância* de `ItemCardapio` ou de uma subclasse de `ItemCardapio`, permitindo flexibilidade na criação de diferentes tipos de itens de cardápio.
- **Tipagem de Dados:** Ao verificar o tipo do objeto, o código garante a integridade dos dados e evita erros. Isso torna o código mais robusto e fácil de manter.
- **Encapsulamento:** O uso do underscore (`_`) no nome do atributo `_cardapio` indica que ele é privado e não deve ser acessado diretamente de fora da *classe*, promovendo o encapsulamento e a proteção dos dados internos da *classe*.

&nbsp;

**`sabor-express/app.py`**

```PY
# ... (resto do seu código)

restaurante_praca.adicionar_cardapio(bebida_suco)
restaurante_praca.adicionar_cardapio(prato_pao)

# ... (resto do seu código)
```

&nbsp;

#### 03. Exibindo o cardapio

Foi criado uma *classe* `exibir_cardapio`, nela usamos o *parametro especial* `self`, como o laco de repeticao `for` e a condicional `if/else`, tambem usou as novas funcoes `enumerate` e `hasattr`.

&nbsp;

**`sabor-express/modelos/restaurante.py`**

```PY
# ... (resto do seu código)

    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preco: R$ {item._preco:.2f} | Descricao: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preco: R$ {item._preco:.2f} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)
```

&nbsp;

**Analisando o Código**

***O Decorador `@property`***

- **O que faz:** Transforma um *método* em uma *propriedade*. Isso significa que pode acessar o *método* como se fosse um *atributo*, sem a necessidade de usar *parênteses*.
- **Por que usar:** Aumenta a legibilidade do código, tornando-o mais parecido com a forma como acessamos *atributos*.
- **Neste caso:** O *método* `exibir_cardapio` está sendo transformado em uma *propriedade*, permitindo que seja acessado como `restaurante.exibir_cardapio`.

***Método `exibir_cardapio`***

- **`print(f'Cardapio do restaurante {self._nome}\n')`:** A primeira linha, imprime o nome do restaurante, usando o atributo `_nome` da *instância*.
- **`for i, item in enumerate(self._cardapio, start=1)`:** O `for` *loop* itera pelos os itens do cardápio (`self._cardapio`), numerando-os a partir de *1*.
- **Verificação do tipo de item:**
    - **`if hasattr(item, 'descricao')`:** Se tiver atributo `descricao`, é considerado um *prato* e a mensagem é formatada com *nome*, *preço* e *descrição*.
    - **`else`**: Caso contrário, é considerado uma *bebida* e a mensagem é formatada com *nome*, *preço* e *tamanho*.
- **Formatação da saída:** As *f-strings* são usadas para formatar as mensagens de forma clara e concisa, com o preço formatado com duas casas decimais.

***Resumo do Funcionamento***

- Ao chamar `restaurante.exibir_cardapio`, o *método* é executado.
- O *método* imprime o nome do *restaurante*.
- Para cada *item no cardápio*, ele verifica se o *item* é um *prato* ou uma *bebida* com base na existência do *atributo descricao*.
- Imprime uma mensagem formatada para cada *item*, mostrando o número, nome, preço e, dependendo do *tipo*, descrição ou tamanho.

&nbsp;

**Novas funcoes usadas no codigo**

***`for i, item in enumerate(self._cardapio, start=1):`***

***`enumerate()`:*** Essa *função* é muito útil quando precisa iterar sobre uma sequência (como uma *lista*, *tupla* ou *string*) e, ao mesmo tempo, ter acesso ao índice de cada elemento. Ela retorna um objeto *enumerador* que gera pares (*índice*, *elemento*) a cada iteração.

- **`i`:** Recebe o *índice* atual do elemento na iteração.
- **`item`:** Recebe o elemento da lista `self._cardapio` na posição correspondente ao índice.
- **`start=1`:** Especifica que a contagem dos índices deve começar em 1, em vez do 0 padrão. Isso significa que o primeiro elemento terá o índice 1, o segundo terá o índice 2, e assim por diante.

&nbsp;

***`if hasattr(item, 'descricao'):`***

***`hasattr()`:*** Essa *função* verifica se um objeto possui um determinado *atributo*. Ela retorna `True` se o objeto tiver o *atributo* especificado e `False` caso contrário.

- **`item`:** O objeto que será verificado.
- **`'descricao':`** O nome do atributo que queremos verificar.

#### 04. Metodos abstrato

Implementado o *metodo abstrado* no arquivo `item_cardapio.py`.

**`sabor-express/modelos/cardapio/item_cardapio.py`**

```PY
from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @abstractmethod
    def aplicar_desconto(self):
        pass
```

&nbsp;

***Analisando o Código Python***

- **`Importação:`** A linha `from abc import ABC, abstractmethod` importa as *classes* `ABC` e o *decorador* `abstractmethod` do *módulo* `abc` *(Abstract Base Class)*, que são essenciais para definir *classes* e *métodos abstratos* em *Python*.
- **Classe abstrata `ItemCardapio`:**
    - Herda da *classe* `ABC`, indicando que é uma *classe abstrata*.
    - Possui um *método construtor* `__init__` que inicializa os *atributos* `_nome` e `_preco` de um item de cardápio.
    - Possui um *método abstrato* `aplicar_desconto`. Esse *método* não tem implementação, apenas define a assinatura.

&nbsp;

***O que esse código significa?***

- A *classe* `ItemCardapio` define um modelo genérico para qualquer item de um cardápio.
- O método `aplicar_desconto` indica que todos os itens de cardápio podem ter um desconto aplicado, mas a forma como esse desconto será calculado e aplicado varia de acordo com o tipo de item (pizza, bebida, etc.).
- As *classes filhas* de `ItemCardapio` (por exemplo, Pizza, Bebida) deverão implementar o *método* `aplicar_desconto` para definir a lógica específica de cálculo de desconto para cada tipo de item.

&nbsp;

***Exemplo de uso***

```PY
class Pizza(ItemCardapio):
    def aplicar_desconto(self):
        # Lógica específica para calcular o desconto de uma pizza
        novo_preco = self._preco * 0.9  # Desconto de 10%
        return novo_preco

class Bebida(ItemCardapio):
    def aplicar_desconto(self):
        # Lógica específica para calcular o desconto de uma bebida
        # ...
```

&nbsp;

***Em resumo:***

O código define uma estrutura para representar itens de um cardápio, onde cada item pode ter um desconto, mas a forma de calcular esse desconto é definida pelas *classes filhas*. Isso torna o código mais flexível e reutilizável, pois permite criar diferentes tipos de itens com suas próprias regras de desconto.

&nbsp;

***Métodos Abstratos e o Código Python***

***O que é um Método Abstrato?***

Em programação *orientada a objetos*, um *método abstrato* é um *método* declarado em uma *classe abstrata*, mas que não possui uma implementação concreta. Ou seja, ele apenas define a assinatura do *método* (nome, parâmetros e tipo de retorno), mas deixa a implementação específica para as *classes filhas*.

&nbsp;

***Características de um Método Abstrato:***

- **Não tem corpo:** A declaração do *método* termina com um ponto e vírgula, sem as chaves que delimitam o corpo de um *método* normal.
- **É precedido pela palavra-chave `abstract`:** Essa palavra-chave indica que o *método* é *abstrato* e não tem implementação na classe pai.
- **Obriga as *classes filhas* a implementarem:** As classes que herdam da *classe abstrata* são obrigadas a implementar o *método abstrato*, cada uma à sua maneira, de acordo com sua lógica específica.

&nbsp;

***Por que usar métodos abstratos?***

- **Abstração:** Permite criar *classes* mais genéricas, definindo uma interface comum para as *classes filhas*.
- **Polimorfismo:** Permite que diferentes *classes filhas* tenham implementações diferentes para o mesmo *método*, tornando o código mais flexível e reutilizável.
- **Hierarquias de classes:** Ajuda a organizar o código em uma hierarquia de *classes*, onde a *classe abstrata* define as características comuns e as *classes filhas* as particularidades.


&nbsp;

#### 05. Polimorfismo

Aplicacao dos metodos `aplicar_desconto` nas classes `Prato` e `Bebidas`, tambem teve a aplicacao do uso do metodo no  arquivo `app.py`.

**`sabor-express/modelos/cardapio/bebida.py`**

```PY
# ... (resto do seu código)

    def aplicar_desconto(self):
        self._preco = self._preco * 0.75
        return self._preco
```

&nbsp;

**`sabor-express/modelos/cardapio/prato.py`**
```PY
# ... (resto do seu código)

    def aplicar_desconto(self):
        self._preco = self._preco * 0.9 
        return self._preco
```

&nbsp;

**`sabor-express/modelos/cardapio/prato.py`**

```PY
bebida_suco.aplicar_desconto()
prato_pao.aplicar_desconto()
```

&nbsp;

***Polimorfismo em Python: Uma Explicação Simples***

***O que é Polimorfismo?***

Em programação *orientada a objetos*, *polimorfismo* significa a capacidade de um objeto assumir muitas formas. Em outras palavras, um mesmo *método* pode se comportar de maneira diferente em diferentes *classes*, dependendo do contexto. Isso torna o código mais flexível e reutilizável.

&nbsp;

***Polimorfismo em Python:***

Em *Python*, o *polimorfismo* é alcançado principalmente através da *herança* e da sobrecarga de *métodos*.

- **Herança:** Quando uma *classe* herda de outra, ela adquire os *métodos* e *atributos* da *classe pai*. No entanto, a *classe filha* pode sobrescrever esses *métodos*, implementando uma lógica diferente.
- **Sobrecarga:** É o processo de criar *métodos* com o mesmo nome, mas com diferentes *parâmetros*, em uma mesma classe ou em classes diferentes.

&nbsp;

***Exemplo Prático:***

Imagine uma *classe* base chamada `Animal` e duas *classes filhas*, `Cachorro` e `Gato`. Ambas as *classes filhas* herdam da *classe* base e possuem um *método* chamado `fazer_barulho()`. No entanto, a implementação desse *método* será diferente para cada classe:

```PY
class Animal:
    def fazer_barulho(self):
        pass

class Cachorro(Animal):
    def fazer_barulho(self):
        print("Au au!")

class Gato(Animal):
    def fazer_barulho(self):
        print("Miau!")
```

Nesse exemplo, o *método* `fazer_barulho()` é *polimórfico*, pois ele se comporta de maneira diferente dependendo do objeto que o chama. Se criar um objeto `cachorro` e chamar o *método* `fazer_barulho()`, ele irá imprimir "Au au!". Se criar um objeto `gato` e chamar o mesmo *método*, ele irá imprimir "Miau!".

&nbsp;

***Por que usar Polimorfismo?***

- **Reutilização de código:** Ao criar uma *classe* base, pode definir *métodos* comuns que serão herdados por todas as *classes filhas*.
- **Flexibilidade:** O *polimorfismo* permite que você trate *objetos* de diferentes *classes* de forma uniforme, tornando o código mais flexível e fácil de manter.
- **Abstração:** O *polimorfismo* ajuda a criar abstrações mais poderosas, permitindo que concentre na interface dos *objetos*, em vez de suas implementações específicas.

&nbsp;

***Outro Exemplo: Formas Geométricas***

```PY
class Forma:
    def area(self):
        pass

class Retangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14159 * self.raio**2

```

Neste exemplo, o *método* `area()` é *polimórfico*. A implementação específica do *método* `area()` varia dependendo se o *objeto* é um retângulo ou um círculo.

&nbsp;

***Em resumo:***

O *polimorfismo* é uma característica fundamental da programação *orientada a objetos* que permite escrever código mais flexível, reutilizável e fácil de entender. Ao entender o *polimorfismo*, estará mais preparado para criar programas mais robustos e escaláveis.


**Exercícios**

01. Crie uma classe chamada Veiculo com um método abstrato chamado ligar.

```PY
from abc import ABC, abstractmethod

class Veiculo1:
    @abstractmethod
    def ligar(self):
        pass
```

&nbsp;

02. No mesmo arquivo, crie um construtor para a classe Veiculo que aceita os parâmetros marca e modelo.

```PY
from abc import ABC, abstractmethod

class Veiculo2:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @abstractmethod
    def ligar(self):
        pass
```

&nbsp;

03. Crie uma nova classe chamada Carro que herda da classe Veiculo.

```PY
from abc import ABC, abstractmethod

class Veiculo3:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @abstractmethod
    def ligar(self):
        pass

class Carro3(Veiculo3):
    pass
```

&nbsp;

04. No construtor da classe Carro, utilize o método super() para chamar o construtor da classe pai e atribua o atributo específico cor à classe filha.

```PY
from abc import ABC, abstractmethod

class Veiculo4:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @abstractmethod
    def ligar(self):
        pass

class Carro4(Veiculo4):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor
```

&nbsp;

05. Em um arquivo chamado main.py, importe a classe Carro.

```BASH
touch main.py
```

**`main.py`**

```PY
from veiculo import Carro
```

&nbsp;

06. No arquivo main.py, instancie três objetos da classe Carro com diferentes características, como marca, modelo e cor.

**`main.py`**

```PY
from veiculo import Carro

carro1 = Carro('Chevrolet', 'Corsa', 'prata')
carro2 = Carro('Ford', 'Focus', 'preto')
carro3 = Carro('Dodge', 'Viper', 'branco')

print(f"Carro 1: {carro1.marca} {carro1.modelo}, Cor: {carro1.cor}")
print(f"Carro 2: {carro2.marca} {carro2.modelo}, Cor: {carro2.cor}")
print(f"Carro 3: {carro3.marca} {carro3.modelo}, Cor: {carro3.cor}")
```

&nbsp;
&nbsp;
