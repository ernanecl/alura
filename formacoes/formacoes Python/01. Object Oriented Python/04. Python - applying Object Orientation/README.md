### Python - aplicando a Orientação a Objetos

O que sera trabalhado durante o treinamento:

- Introdução: orientação a objetos (OO)
- Conceito de classe
- Atributos de instância
- Métodos

#### 01 - Classes

`Classe` é como um molde para criar objetos, a base da programação orientada a objetos em *Python*. Elas proporcionam uma forma eficiente e organizada de modelar o mundo real em seus programas.

Conceitos-chave:

- **Objeto**: Uma instância de uma classe. É a representação real de um objeto no seu programa.
- **atributos**: São as características de um objeto, como o nome, a idade, a cor, etc. Em uma classe, os *atributos* são definidos como variáveis.
- **métodos**: São as ações que um objeto pode realizar, como calcular, comparar, imprimir, etc. Em uma classe, os *métodos* são definidos como funções.

##### OO Sabor Express

Nessa etapa desenvolveu um arquivo `restaurante.py` para o primeiro contato e melhor entendimento sobre classes.

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

##### Por que usar classes?

- **Organização**: Agrupa dados (*atributos*) e funcionalidades (*métodos*) relacionados.
- **Reutilização**: Permite criar múltiplos objetos com a mesma estrutura.
- **Abstração**: Esconde a complexidade interna dos objetos, expondo apenas as interfaces necessárias.
- **Herança**: Permite criar novas classes a partir de classes existentes, reutilizando código e criando hierarquias de classes.
- **Polimorfismo**: Permite que objetos de diferentes classes sejam tratados de forma uniforme.


##### Tópicos para explorar:

**Herança**: Como criar novas classes a partir de classes existentes.
**Polimorfismo**: Como tratar objetos de diferentes classes de forma uniforme.
**Encapsulamento**: Como esconder os detalhes internos de uma classe.
**métodos especiais**: *métodos* como `__str__`, `__repr__`, `__eq__`, etc.

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