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