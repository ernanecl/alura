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

Segue a arquitetura do sistema atual com os novos itens em negrito e o item alterado em italico:

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

**item_cardapio.py**

```PY
class ItemCardapio:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
```
&nbsp;

**bebida.py**

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

**prato.py**

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

**app.py**

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

- **Reutilização de código:** Evita a duplicação de código, pois as *classes filhas* herdam as características da *classe pai*.
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
- `Cachorro` e `Gato` são *classes filhas* que *herdam* de `Animal`.
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
