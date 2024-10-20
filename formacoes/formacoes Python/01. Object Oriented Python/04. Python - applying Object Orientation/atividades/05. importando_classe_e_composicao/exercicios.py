# EXERCICIO 1
print('1. Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.')

class Livro1:
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True

#####################################################################################################################################################################################

# EXERCICIO 2
print('\n2. Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.')

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

#####################################################################################################################################################################################

# EXERCICIO 3
print('\n\n3. Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.')

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

#####################################################################################################################################################################################

# EXERCICIO 4
print('\n\n4. Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.')

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

#####################################################################################################################################################################################

# EXERCICIO 5
print('\n5. Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.')

from models.livros import Livro

#####################################################################################################################################################################################

# EXERCICIO 6
print('\n6. No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.')

livro_hp4 = Livro('Harry Potter e o Cálice de Fogo', 'J.K. Rowling', 2000)
livro_hp4.emprestar()

print(livro_hp4)

#####################################################################################################################################################################################

# EXERCICIO 7
print('\n7. No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.')

ano_especifico = 2000
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)

print(livros_2000)

#####################################################################################################################################################################################

# EXERCICIO 8
print('\n8. Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.')

from models.livros import Livro

livro_hp4 = Livro('Harry Potter e o Cálice de Fogo', 'J.K. Rowling', 2000)
livro_hp4_1 = Livro('Harry Potter e o Cálice de Fogo', 'J.K. Rowling', 2000)

print(livro_hp4)

livro_hp4.emprestar()
print(livro_hp4)

livros_2000 = Livro.verificar_disponibilidade(2000)
print(livros_2000)
