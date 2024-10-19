### Python - aplicando a Orientação a Objetos

O que sera trabalhado durante o treinamento:

- Introdução: orientação a objetos (OO)
- Conceito de classe
- Atributos de instância
- Métodos

&nbsp;
&nbsp;

#### 01 - Classes

Topicos trabalhados no capitulo

- Classes
- Atributos de instancia
- Funcoes

&nbsp;

##### OO Sabor Express

Neste capitulo iniciou com a criacao de um novo arquivo chamado `restaurante.py`, nele trabalhou com as funcionalidades basicas sobre **classes**.

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

&nbsp;

##### Classe

`Classe` é como um molde para criar objetos, a base da programação orientada a objetos em *Python*. Elas proporcionam uma forma eficiente e organizada de modelar o mundo real em seus programas.

Conceitos-chave:

- **Objeto**: Uma instância de uma classe. É a representação real de um objeto no seu programa.
- **atributos**: São as características de um objeto, como o nome, a idade, a cor, etc. Em uma classe, os *atributos* são definidos como variáveis.
- **métodos**: São as ações que um objeto pode realizar, como calcular, comparar, imprimir, etc. Em uma classe, os *métodos* são definidos como funções.

&nbsp;

##### Exemplo

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

##### Por que usar classes?

- **Organização**: Agrupa dados (*atributos*) e funcionalidades (*métodos*) relacionados.
- **Reutilização**: Permite criar múltiplos objetos com a mesma estrutura.
- **Abstração**: Esconde a complexidade interna dos objetos, expondo apenas as interfaces necessárias.
- **Herança**: Permite criar novas classes a partir de classes existentes, reutilizando código e criando hierarquias de classes.
- **Polimorfismo**: Permite que objetos de diferentes classes sejam tratados de forma uniforme.

&nbsp;

##### Tópicos para explorar:

**Herança**: Como criar novas classes a partir de classes existentes.
**Polimorfismo**: Como tratar objetos de diferentes classes de forma uniforme.
**Encapsulamento**: Como esconder os detalhes internos de uma classe.
**métodos especiais**: *métodos* como `__str__`, `__repr__`, `__eq__`, etc.

&nbsp;

##### *dir()* e *vars()*

As funções `dir()` e `vars()` permitem trabalhar com os *atributos* e *métodos* de objetos, especialmente quando se trabalha com classes.

***dir()***

- **Retorna**: Uma lista de strings contendo os nomes de todos os *atributos* e *métodos* de um objeto, incluindo aqueles herdados de classes-pai.
- **Alcance**: Vai além dos *atributos* definidos diretamente no objeto, exibindo também *atributos* de classes e *métodos* especiais (como __init__, __str__, etc.).
- **Uso**:
    - **Exploração**: Para descobrir quais *atributos* e *métodos* um objeto possui.
    - **Depuração**: Para verificar se um *atributo* está sendo definido corretamente.
    - **Introspeção**: Para entender a estrutura de um objeto.

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

A saída de `dir(pessoa1)` lista os *atributos* definidos na classe como `nome`, `idade`, `cumprimentar`, além de outros *atributos* e *métodos* herdados da *classe* base `object`.

***vars()***

- **Retorna**: Um dicionário que mapeia os nomes dos *atributos* de um objeto aos seus valores correspondentes.
- **Alcance**: Se limita aos *atributos* definidos diretamente no objeto, não incluindo *atributos* de classes ou *métodos* especiais.
- **Uso**:
    - **Acesso aos valores**: Para obter os valores dos *atributos* de um objeto de forma direta.
    - **Modificação**: Para modificar os valores dos *atributos* de um objeto.

***Exemplo:***

```PY
print(vars(pessoa1))
```

A saída de `vars(pessoa1)` será um ***dicionário*** como `{'nome': 'Alice', 'idade': 30}`.


***Diferenças e Quando Usar Cada Uma***

| **Característica** | **dir()** | **vars()**
|---|---|---|
| *Tipo de retorno* | Lista de strings | Dicionário
| *Alcance* | Todos os *atributos* (incluindo herdados) | Apenas *atributos* definidos diretamente
| *Uso principal* | Exploração, depuração | Acesso e modificação de *atributos*


- Use `dir()` quando quiser obter uma visão geral completa dos *atributos* e *métodos* de um *objeto*, incluindo aqueles *herdados*.
- Use `vars()` quando precisar acessar ou modificar os valores dos *atributos* de um *objeto* de forma direta.

&nbsp;

##### Exercicios

```PY
# EXERCICIO 1
print("1 - Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.")
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

# EXERCICIO 2
print("\n2 - Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.")

nome_do_restaurante = restaurante_praca.nome
print(nome_do_restaurante)

# EXERCICIO 3
print("\n3 - Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.")

check1 = 'Restaurante esta ativo' if restaurante_praca.ativo == True else 'Nao esta ativo'
print(check1)

#############################
#OUTRO METODO PARA A QUESTAO#
#############################

if restaurante_praca.ativo:
    print('O restaurante está ativo.')
else:
    print('O restaurante está inativo.')

# EXERCICIO 4
print("\n4 - Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.")

categoria = Restaurante()
print(Restaurante.categoria)

#############################
#OUTRO METODO PARA A QUESTAO#
#############################

categoria1 = Restaurante.categoria
print(categoria1)

# EXERCICIO 5
print("\n5 - Altere o valor do atributo nome para 'Bistrô'.")

restaurante_praca.nome = 'Bistrô'
print(restaurante_praca.nome)

# EXERCICIO 6
print("\n6 - Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.")

restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

print(restaurante_pizza.nome)
print(restaurante_pizza.categoria)

# EXERCICIO 7
print("\n7 - Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.")

check2 = f'O restaurante {restaurante_pizza.nome} é categoria Fast Food' if restaurante_pizza.categoria == 'Fast Food' else f'O restaurante {restaurante_pizza.nome} NAO é categoria Fast Food'
print(check2)

#############################
#OUTRO METODO PARA A QUESTAO#
#############################

if restaurante_pizza.categoria == 'Fast Food':
    print('A categoria é Fast Food.')
else:
    print('A categoria não é Fast Food.')

# EXERCICIO8
print("\n8 - Mude o estado da instância restaurante_pizza para ativo.")

print(f'O restaurante {restaurante_pizza.nome} esta com estado ativo como {restaurante_pizza.ativo}')

if restaurante_pizza.ativo == False:
    restaurante_pizza.ativo = True
    print(f'Agora o restaurante {restaurante_pizza.nome} esta com estado ativo como {restaurante_pizza.ativo}')
else:
    print(f"O restaurante {restaurante_pizza.nome} já está ativo")

#############################
#OUTRO METODO PARA A QUESTAO#
#############################

restaurante_pizza.ativo = True

# EXERCICIO
print("\n9 - Imprima no console o nome e a categoria da instância restaurante_praca.")

print(restaurante_praca.nome)
print(restaurante_praca.categoria)

#############################
#OUTRO METODO PARA A QUESTAO#
#############################

print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')
```
&nbsp;
&nbsp;

#### 02 - Construtor e instanciando objetos

Topicos trabalhados no capitulo

- Construtor
- Metodos especiais
- Criando metodos

&nbsp;

##### OO Sabor Express

Nessa etapa trabalhou com metodos especiais `__init__` e `__str__`, alem de criar o proprio metodo.

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

&nbsp;

##### Construtor

***O Método init: O Construtor da Classe***

Em *Python*, o *método* `__init__` desempenha a funcao fundamental na criação de objetos a partir de uma classe.

Frequentemente chamado de *construtor*, pois é executado automaticamente quando uma nova *instância* (*objeto*) da *classe* é criada.

&nbsp;

**Qual a sua função principal?**

- **Inicializar atributos**: O `__init__` é utilizado para atribuir valores iniciais aos *atributos* de um *objeto*. Esses atributos definem as características e o estado de cada *instância* da *classe*.
- **Realizar outras tarefas de inicialização**: Além de atribuir valores, o `__init__` pode ser usado para realizar outras operações necessárias no momento da criação do *objeto*, como conectar a um *banco de dados*, carregar configurações, etc.

*Exemplo*

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

**Para que serve o `self`?**

- **Acessar atributos**: O `self` é usado para acessar e modificar os atributos de um objeto dentro de um método. Por exemplo, `self.nome` acessa o atributo nome da *instância* atual.
- **Chamar outros métodos**: O `self` também pode ser usado para chamar outros *métodos* da mesma *classe*.

*Exemplo*

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

**Por que usar self?**

- **Clareza**: O `self` torna explícito que estamos acessando *atributos* ou *métodos* de uma *instância* específica.
- **Evita confusões**: Ao usar `self`, evita conflitos entre nomes de variáveis locais e *atributos* da *classe*.

***O Método `__str__` em Python: Uma Representação Amigável dos Objetos***

O *método* `__str__` em *Python* é um *método* especial que retorna uma representação em *string* de um *objeto*.

Quando imprimir um *objeto* ou convertê-lo para uma *string*, o *Python* chama automaticamente este método para obter a representação a ser exibida.

&nbsp;

**Por que usar o __str__?**

- **Leiturabilidade**: Ao personalizar o *método* `__str__`, pode controlar como os *objetos* de sua *classe* são exibidos, tornando a saída mais clara e concisa para o usuário.
- **Depuração**: Durante o desenvolvimento, o *método* `__str__` pode ser muito útil para inspecionar o estado de um *objeto* e identificar possíveis problemas.
- **Interoperabilidade**: Ao definir um *método* `__str__` adequado, facilita a integração de seus objetos com outras ferramentas e bibliotecas que trabalham com *strings*.

&nbsp;

**Como funciona:**

- **Método especial**: O __str__ é um método "mágico" ou "dunder" (double underscore), o que significa que ele tem um significado especial para o interpretador Python.
- **Retorno**: O método deve retornar uma string que representa o objeto de forma clara e concisa.
- **Chamada automática**: Quando você tenta imprimir um objeto usando a função print() ou o operador str(), o Python chama o método __str__ do objeto automaticamente.

&nbsp;

**Comparação com `__repr__`:**

`__str__`: Destinado a fornecer uma representação amigável ao usuário, como se fosse para ser exibida em um *console* ou *log*.
`__repr__`: Destinado a fornecer uma representação não ambígua do *objeto*, ideal para depuração e reprodução do *objeto*. Geralmente é mais detalhado e pode incluir informações técnicas.

&nbsp;

**Quando usar `__str__` e `__repr__`?**

`__str__`: Para a maioria dos casos, quando você precisa de uma representação concisa e legível para o usuário final.
`__repr__`: Para depuração, geração de documentação ou quando você precisa de uma representação completa e inequívoca do *objeto*.

&nbsp;

**Exemplo com `__repr__`:**

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

##### Exercicios

```PY
# EXERCICIO 1
print('1 - Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.')

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

#####################################################################################################################################################################################

# EXERCICIO 2
print('\n2 - Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.')

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

#####################################################################################################################################################################################

# EXERCICIO 3
print('\n\n3 - Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.')

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


#####################################################################################################################################################################################

# EXERCICIO 4
print('\n\n4 - Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.')

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

#####################################################################################################################################################################################

# EXERCICIO 5
print('\n\n5 -Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.')

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
&nbsp;
