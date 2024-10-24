## Python - aplicando a Orientação a Objetos

O que sera trabalhado durante o treinamento:

- Introdução: orientação a objetos (OO)
- Conceito de classe
- Atributos de instância
- Métodos

&nbsp;
&nbsp;

Para dar inicio ao treinamento, precisa organizar o ambiente para realizar as atividades.

Iniciamos criando um *diretorio* `oo-sabor-express`, depois dentro desse mesmo *diretorio* criamos mais um *diretorio* chamado `modelos`.

Apos a conclusao, criar um arquivo chamado `restaurante.py` para iniciar as atividades.

&nbsp;
&nbsp;

### 01 - Classes

**Topicos do capitulo:**

- Classes
- Atributos de instancia
- Funcoes

&nbsp;

#### OO Sabor Express

Versao final do *codigo* do capitulo:

```PY
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_pizza = Restaurante()

restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

restaurantes = [restaurante_praca, restaurante_pizza]

print(restaurantes)
print(dir(restaurantes))
print(vars(restaurantes[0]))
```

Durante o capitulo, trabalha com a criacao de um novo arquivo chamado `restaurante.py`, nele trabalhou com as funcionalidades basicas sobre **classes**.

&nbsp;

#### Classe

`Classe` é como um molde para criar objetos, a base da programação orientada a objetos em *Python*. Elas proporcionam uma forma eficiente e organizada de modelar o mundo real em seus programas.

Conceitos-chave:

- **Objeto**: Uma instância de uma classe. É a representação real de um objeto no seu programa.
- **atributos**: São as características de um objeto, como o nome, a idade, a cor, etc. Em uma classe, os *atributos* são definidos como variáveis.
- **métodos**: São as ações que um objeto pode realizar, como calcular, comparar, imprimir, etc. Em uma classe, os *métodos* são definidos como funções.

&nbsp;

***Exemplo***

```PY
class Cachorro:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def latir(self):
        print("Au au!")

# Criando objetos (instâncias da classe)
cachorro1 = Cachorro("Rex", "Labrador")
cachorro2 = Cachorro("Bella", "Poodle")

# Acessando atributos
print(cachorro1.nome)  # Saída: Rex
print(cachorro2.raca)  # Saída: Poodle

# Chamando métodos
cachorro1.latir()  # Saída: Au au!
```

- Classe `Cachorro`: Define um modelo para criar objetos do tipo cachorro.
- `__init__`: É um *método* especial chamado construtor. Ele é executado automaticamente quando um novo objeto da classe é criado. Neste caso, ele inicializa os *atributos* nome e raca do objeto.
- `latir`: É um *método* que define a ação de latir.
- Objetos `cachorro1` e `cachorro2`: São duas instâncias da classe Cachorro, cada uma com seus próprios *atributos*.

&nbsp;

***Por que usar classes?***

- **Organização**: Agrupa dados (*atributos*) e funcionalidades (*métodos*) relacionados.
- **Reutilização**: Permite criar múltiplos objetos com a mesma estrutura.
- **Abstração**: Esconde a complexidade interna dos objetos, expondo apenas as interfaces necessárias.
- **Herança**: Permite criar novas classes a partir de classes existentes, reutilizando código e criando hierarquias de classes.
- **Polimorfismo**: Permite que objetos de diferentes classes sejam tratados de forma uniforme.

&nbsp;

#### Tópicos para explorar:

**Herança**: Como criar novas classes a partir de classes existentes.
**Polimorfismo**: Como tratar objetos de diferentes classes de forma uniforme.
**Encapsulamento**: Como esconder os detalhes internos de uma classe.
**métodos especiais**: *métodos* como `__str__`, `__repr__`, `__eq__`, etc.

&nbsp;

#### *dir()* e *vars()*

As funções `dir()` e `vars()` permitem trabalhar com os *atributos* e *métodos* de objetos, especialmente quando se trabalha com classes.

***dir()***

- **Retorna**: Uma lista de strings contendo os nomes de todos os *atributos* e *métodos* de um objeto, incluindo aqueles herdados de classes-pai.
- **Alcance**: Vai além dos *atributos* definidos diretamente no objeto, exibindo também *atributos* de classes e *métodos* especiais (como __init__, __str__, etc.).
- **Uso**:
    - **Exploração**: Para descobrir quais *atributos* e *métodos* um objeto possui.
    - **Depuração**: Para verificar se um *atributo* está sendo definido corretamente.
    - **Introspeção**: Para entender a estrutura de um objeto.

&nbsp;

***Exemplo***

```PY
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

pessoa1 = Pessoa("Alice", 30)
print(dir(pessoa1))
```

&nbsp;

A saída de `dir(pessoa1)` lista os *atributos* definidos na classe como `nome`, `idade`, `cumprimentar`, além de outros *atributos* e *métodos* herdados da *classe* base `object`.

***vars()***

- **Retorna**: Um dicionário que mapeia os nomes dos *atributos* de um objeto aos seus valores correspondentes.
- **Alcance**: Se limita aos *atributos* definidos diretamente no objeto, não incluindo *atributos* de classes ou *métodos* especiais.
- **Uso**:
    - **Acesso aos valores**: Para obter os valores dos *atributos* de um objeto de forma direta.
    - **Modificação**: Para modificar os valores dos *atributos* de um objeto.

&nbsp;

***Exemplo:***

```PY
print(vars(pessoa1))
```

A saída de `vars(pessoa1)` será um ***dicionário*** como `{'nome': 'Alice', 'idade': 30}`.

&nbsp;

***Diferenças e Quando Usar Cada Uma***

| **Característica** | **dir()** | **vars()**
|---|---|---|
| *Tipo de retorno* | Lista de strings | Dicionário
| *Alcance* | Todos os *atributos* (incluindo herdados) | Apenas *atributos* definidos diretamente
| *Uso principal* | Exploração, depuração | Acesso e modificação de *atributos*


- Use `dir()` quando quiser obter uma visão geral completa dos *atributos* e *métodos* de um *objeto*, incluindo aqueles *herdados*.
- Use `vars()` quando precisar acessar ou modificar os valores dos *atributos* de um *objeto* de forma direta.

&nbsp;

**Exercicios**


01. Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante."

```PY

class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_pizza = Restaurante()

restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'

restaurantes = [restaurante_praca, restaurante_pizza]

print(restaurantes)
print(dir(restaurantes))
print(vars(restaurantes[0]))
```

&nbsp;

02. Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.")

```PY
nome_do_restaurante = restaurante_praca.nome
print(nome_do_restaurante)
```

&nbsp;

03. Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.")

```PY
check1 = 'Restaurante esta ativo' if restaurante_praca.ativo == True else 'Nao esta ativo'
print(check1)
```

- OUTRO METODO PARA A QUESTAO

```PY
if restaurante_praca.ativo:
    print('O restaurante está ativo.')
else:
    print('O restaurante está inativo.')
```

&nbsp;

04. Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.")

```PY
categoria = Restaurante()
print(Restaurante.categoria)
```

&nbsp;

- OUTRO METODO PARA A QUESTAO#

```PY
categoria1 = Restaurante.categoria
print(categoria1)
```

&nbsp;

05. Altere o valor do atributo nome para 'Bistrô'.")

```PY
restaurante_praca.nome = 'Bistrô'
print(restaurante_praca.nome)
```

&nbsp;

06. Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.")

```PY
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

print(restaurante_pizza.nome)
print(restaurante_pizza.categoria)
```

&nbsp;

07. Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.")

```PY
check2 = f'O restaurante {restaurante_pizza.nome} é categoria Fast Food' if restaurante_pizza.categoria == 'Fast Food' else f'O restaurante {restaurante_pizza.nome} NAO é categoria Fast Food'
print(check2)
```

- OUTRO METODO PARA A QUESTAO

```PY
if restaurante_pizza.categoria == 'Fast Food':
    print('A categoria é Fast Food.')
else:
    print('A categoria não é Fast Food.')
```

&nbsp;

08. Mude o estado da instância restaurante_pizza para ativo.

```PY
print(f'O restaurante {restaurante_pizza.nome} esta com estado ativo como {restaurante_pizza.ativo}')

if restaurante_pizza.ativo == False:
    restaurante_pizza.ativo = True
    print(f'Agora o restaurante {restaurante_pizza.nome} esta com estado ativo como {restaurante_pizza.ativo}')
else:
    print(f"O restaurante {restaurante_pizza.nome} já está ativo")
```

- OUTRO METODO PARA A QUESTAO

```PY
restaurante_pizza.ativo = True
```

&nbsp;

09. Imprima no console o nome e a categoria da instância restaurante_praca.")

```PY
print(restaurante_praca.nome)
print(restaurante_praca.categoria)
```
- OUTRO METODO PARA A QUESTAO

```PY
print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')
```
&nbsp;
&nbsp;

### 02 - Construtor e instanciando objetos

**Topicos do capitulo:**

- Construtor
- Metodos especiais
- Criando metodos

&nbsp;

#### OO Sabor Express

Versao final do *codigo* do capitulo:

```PY
class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

restaurante_praca = Restaurante('Praca', 'Arabe')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')


Restaurante.listar_restaurantes()
```

Durante o capitulo, trabalha com metodos especiais `__init__` e `__str__`, alem de criar o proprio metodo.

&nbsp;

#### Construtor e outros metodos

***O Método init: O Construtor da Classe***

Em *Python*, o *método* `__init__` desempenha a funcao fundamental na criação de objetos a partir de uma classe.

Frequentemente chamado de *construtor*, pois é executado automaticamente quando uma nova *instância* (*objeto*) da *classe* é criada.

&nbsp;

***Qual a sua função principal?***

- **Inicializar atributos**: O `__init__` é utilizado para atribuir valores iniciais aos *atributos* de um *objeto*. Esses atributos definem as características e o estado de cada *instância* da *classe*.
- **Realizar outras tarefas de inicialização**: Além de atribuir valores, o `__init__` pode ser usado para realizar outras operações necessárias no momento da criação do *objeto*, como conectar a um *banco de dados*, carregar configurações, etc.

&nbsp;

***Exemplo***

```PY
class Cachorro:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca
        self.energia = 100

# Criando um objeto da classe Cachorro
meu_cachorro = Cachorro("Rex", "Labrador")
```

Neste exemplo, o *método* `__init__` recebe os parâmetros nome e raca e os atribui aos *atributos* correspondentes do objeto `meu_cachorro`. O atributo energia também é inicializado com o valor 100.

&nbsp;

***O self: Referência à Instância Atual***

O `self` é um parâmetro especial que é passado implicitamente para todos os *métodos* de uma *classe*, incluindo o `__init__`. Ele representa a instância atual da classe, ou seja, o objeto específico que está sendo manipulado.

&nbsp;

***Para que serve o `self`?***

- **Acessar atributos**: O `self` é usado para acessar e modificar os atributos de um objeto dentro de um método. Por exemplo, `self.nome` acessa o atributo nome da *instância* atual.
- **Chamar outros métodos**: O `self` também pode ser usado para chamar outros *métodos* da mesma *classe*.

&nbsp;

***Exemplo***

```PY
class Cachorro:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca
        self.energia = 100

    def latir(self):
        print(f"{self.nome} está latindo!")

meu_cachorro = Cachorro("Rex", "Labrador")
meu_cachorro.latir()  # Saída: Rex está latindo!
```

Neste exemplo, o *método* `latir` usa `self.nome` para acessar o nome do cachorro e imprimir a mensagem correspondente.

&nbsp;

***Por que usar self?***

- **Clareza**: O `self` torna explícito que estamos acessando *atributos* ou *métodos* de uma *instância* específica.
- **Evita confusões**: Ao usar `self`, evita conflitos entre nomes de variáveis locais e *atributos* da *classe*.

&nbsp;

***O Método `__str__` em Python: Uma Representação Amigável dos Objetos***

O *método* `__str__` em *Python* é um *método* especial que retorna uma representação em *string* de um *objeto*.

Quando imprimir um *objeto* ou convertê-lo para uma *string*, o *Python* chama automaticamente este método para obter a representação a ser exibida.

&nbsp;

***Por que usar o __str__?***

- **Leiturabilidade**: Ao personalizar o *método* `__str__`, pode controlar como os *objetos* de sua *classe* são exibidos, tornando a saída mais clara e concisa para o usuário.
- **Depuração**: Durante o desenvolvimento, o *método* `__str__` pode ser muito útil para inspecionar o estado de um *objeto* e identificar possíveis problemas.
- **Interoperabilidade**: Ao definir um *método* `__str__` adequado, facilita a integração de seus objetos com outras ferramentas e bibliotecas que trabalham com *strings*.

&nbsp;

***Como funciona:***

- **Método especial**: O __str__ é um método "mágico" ou "dunder" (double underscore), o que significa que ele tem um significado especial para o interpretador Python.
- **Retorno**: O método deve retornar uma string que representa o objeto de forma clara e concisa.
- **Chamada automática**: Quando você tenta imprimir um objeto usando a função print() ou o operador str(), o Python chama o método __str__ do objeto automaticamente.

&nbsp;

***Comparação com `__repr__`:***

`__str__`: Destinado a fornecer uma representação amigável ao usuário, como se fosse para ser exibida em um *console* ou *log*.
`__repr__`: Destinado a fornecer uma representação não ambígua do *objeto*, ideal para depuração e reprodução do *objeto*. Geralmente é mais detalhado e pode incluir informações técnicas.

&nbsp;

***Quando usar `__str__` e `__repr__`?***

`__str__`: Para a maioria dos casos, quando você precisa de uma representação concisa e legível para o usuário final.
`__repr__`: Para depuração, geração de documentação ou quando você precisa de uma representação completa e inequívoca do *objeto*.

&nbsp;

***Exemplo com `__repr__`:***

```PY
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"Pessoa: {self.nome}, {self.idade} anos"

    def __repr__(self):
        return f"Pessoa(nome='{self.nome}', idade={self.idade})"

pessoa1 = Pessoa("Sofia", 30)
print(pessoa1)  # Saída: Pessoa: Sofia, 30 anos
print(repr(pessoa1))  # Saída: Pessoa(nome='Sofia', idade=30)
```

&nbsp;

**Exercicios**


01. Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.')

```PY
class Carro:
    
    carros = []

    def __init__ (self, nome, modelo, cor, ano):
        self.nome = nome
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        Carro.carros.append(self)

    def listar_carros():
        for carro in Carro.carros:
            print(f'nome: {carro.nome} \nmodelo: {carro.modelo} \ncor: {carro.cor} \nano: {carro.ano}')

carro1 = Carro('Civic','Sedan','Preto','2017')
Carro.listar_carros()
```

&nbsp;

02. Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.')

```PY
class Restaurante0:
    nome = ''
    categoria = ''
    ativo = False
    nota = int
    ano = int

restaurante0 = Restaurante0()

restaurante0.nome = 'Comida Mineira'
restaurante0.categoria ='Mineiro'
restaurante0.nota = 4.3
restaurante0.ano = 1873

restaurantes0 = [restaurante0]

print(restaurantes0)
print(dir(restaurantes0))
print(vars(restaurantes0[0]))
print(vars(restaurante0))
```

&nbsp;

03. Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.')

```PY
class Restaurante1:
    restaurantes = []

    def __init__(self, nome, categoria, nota, ano):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.nota = nota
        self.ano = ano
        Restaurante1.restaurantes.append(self)

    def listar_restaurantes():
        for restaurante in Restaurante1.restaurantes:
            print(f'\nnome: {restaurante.nome} \ncategoria: {restaurante.categoria} \nativo: {restaurante.ativo} \nnota: {restaurante.nota} \nano: {restaurante.ano}')

restaurante1 = Restaurante1('Santa Marmita', 'Fast Food','4.5 estrelas','1989')

Restaurante1.listar_restaurantes()
```

&nbsp;

04. Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.')

```PY
class Restaurante2:
    restaurantes = []

    def __init__(self, nome, categoria, nota, ano):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.nota = nota
        self.ano = ano
        Restaurante2.restaurantes.append(self)

    def __str__(self):
        return f'\nnome: {self.nome} \ncategoria: {self.categoria} \nativo: {self.ativo} \nnota: {self.nota} \nano: {self.ano}'

restaurante2 = Restaurante2('Bora comer', 'Brasileira','4.5 estrelas','1989')

print(restaurante2)
```

&nbsp;

05. Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.')

```PY
class Cliente:
    clientes = []

    def __init__(self, nome, idade, cidade, profissao):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.profissao = profissao
        
        Cliente.clientes.append(self)

    def listar_clientes():
        for cliente in Cliente.clientes:
            print(f'\nnome: {cliente.nome} \ncategoria: {cliente.idade} \nativo: {cliente.cidade} \nnota: {cliente.profissao}')

cliente1 = Cliente('Zahira', '29 years old', 'Ajman', 'Businesswoman')
cliente2 = Cliente('Aada', '20 years old', 'Kazan', 'Aeronautical Engineer')
cliente3 = Cliente('Raissa', '27 years old', 'Oulu', 'Doctor')
cliente4 = Cliente('Sofia', '33 years old', 'Merida', 'Professional Cook')

Cliente.listar_clientes()
```

&nbsp;
&nbsp;

### 03 - Property e metodos de classe

**Topicos do capitulo:**

- Property
- Aprofundando em propriedades
- Metodos de classe

&nbsp;

#### OO Sabor Express

Versao final do *codigo* do capitulo:

```PY
class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | Status')

        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧ ativo' if self._ativo else '☐ ativo'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante('Praca', 'Arabe')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

# restaurante_praca.alternar_estado()
# restaurante_praca._nome = 'praca 2.0'

Restaurante.listar_restaurantes()
```

Durante o capitulo, trabalha com os recursos `@property`, `self._attribute`, `@classmethod`, `cls` e construcao do proprio *metodo*.

&nbsp;

#### Property e self._attribute

**Entendendo self._ativo e @property no código**

&nbsp;

***`self._ativo`***

- **O que é:** É um *atributo* da *classe Restaurante* que indica se o restaurante está ativo ou não.
- **Por que o underline?** O *underline (_)* antes do nome do *atributo* é uma convenção em *Python* para indicar que o *atributo* é *privado* ou *protegido*, ou seja, não é destinado a ser acessado diretamente de fora da classe. Essa convenção ajuda a evitar modificações acidentais no estado interno do objeto.
- **Por que usar um atributo privado?** Ao encapsular o estado do *objeto* (se o restaurante está ativo ou não) dentro de um *atributo privado*, garante que as modificações nesse estado sejam feitas de forma controlada, através de *métodos específicos da classe*. Isso torna o seu código mais seguro e fácil de manter.

&nbsp;

***`@property`***

- **O que é:** É um decorador em *Python* que permite que um *método* seja acessado como se fosse um *atributo*.
- **Qual a sua função?** No seu código, o decorador `@property` transforma o *método ativo* em uma propriedade. Isso significa que você pode acessar o valor desse *atributo* usando a sintaxe `restaurante.ativo`, mas na verdade, o que está acontecendo por trás das cortinas é uma chamada ao *método ativo*.
- **Por que usar @property?**
    - **Encapsulamento:** Permite ocultar a implementação interna do *atributo*, oferecendo uma interface mais limpa para o usuário da *classe*.
    - **Validação:** Você pode adicionar lógica de validação dentro do *método ativo* para garantir que o valor retornado seja sempre válido.
    - **Cálculos:** Permite que calcule o valor do *atributo* dinamicamente, em vez de armazená-lo diretamente.

&nbsp;

***Como funciona o código:***

- **Atributo privado:** O atributo `_ativo` armazena o estado real do restaurante (*True* ou *False*).
- **Propriedade ativo:** A propriedade *ativo* retorna uma *string* ('*ativo*' ou '*desativo*') com base no valor de `_ativo`. Essa *string* é mais amigável para o usuário do que um valor *booleano*.
- **Método `listar_restaurantes`:** Esse *método* itera sobre a *lista de restaurantes* e imprime informações sobre cada um, incluindo o *status* (*ativo* ou *desativo*) usando a propriedade *ativo*.

&nbsp;

***Benefícios dessa abordagem:***

- **Leiturabilidade:** O código fica mais fácil de entender, pois o status do restaurante é representado por uma string clara ('ativo' ou 'desativo').
- **Flexibilidade:** Você pode adicionar mais lógica ao *método ativo* no futuro, como por exemplo, verificar se o restaurante está aberto em um determinado horário.
- **Manutenção:** Ao encapsular o estado do objeto, você facilita a manutenção do código, pois as mudanças no comportamento do atributo ativo podem ser feitas em um único lugar.

&nbsp;

***Em resumo:***

- `self._ativo` armazena o estado interno do *objeto* de forma *privada*.
- `@property` transforma o *método ativo* em uma propriedade, permitindo que você acesse o `_ativo` de forma mais natural e legível.

&nbsp;

***Exemplo de uso:***

```PY
restaurante_praca.ativo = True  # Isso chama a propriedade e muda o valor de _ativo para True
print(restaurante_praca.ativo)  # Imprime 'ativo'
```

&nbsp;

**Observação:** Embora não esteja presente no código, também pode definir um `setter` para a propriedade *ativo* usando o decorador `@ativo.setter`. Isso permitiria que atribuir novos valores ao *atributo* `_ativo` de forma controlada.

&nbsp;

***Exemplo com setter:***

```PY
@ativo.setter
def ativo(self, valor):
    if isinstance(valor, bool):
        self._ativo = valor
    else:
        raise ValueError("O valor deve ser um booleano")
```

Com essa implementação, garantiria que o *atributo* `_ativo` só possa receber valores *booleanos*.

&nbsp;

***Em resumo:***
- O uso combinado de *atributos privados* e *propriedades* em *Python* é uma prática comum para *encapsular* o estado de um *objeto* e fornecer uma *interface* mais clara e segura para interagir com ele.

&nbsp;

#### Aprofundando em propriedades

**Aplicado os recursos `.title()`, `.upper()`, `_nome` e `_categoria`.**

- `.title()`: inicia a primeira letra em maiusculo.
- `.upper()`: transforma todo o dado em letras maiusculas.
- `_nome`: armazena o estado interno do *objeto* de forma *privada*.
- `_categoria`: armazena o estado interno do *objeto* de forma *privada*.

&nbsp;

**Exemplo**

```PY
class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        Restaurante.restaurantes.append(self)

    def listar_restaurantes():
        print(f'{'Nome restaurante'.ljust(20)} | Categoria')

        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria}')

restaurante_praca = Restaurante('praca', 'Arabe')

Restaurante.listar_restaurantes()

# Saida:
# Nome restaurante     | Categoria
# Praca                | ARABE
```

&nbsp;

#### Metodos de classes

**Aplicado o *decorador* `@classmethod`, o *parametro* `cls` e o novo *metodo* `alternar_estado()`.**

```PY
class Restaurante:
    restaurantes = []

    def __init__(self):
        self._ativo = False
        Restaurante.restaurantes.append(self)

    @classmethod
    def listar_restaurantes(cls):
        print('Status')

        for restaurante in cls.restaurantes:
            print(f'{restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧ ativo' if self._ativo else '☐ ativo'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

restaurante1 = Restaurante()
restaurante1.alternar_estado()

Restaurante.listar_restaurantes()
```

&nbsp;

**Entendendo `@classmethod` e `cls` em Python.**

***O que é `@classmethod`?***

O *decorador* `@classmethod` em *Python* transforma um *método de classe* em um *método* que pode ser chamado diretamente na *classe*, sem a necessidade de *instanciar* um *objeto*. Em outras palavras, ele permite que acesse e modifique *atributos* de *classe* diretamente a partir da *classe*, sem precisar de uma *instância* específica.

&nbsp;

***O parâmetro `cls`.***

Quando você usa `@classmethod`, o primeiro *parâmetro do método*, por convenção, é chamado de `cls`. Ele representa a própria *classe*, não uma *instância* da *classe* como `self`.

- **`self`:** Refere-se à *instância* específica de uma *classe*. É usado dentro dos *métodos* de *instância* para acessar os *atributos* e *métodos* daquela *instância* particular.
- **`cls`:** Refere-se à *classe* em si. É usado dentro dos *métodos* de *classe* para acessar *atributos* e *métodos* da classe, ou para criar novas *instâncias* da *classe*.

&nbsp;

***Por que usar `@classmethod`?***

- **Métodos de fábrica:** Criar *métodos* que retornam novas *instâncias* da *classe*, potencialmente com argumentos diferentes do *construtor* padrão.
- **Métodos utilitários:** Implementar *métodos* que operam em toda a classe, como *métodos* para contar o número de *instâncias* ou para acessar *atributos* de *classe*.
- **Métodos que não precisam de uma instância:** Criar *métodos* que podem ser chamados diretamente na *classe* sem a necessidade de criar um objeto.

&nbsp;

***Relacionamento entre `@classmethod` e `@property`***

*`@classmethod` e `@property` são *decoradores* com propósitos diferentes:*

- **`@classmethod`:** Transforma um *método* em um *método* de *classe*, permitindo o acesso à *classe* e seus *atributos*.
- **`@property`:** Permite que um *método* seja acessado como se fosse um *atributo*, oferecendo um mecanismo para encapsular a lógica de acesso a dados.

&nbsp;

***Eles não têm uma relação direta, mas podem ser usados em conjunto:***

- Uma *propriedade* pode chamar um *método* de *classe* para obter um valor.
- Um *método* de *classe* pode usar *propriedades* para acessar os *atributos* de uma *instância*.

&nbsp;

**Analisando o código**

***No código, o *método* `listar_restaurantes` é um `@classmethod`:***

- **Não precisa de uma instância:** Pode ser chamado diretamente na *classe* `Restaurante`.
- **Acessa a lista de restaurantes:** Usa `cls.restaurantes` para acessar a lista de todos os restaurantes, que é um *atributo* de *classe*.
- **Imprime informações:** Imprime o status de cada restaurante.

&nbsp;

***Por que usar cls.restaurantes em vez de self.restaurantes?***

Porque a lista de *restaurantes* é um *atributo* da *classe*, não de cada *instância*. Ao usar `cls.restaurantes`, garante que está acessando a lista compartilhada por todos os objetos da classe `Restaurante`.

&nbsp;

***Em resumo:***

- `@classmethod` permite criar *métodos* que operam no nível da *classe*, não da *instância*.
- `cls` representa a própria *classe* dentro de um *método de classe*.
- `@property` permite que um *método* seja acessado como um *atributo*.

&nbsp;

**Exercicios**

01. Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.')

```PY
class ContaBancaria1:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False

pessoa1_conta_bancaria1 = ContaBancaria1('Raissa',200)

print(f'A conta de {pessoa1_conta_bancaria1.titular} esta com status {pessoa1_conta_bancaria1._ativo} e tem saldo de {pessoa1_conta_bancaria1.saldo} bitcoins')
```

&nbsp;

02. Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.')

```PY
class ContaBancaria2:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'A conta de {self.titular} esta com status {self._ativo} e tem saldo de {self.saldo} bitcoin'
    
pessoa1_conta_bancaria2 = ContaBancaria2('Zahira', 500)
pessoa2_conta_bancaria2 = ContaBancaria2('Aada', 100)

print(pessoa1_conta_bancaria2)
print(pessoa2_conta_bancaria2)
```

&nbsp;

03. Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.')

```PY
class ContaBancaria3:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'A conta de {self.titular} esta com status {self._ativo} e tem saldo de {self.saldo} bitcoin'
    
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True

pessoa1_conta_bancaria3 = ContaBancaria3('Emma',150)
print(pessoa1_conta_bancaria3)

ContaBancaria3.ativar_conta(pessoa1_conta_bancaria3)
print(pessoa1_conta_bancaria3)
```

&nbsp;

04. Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.')

```PY
class ContaBancaria4:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'A conta de {self.titular} esta com status {self._ativo} e tem saldo de {self.saldo} bitcoin'
    
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True

    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def ativo(self):
        return self._ativo
```

&nbsp;

05. Crie uma instância da classe e imprima o valor da propriedade titular.')

```PY
class ContaBancaria5:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'A conta de {self.titular} esta com status {self._ativo} e tem saldo de {self.saldo} bitcoin'
    
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True

    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def ativo(self):
        return self._ativo

pessoa1_conta_bancaria5 = ContaBancaria5('Sofia', 450)
print(f'O titular da conta bancaria: {pessoa1_conta_bancaria5.titular}')
```

&nbsp;

06. Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.')

```PY
class ClienteBanco1:
    def __init__(self, nome, conta, idade, origem, profissao):
        self._nome = nome.title()
        self._conta = conta
        self._idade = idade
        self._origem = origem.title()
        self._profissao = profissao.upper()

conta1_cliente_banco1 = ClienteBanco1('Caitlyn', 87245, 38, 'irlanda', 'biologa')
conta2_cliente_banco1 = ClienteBanco1('Elizabeth', 3901, 35, 'inglaterra', 'investidora')
conta3_cliente_banco1 = ClienteBanco1('Chloe', 65812, 25, 'gracia', 'atleta olimpica')

print(f'{vars(conta1_cliente_banco1)}\n{vars(conta2_cliente_banco1)}\n{vars(conta3_cliente_banco1)}')

# EXERCICIO 7
print('\n7. Crie um método de classe para a conta ClienteBanco.')

class ClienteBanco2:
    def __init__(self, nome, conta, idade, origem, profissao):
        self._nome = nome.title()
        self._conta = conta
        self._idade = idade
        self._origem = origem.upper()
        self._profissao = profissao.upper()

    @classmethod
    def conta(cls, titular, saldo):
        conta = ClienteBanco2(titular, saldo)
        return conta

conta1_cliente_banco2 = ClienteBanco2('Charlotte', 427, 43, 'franca', 'CEO')
conta2_cliente_banco2 = ClienteBanco2('Emily', 98630, 21, 'alemanha', 'duble')

print(f'{vars(conta1_cliente_banco2)}\n{vars(conta2_cliente_banco2)}\n')
```

&nbsp;
&nbsp;

### 04 - Importando classe e composicao

**Topicos do capitulo:**

- From e import
- Criando classe de avaliacao
- Composicao
- Listando avaliacoes

&nbsp;

#### OO Sabor Express

Versao final dos *codigos* do capitulo:

**`restaurante.py`**

```PY
# oo-sabor-express/modelos/restaurante.py

from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliacao'.ljust(20)} | Status')

        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacao).ljust(20)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧ ativo' if self._ativo else '☐ ativo'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return 0
        
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media_notas = round(soma_notas / quantidade_notas,1)

        return media_notas
```

&nbsp;

**`avaliacao.py`**

```PY
# oo-sabor-express/modelos/avaliacao.py

class Avaliacao:
    def __init__(self, cliente, nota):
        self._cliente = cliente
        self._nota = nota
```

&nbsp;

**`app.py`**

```PY
# oo-sabor-express/app.py

from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_arabe = Restaurante('Al-Shabab', 'Arabe')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')
restaurante_brasileiro = Restaurante('bom de garfo', 'brasileiro')
restaurante_argentino = Restaurante('Ella', 'argentino')
restaurante_alemao = Restaurante('Munich', 'alemao')

restaurante_praca.alternar_estado()
restaurante_arabe.alternar_estado()
restaurante_mexicano.alternar_estado()
restaurante_brasileiro.alternar_estado()
restaurante_alemao.alternar_estado()

restaurante_praca.receber_avaliacao('Aada', 8)
restaurante_praca.receber_avaliacao('Raissa', 1.5)

restaurante_arabe.receber_avaliacao('Zahira', 9.9)
restaurante_arabe.receber_avaliacao('Emma', 7)
                   
restaurante_mexicano.receber_avaliacao('Sofia', 7.5)
restaurante_mexicano.receber_avaliacao('Caitlyn', 6.75)
restaurante_mexicano.receber_avaliacao('Elizabeth', 8.4)
                                       
restaurante_brasileiro.receber_avaliacao('Chloe', 4)
restaurante_brasileiro.receber_avaliacao('Charlotte', 5.25)

restaurante_alemao.receber_avaliacao('Emily', 10)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
```

&nbsp;

#### From e import

Agora que a *classe* está criada, vamos organizar o *código* para separar a definição da *classe* das *instâncias* criadas a partir dela, seguindo as boas práticas de projetos de *software*.

O arquivo `restaurante.py` será dedicado exclusivamente à definição da classe `Restaurante`, encapsulando todas as suas *propriedades* e *métodos*.

Para encapsular a lógica de criação, manipulação e acesso às *instâncias*, bem como outros recursos necessários, será criado um arquivo específico.

O arquivo principal da aplicação, `app.py`, será criado no *diretório* raiz do projeto, `oo-sabor-express`, paralelamente ao *diretório* `modelos`, onde esta a *classe* `Restaurante`.

O arquivo `app.py` servirá como ponto de entrada da *aplicação*. Para impedir que seja importado como um *módulo* e executado diretamente, incluiremos o seguinte código:

```PY
from modelos.restaurante import Restaurante

restaurante_arabe = Restaurante('Al-Shabab', 'Arabe')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japonesa = Restaurante('Japa', 'Japonesa')

restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
```

&nbsp;

**O Diretório `__pycache__` em Python**

O `__pycache__` é uma forma mais simples do *Python* interpretar o *módulo* importado, ou seja, é um *diretório* que o *Python* cria para armazenar os arquivos compilados em `bytecode`. Que é uma forma que ele tem de interpretar os códigos de uma maneira muito mais simples do que no arquivo original.

&nbsp;

***O que é?***

O *diretório* `__pycache__` é uma pasta criada automaticamente pelo interpretador *Python* para armazenar ***versões compiladas (`bytecode`)*** dos seus *módulos Python*. Esses arquivos compilados, geralmente com extensão `.pyc` ou `.pyo`, são uma forma otimizada do código fonte que o *Python* utiliza para executar seus programas mais rapidamente.

&nbsp;

***Por que ele existe?***

- **Otimização:** Ao compilar o código para *bytecode*, o interpretador *Python* economiza tempo na análise e compilação do código fonte a cada execução. Isso torna a execução de programas *Python* mais rápida, especialmente ao importar módulos frequentemente.
- **Cache:** Os arquivos `.pyc` servem como um *cache* do código compilado. Quando você modifica um arquivo `.py`, o *Python* detecta a alteração e regenera o arquivo `.pyc` correspondente.

&nbsp;

***Como funciona?***

- **Compilação:** Quando executa um *script Python* ou importa um *módulo*, o *interpretador Python* compila o código fonte em *bytecode* e armazena o resultado em um arquivo `.pyc` dentro do *diretório* `__pycache__`.
- **Execução:** Nas execuções subsequentes, se o arquivo `.pyc` não estiver desatualizado (ou seja, se o arquivo `.py` correspondente não foi modificado), o *Python* utiliza diretamente o *bytecode*, pulando a etapa de compilação.

&nbsp;

***Estrutura dos arquivos .pyc:***

- **Nome:** O nome do arquivo `.pyc` corresponde ao nome do *módulo Python*, com a extensão `.pyc`.
- **Conteúdo:** O arquivo contém o *bytecode do módulo*, que é uma representação intermediária do código *Python* mais próxima do código de máquina.
- **Versão:** O formato do *bytecode* pode variar entre diferentes versões do *Python*, o que significa que arquivos `.pyc` criados em uma versão podem não ser compatíveis com outras versões.

&nbsp;

***Por que `__pycache__`?***

- **Convenção:** O uso de dois *underscores* no início do nome do *diretório* indica que ele é um *diretório interno* e não deve ser modificado manualmente.
- **Organização:** Agrupa os arquivos compilados em um único local, mantendo a organização do projeto.

&nbsp;

***Você precisa se preocupar com `__pycache__`?***

- **Normalmente não:** O *Python* cuida automaticamente da criação e atualização dos arquivos `.pyc`.
- **Ignorar em versionamento:** É comum adicionar o *diretório* `__pycache__` ao arquivo `.gitignore` para evitar que ele seja versionado.

&nbsp;

***Em resumo:***

O *diretório* `__pycache__` é uma parte essencial do mecanismo de execução do *Python*, otimizando a performance ao armazenar versões compiladas dos seus módulos. A compreensão do seu funcionamento pode ajudar a entender melhor como o *Python* executa seus programas.

&nbsp;

#### Criando classe de avaliacao

Neste tópico, adicionaremos ao sistema a avaliação dos restaurantes, vamos criar a *classe* `Avaliação` em um novo arquivo, `avaliacao.py`, dentro do *diretório* `modelos`.

No arquivo `avaliacao.py`, vamos criar um *modulo construtor* que recebe dois *parametros*, `cliente` e `nota`.

**`avaliacao.py`**

```PY
# avaliacao.py

class Avaliacao:
    def __init__(self, cliente, nota):
        self._cliente = cliente
        self._nota = nota
```

Com a criacao da nova *classe* `Avaliacao`, precisamos relacionar com a *classe* `Restaurante` do arquivo `restaurante.py`.

O codigo `restaurante.py` com as linhas adicionadas com comentario:

```PY
# restaurante.py

from modelos.avaliacao import Avaliacao # importamos a classe Avaliacao do arquivo acaliacao.py.

class Restaurante:
    # código omitido

    def __init__(self, nome, categoria):
        # código omitido
        self._avaliacao = [] # adicionamos um novo atributo referente a funcao de avaliacao do restaurante.
        # código omitido

    # código omitido

    def receber_avaliacao(self, cliente, nota): # criamos o modulo receber_avaliacao com os parametros cliente e nota, referente aos parametros e atributos da classe Avaliacao importada do arquivo avaliacai.py.
        avaliacao = Avaliacao(cliente, nota) # a variavel avaliacao recebe a classe Avaliacao com seus dois paramentros criados, o cliente e nota.
        self._avaliacao.append(avaliacao) # append tem a funcao de acrescentar toda a informacao adicionada ao atributo self._avaliacao, no caso, sempre adiciona os parametros da classe Avaliacao.
```

Tambem podemos adicionar o *codigo* no `app.py` chamando o *modulo* `receber_avaliacao`.

```PY
# app.py

from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')

restaurante_praca.receber_avaliacao('Zahira', 10)
restaurante_praca.receber_avaliacao('Aada', 8)
restaurante_praca.receber_avaliacao('Raissa', 9.5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
```

&nbsp;

#### Composicao

Adicionamos o *metodo* `media_avaliacao` na *classe* `Restaurante`.

Novo bloco de codigo com comentario.

```PY
# restaurante.py

    # código omitido

    @property # adicionamos o metodo especial @property para possibilitar o acesso do metodo media_avaliacao.
    def media_avaliacao(self): # metodo avaliacao com parametro self, isso quer dizer que ele tem acesso a todos os atributos e métodos da instância da classe que o chamou.
        if not self._avaliacao: # condicional if que verifica se nao ainda nao existe avaliacao do restaurante
            return 0 # se a condicao confirmar, retorno como o valor 0
        
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao) # sum tem a funcao de somar todas as notas do restaurante, buscando a avaliacao do metodo recever_avaliacao
        quantidade_notas = len(self._avaliacao) # len tem a funcao de fazer contagem de quantas notas existem do restaurante
        media_notas = round(soma_notas / quantidade_notas,1) # a variavel media_notas faz a media da soma_notas por quantidade_notas, com a funcao round para arredondar as casas decimais para 1

        return media_notas # retorna a media das notas do restaurante
```

&nbsp;

#### Listando avaliacoes

Adicionamos a media de avaliacoes na lista de restaurantes do *metodo* `listar_restaurantes`, junto com nome, categoria e ativo.

Alteracao do codigo com comentario.

```PY
# restaurante.py

    # código omitido

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliacao'.ljust(20)} | Status') # adicionamos

        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacao).ljust(20)} | {restaurante.ativo}')

    # código omitido
```

&nbsp;

**Exercicios**

***`importando_classe_e_composicao/exercicios.py`***

01. Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.')

```PY
class Livro1:
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
```

&nbsp;

02. Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.')

```PY
class Livro2:
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True

    def __str__(self):
        return f'O livro {self._titulo}, escrito por {self._autor}, foi publicado no ano de {self._ano_publicacao}'
    
livro2_hp3 = Livro2('Harry Potter e o Prisioneiro de Azkaban', 'J.K. Rowling', 1999)
livro2_sa3 = Livro2('O Senhor dos Anéis - O Retorno do Rei', 'J.R.R. Tolkien', 1955)
livro2_gt5 = Livro2('As Crônicas de Gelo e Fogo - A Dança dos Dragões', 'George R.R. Martin', 2011)

print(f'\n{livro2_hp3}\n{livro2_sa3}\n{livro2_gt5}')
```

&nbsp;

03. Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.')

```PY
class Livro3:
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True

    def __str__(self):
        return f'O livro {self._titulo}, escrito por {self._autor}, publicado no ano de {self._ano_publicacao} esta {self._disponivel}'
    
    def emprestar(self):
        #self._disponivel = False
        self._disponivel = not self._disponivel

livro3_hp4 = Livro3('Harry Potter e o Cálice de Fogo', 'J.K. Rowling', 2000)

livro3_hp4.emprestar()

print(livro3_hp4)
```

&nbsp;

04. Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.')

```PY
class Livro4:
    livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro4.livros.append(self)

    def __str__(self):
        return f'O livro {self._titulo}, escrito por {self._autor}, publicado no ano de {self._ano_publicacao} esta {self._disponivel}'
    
    def emprestar(self):
        self._disponivel = not self._disponivel

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = []
        for livro in Livro4.livros:
            if livro._ano_publicacao == ano and livro._disponivel:
                livros_disponiveis.append(livro)
        # VALIDAR LINHA ABAIXO
        #livros_disponiveis = [livro for livro in Livro4.livros if livro.ano_publicacao == ano and livro.disponivel]
        return livros_disponiveis
        

livro4_hp4 = Livro4('Harry Potter e o Cálice de Fogo', 'J.K. Rowling', 2000)
livro4_sa = Livro4("O Senhor dos Anéis - As Duas Torres", "J.R.R. Tolkien", 1954)
livro4_hp1 = Livro4("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997)

#livro4_hp4.emprestar()

livros_2000 = Livro4.verificar_disponibilidade(2000)
print(livros_2000)
```

&nbsp;

05. Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.')

```PY
from models.livros import Livro
```

&nbsp;

06. No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.')

```PY
livro_hp4 = Livro('Harry Potter e o Cálice de Fogo', 'J.K. Rowling', 2000)
livro_hp4.emprestar()

print(livro_hp4)
```

&nbsp;

07. No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.')

```PY
ano_especifico = 2000
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)

print(livros_2000)
```

&nbsp;

08. Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.')

```PY
from models.livros import Livro

livro_hp4 = Livro('Harry Potter e o Cálice de Fogo', 'J.K. Rowling', 2000)
livro_hp4_1 = Livro('Harry Potter e o Cálice de Fogo', 'J.K. Rowling', 2000)

print(livro_hp4)

livro_hp4.emprestar()
print(livro_hp4)

livros_2000 = Livro.verificar_disponibilidade(2000)
print(livros_2000)
```

**`livros.py`**

```PY
# 05. importando_classe_e_composicao/book-library/models/livros.py

class Livro:
    lista_livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.lista_livros.append(self)

    def __str__(self):
        return f'O livro {self._titulo}, escrito por {self._autor}, publicado no ano de {self._ano_publicacao}'
    
    @classmethod
    def listar_livros(cls):
        print(f'{'Nome livro'.ljust(60)} | {'Autor'.ljust(60)} | {'Ano Publicacao'.ljust(60)} | Disponivel')

        for livro in cls.lista_livros:
            print(f'{livro._titulo.ljust(60)} | {livro._autor.ljust(60)} | {str(livro._ano_publicacao).ljust(60)} | {livro._disponivel}')

    @property
    def disponibilidade(self):
        return f'O livro {self._titulo}, escrito por {self._autor}, publicado no ano de {self._ano_publicacao} esta disponivel' if self._disponivel else f'O livro {self._titulo} esta indisponivel'
    
    def emprestar(self):
        self._disponivel = not self._disponivel

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = []
        for livro in Livro.lista_livros:
            if livro._ano_publicacao == ano and livro._disponivel:
                livros_disponiveis.append(livro)
        return f'{livros_disponiveis}'
```

**`biblioteca.py`**

```PY
# 05. importando_classe_e_composicao/book-library/biblioteca.py

from models.livros import Livro

livro_hp4 = Livro('Harry Potter e o Cálice de Fogo', 'J.K. Rowling', 2000)
livro_sa2 = Livro("O Senhor dos Anéis - As Duas Torres", "J.R.R. Tolkien", 1954)
livro_hp1 = Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997)
livro_sa3 = Livro('O Senhor dos Anéis - O Retorno do Rei', 'J.R.R. Tolkien', 1955)
livro_gt5 = Livro('As Crônicas de Gelo e Fogo - A Dança dos Dragões', 'George R.R. Martin', 2011)

print(livro_hp4)

livro_hp4.emprestar()
print(livro_hp4)

livros_2000 = Livro.verificar_disponibilidade(2000)
print(livros_2000)

Livro.listar_livros()
print(livro_hp4.disponibilidade)
```

&nbsp;
&nbsp;

### 05 - Consolidado conhecimento

**Topicos do capitulo:**

- Condicional no metodo `receber_avaliacao`
- Adicionando saida no metodo `media_avaliacao`
- Colocando *docstring* na classe `Restaurante` 

&nbsp;

#### OO Sabor Express

Versao final do *codigo* do capitulo:

```PY
from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        """
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        """Retorna uma representação em string do restaurante."""
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        """Exibe uma lista formatada de todos os restaurantes."""
        print(f'{'Nome restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliacao'.ljust(20)} | Status')

        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacao).ljust(20)} | {restaurante.ativo}')

    @property
    def ativo(self):
        """Retorna um símbolo indicando o estado de atividade do restaurante."""
        return '⌧ ativo' if self._ativo else '☐ ativo'
    
    def alternar_estado(self):
        """Alterna o estado de atividade do restaurante."""
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        """
        avaliacao = Avaliacao(cliente, nota)
        if 0 <= avaliacao._nota <= 5:
            self._avaliacao.append(avaliacao)
            print(f'A avaliacao de {avaliacao._cliente} foi de {avaliacao._nota}')
        else:
            print(f'Avaliacao de {avaliacao._nota} nao valida, a avaliacao de {avaliacao._cliente} precisa ser de 0 a 5')

    @property
    def media_avaliacao(self):
        """Calcula e retorna a média das avaliações do restaurante."""
        if not self._avaliacao:
            return 'Sem avaliacao'
        
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media_notas = round(soma_notas / quantidade_notas,1)

        return media_notas
```